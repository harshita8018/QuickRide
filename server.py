import sys
import grpc
from concurrent import futures
import time
import logging
from protofiles import quick_ride_pb2
from protofiles import quick_ride_pb2_grpc

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create file handler
file_handler = logging.FileHandler('quick_ride.log')
file_handler.setLevel(logging.INFO)

# Create console handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)

# Create a formatter and set it for both handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

class QuickRideService(quick_ride_pb2_grpc.QuickRideServiceServicer):
    def __init__(self):
        self.ride_count = 1
        self.drivers = {}           # {Driver ID    : availability}
        self.driver_streams = {}    # {Driver ID    : stream (context)}
        self.rides = {}             # {Client ID      : [Source, Destination, Driver ID, Status]}
        self.notification = {}      # {Driver ID    : [ride_requests]}
        self.driver_client = {}

    def RegisterClient(self, request, context):
        response = quick_ride_pb2.RegisterResponse()
        if request.role == 'driver':
            self.drivers[request.client_id] = True 
            logger.info(f"Driver registered: {request.client_id}")

        response.message = f"Client {request.client_id} with role {request.role} registered successfully."
        print(response.message)
        logger.info(response.message)
        return response
    
    def DriverNotify(self, request, context):
        driver_id = request.driver_id
        if driver_id not in self.notification:
            self.notification[driver_id] = []

        while True:
            if self.notification[driver_id]:
                notification = self.notification[driver_id].pop(0)
                yield notification  # This should already contain both ride_id and notification
            time.sleep(1)  # Keep the connection alive
        
    def SendRideResponse(self, request, context):
        logger.info(f"Driver {request.driver_id} responded: {request.accept}")
        if request.accept == 'accept':
            self.drivers[request.driver_id] = False
        return quick_ride_pb2.RideAcceptMessage(accept=request.accept, driver_id=request.driver_id)

    def RequestRide(self, request, context):
        client_id = request.client_id
        source = request.source
        dest = request.dest

        logger.info(f"Ride request received from: {client_id}, Source: {source}, Destination: {dest}")

        if client_id in self.rides:
            if "Progress" in self.rides[client_id][3]:
                return quick_ride_pb2.RideResponse(reply="Ride In Progress, book after this is completed!!!")

        ride_id = str(self.ride_count)
        self.rides[client_id] = [source, dest, "", "Looking for Drivers"]
        self.ride_count += 1

        available_drivers = [driver for driver, available in self.drivers.items() if available]
        
        if available_drivers:
            self.rides[client_id][3] = "Will get a driver"

            for driver in available_drivers:
                logger.info(f"Sent request to driver {driver}")
                self.notification[driver] = [quick_ride_pb2.DriverResponse(reply="Ride from " + source + " : " + dest)]
                time.sleep(10)
                
                driver_avail = self.drivers[driver]
                if not driver_avail:
                    logger.info(f"Driver {driver} accepted the ride.")
                    self.rides[client_id][3] = "In Progress"
                    self.drivers[driver] = False
                    self.driver_client[driver] = client_id
                    return quick_ride_pb2.RideResponse(reply="Driver Assigned Successful")
                logger.info(f"Driver Available: {driver}")

        else:
            logger.warning("No drivers available at the moment.")
            self.rides[client_id][3] = "No Drivers Available"
            return quick_ride_pb2.RideResponse(reply="No Drivers Available")
        
        self.rides[client_id][3] = "No Driver Accepted Your Ride"
        return quick_ride_pb2.RideResponse(reply="No Driver Accepted Your Ride")
    
    def RideStatus(self, request, context):
        client_id = request.client_id
        if client_id not in self.rides:
            return quick_ride_pb2.StatusResponse(status="Never Booked a Ride...!!!")
        logger.info(f"Status requested for client: {client_id}. Current status: {self.rides[client_id][3]}")
        return quick_ride_pb2.StatusResponse(status=self.rides[client_id][3])
    
    def CompleteRide(self, request, context):
        rider_id = self.driver_client[request.driver_id]
        self.rides[rider_id][3] = "Completed"
        self.drivers[request.driver_id] = True
        logger.info(f"Ride completed for driver: {request.driver_id}.")
        return quick_ride_pb2.CompleteReply(reply="DONE!!!")
    
    def ServerStatus(self, request, context):
        # print("Ok")
        available_drivers = len(self.drivers)
        rides_count = len(self.rides)
        return quick_ride_pb2.ServerStatusResponse(available_drivers = available_drivers, rides_count = rides_count)

def serve(port):
    server_key = './certificates/server.key'
    server_cert = './certificates/server.crt'
    ca_cert = './certificates/ca.crt'

    server_credentials = grpc.ssl_server_credentials(
        [(open(server_key, 'rb').read(), open(server_cert, 'rb').read())],
        root_certificates=open(ca_cert, 'rb').read(),
        require_client_auth=True  
    )

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    quick_ride_pb2_grpc.add_QuickRideServiceServicer_to_server(QuickRideService(), server)
    
    # server.add_insecure_port(f'[::]:{port}')
    server.add_secure_port(f'[::]:{port}', server_credentials)
    server.start()
    logger.info(f"Server is running on port {port}...")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("You have not entered a port number.")
        sys.exit(1)
    
    port = sys.argv[1]
    serve(port)