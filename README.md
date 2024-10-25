## Files

- `quickride.proto`: Protocol Buffers file that defines the service and messages.
- `server.py`: The gRPC server.
- `client.py`: The client that sends a requests to the server.
- `certificates and keys` 

## Generating Python Code from Proto File

Before running the server and client, generate the gRPC code from the `quickride.proto` file. Use the following command to compile the proto file:

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. quickride.proto
```

This will generate Python files for both the service and the messages.

## Running the Server

To start the gRPC server, run the following command:

```bash
python server.py --port 50051
python server.py --port 50052
python server.py --port 50053
```

- `--port` is a mandatory field and specifies the port the server will listen on. You can change `50051` to any other available port.

## Running the Client

To run the client and send a KNN query to the server, use the following command:

```bash
python client.py [role] [client_id] [cert_file] [key_file] [ca_cert]
```

- `role`: This should be either rider or driver.
- `client_id`: Each client should enter there unique ID.
- `cert_file`: Client Certificate
- `key_file`: Client Key
- `ca_file`: CA Certificate

## Assumptions
- Clients know the port numbers of available servers
- A client can book only one ride at a time
- Clients know there client ID
