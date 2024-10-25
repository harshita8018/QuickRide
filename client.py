import sys
import grpc
import threading
import time
from protofiles import quick_ride_pb2
from protofiles import quick_ride_pb2_grpc

ports = ['localhost:50051', 'localhost:50052']

def driver_stream(stub, driver_id, decision_event, decision):
    while True:
        response = stub.DriverNotify(quick_ride_pb2.DriverRequest(driver_id=driver_id))
        for res in response:
            print(res)
            print("1. Accept\n2. Reject")
            print("Enter Your Choice")
            
            print("You have 10 seconds to respond...")
            decision[0] = None  
            decision_event.clear() 
            
            # Timer.....
            timer_thread = threading.Thread(target=timer, args=(decision_event,))
            timer_thread.start()

            while decision[0] is None:
                time.sleep(0.5)

            if decision[0]:
                stub.SendRideResponse(quick_ride_pb2.RideAccept(accept=decision[0], driver_id=driver_id))
            break  

def timer(event):
    time.sleep(10) 
    if not event.is_set():
        print("Time's up! Ride request automatically rejected.")
        event.set()  # Time expired....

def run(role, client_id, cert_file, key_file, ca_cert_file):
    choosen_port = []
    decision_event = threading.Event()  
    decision = [None]  # Shared variable....

    client_credentials = grpc.ssl_channel_credentials(
        root_certificates=open(ca_cert_file, 'rb').read(),
        private_key=open(key_file, 'rb').read(),
        certificate_chain=open(cert_file, 'rb').read()
    )

    drivers_count = []

    for port in ports:
        if len(choosen_port) > 0:
            break
        try:
            print(f"Trying to connect to {port}...")
            # with grpc.insecure_channel(port) as channel:
            with grpc.secure_channel(port, client_credentials) as channel:
                stub = quick_ride_pb2_grpc.QuickRideServiceStub(channel)
                
                response = stub.ServerStatus(quick_ride_pb2.ServerStatusRequest())
                
                print(f"Response from {port}:")
                print(f"Available Drivers: {response.available_drivers}")
                print(f"Rides Count: {response.rides_count}")

                # if response.available_drivers > 0 or response.rides_count < 3:
                if role == "rider" and response.available_drivers > 0:
                    choosen_port = [port]
                    break

                if role == "driver" and response.available_drivers < 5:
                    choosen_port = [port]
                    break

        except grpc.RpcError as e:
            print(f"Error connecting to {port}: {e}")
            # exit(1)
        
    mini = 999
    if len(choosen_port) == 0:
        for i in range(len(drivers_count)):
            if mini > drivers_count[i]:
                mini = drivers_count[i]
                choosen_port = [ports[i]]
    if len(choosen_port) == 0:
        choosen_port = [ports[0]]



    print("Connected with", choosen_port[0])
    with grpc.secure_channel(choosen_port[0], client_credentials) as channel:
    # with grpc.insecure_channel(choosen_port[0]) as channel:
            stub = quick_ride_pb2_grpc.QuickRideServiceStub(channel)
            response = stub.RegisterClient(quick_ride_pb2.RegisterRequest(role=role, client_id=client_id))
            print("Server response:", response.message)

            if role == 'rider':
                while True:
                    print("1. Ride Request \n2. Ride Status \n3. Exit")
                    choice = input("Enter your choice: ")
                    if choice == "1":
                        source = input("Enter Source: ")
                        dest = input("Enter Destination: ")
                        response = stub.RequestRide(quick_ride_pb2.RideRequest(client_id=client_id, source=source, dest=dest))
                        print(response.reply)
                        print()
                        
                    elif choice == "2":
                        response = stub.RideStatus(quick_ride_pb2.StatusRequest(client_id=client_id))
                        print(response.status)
                        print()
                    elif choice == "3":
                        print("Thank You!!!")
                        exit(1)
                    else:
                        print("Enter a valid choice")

            elif role == 'driver':
                print("Waiting for rides...")
                notification_thread = threading.Thread(target=driver_stream, args=(stub, client_id, decision_event, decision))
                notification_thread.daemon = True
                notification_thread.start()
                
                while True:
                    if decision[0] is None:  # Only ask for input if no decision has been made
                        # ch = input("Enter Your Choice (1 for Accept, 2 for Reject): ").strip()
                        ch = input()
                        if ch == "1":
                            decision[0] = "accept"
                            decision_event.set()  # Signal that a decision has been made
                        elif ch == "2":
                            decision[0] = "reject"
                            decision_event.set()  
                        else:
                            print("Invalid choice, please enter 1 or 2.")
                        
                        if decision[0] == "accept":
                            while(1):
                                ride_complete = input("Enter Y when the ride is completed\n")
                                if(ride_complete == 'Y'):
                                    response = stub.CompleteRide(quick_ride_pb2.RideComplete(driver_id=client_id))
                                    print(response.reply)
                                    break


if __name__ == '__main__':
    if len(sys.argv) != 6:
        print("Usage: client.py [role] [client_id] [cert_file] [key_file] [ca_cert_file]")
        sys.exit(1)
    
    role = sys.argv[1].lower()
    client_id = sys.argv[2]
    cert_file = sys.argv[3]
    key_file = sys.argv[4]
    ca_cert_file = sys.argv[5]
    # ca_cert_file = "ca.crt"  

    run(role, client_id, cert_file, key_file, ca_cert_file)
