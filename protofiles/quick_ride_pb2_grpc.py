# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from protofiles import quick_ride_pb2 as protofiles_dot_quick__ride__pb2

GRPC_GENERATED_VERSION = '1.66.2'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in protofiles/quick_ride_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class QuickRideServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterClient = channel.unary_unary(
                '/QuickRideService/RegisterClient',
                request_serializer=protofiles_dot_quick__ride__pb2.RegisterRequest.SerializeToString,
                response_deserializer=protofiles_dot_quick__ride__pb2.RegisterResponse.FromString,
                _registered_method=True)
        self.RequestRide = channel.unary_unary(
                '/QuickRideService/RequestRide',
                request_serializer=protofiles_dot_quick__ride__pb2.RideRequest.SerializeToString,
                response_deserializer=protofiles_dot_quick__ride__pb2.RideResponse.FromString,
                _registered_method=True)
        self.DriverNotify = channel.unary_stream(
                '/QuickRideService/DriverNotify',
                request_serializer=protofiles_dot_quick__ride__pb2.DriverRequest.SerializeToString,
                response_deserializer=protofiles_dot_quick__ride__pb2.DriverResponse.FromString,
                _registered_method=True)
        self.SendRideResponse = channel.unary_unary(
                '/QuickRideService/SendRideResponse',
                request_serializer=protofiles_dot_quick__ride__pb2.RideAccept.SerializeToString,
                response_deserializer=protofiles_dot_quick__ride__pb2.RideAcceptMessage.FromString,
                _registered_method=True)
        self.RideStatus = channel.unary_unary(
                '/QuickRideService/RideStatus',
                request_serializer=protofiles_dot_quick__ride__pb2.StatusRequest.SerializeToString,
                response_deserializer=protofiles_dot_quick__ride__pb2.StatusResponse.FromString,
                _registered_method=True)
        self.CompleteRide = channel.unary_unary(
                '/QuickRideService/CompleteRide',
                request_serializer=protofiles_dot_quick__ride__pb2.RideComplete.SerializeToString,
                response_deserializer=protofiles_dot_quick__ride__pb2.CompleteReply.FromString,
                _registered_method=True)
        self.ServerStatus = channel.unary_unary(
                '/QuickRideService/ServerStatus',
                request_serializer=protofiles_dot_quick__ride__pb2.ServerStatusRequest.SerializeToString,
                response_deserializer=protofiles_dot_quick__ride__pb2.ServerStatusResponse.FromString,
                _registered_method=True)


class QuickRideServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RegisterClient(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RequestRide(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DriverNotify(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendRideResponse(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RideStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CompleteRide(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ServerStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QuickRideServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegisterClient': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterClient,
                    request_deserializer=protofiles_dot_quick__ride__pb2.RegisterRequest.FromString,
                    response_serializer=protofiles_dot_quick__ride__pb2.RegisterResponse.SerializeToString,
            ),
            'RequestRide': grpc.unary_unary_rpc_method_handler(
                    servicer.RequestRide,
                    request_deserializer=protofiles_dot_quick__ride__pb2.RideRequest.FromString,
                    response_serializer=protofiles_dot_quick__ride__pb2.RideResponse.SerializeToString,
            ),
            'DriverNotify': grpc.unary_stream_rpc_method_handler(
                    servicer.DriverNotify,
                    request_deserializer=protofiles_dot_quick__ride__pb2.DriverRequest.FromString,
                    response_serializer=protofiles_dot_quick__ride__pb2.DriverResponse.SerializeToString,
            ),
            'SendRideResponse': grpc.unary_unary_rpc_method_handler(
                    servicer.SendRideResponse,
                    request_deserializer=protofiles_dot_quick__ride__pb2.RideAccept.FromString,
                    response_serializer=protofiles_dot_quick__ride__pb2.RideAcceptMessage.SerializeToString,
            ),
            'RideStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.RideStatus,
                    request_deserializer=protofiles_dot_quick__ride__pb2.StatusRequest.FromString,
                    response_serializer=protofiles_dot_quick__ride__pb2.StatusResponse.SerializeToString,
            ),
            'CompleteRide': grpc.unary_unary_rpc_method_handler(
                    servicer.CompleteRide,
                    request_deserializer=protofiles_dot_quick__ride__pb2.RideComplete.FromString,
                    response_serializer=protofiles_dot_quick__ride__pb2.CompleteReply.SerializeToString,
            ),
            'ServerStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.ServerStatus,
                    request_deserializer=protofiles_dot_quick__ride__pb2.ServerStatusRequest.FromString,
                    response_serializer=protofiles_dot_quick__ride__pb2.ServerStatusResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'QuickRideService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('QuickRideService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class QuickRideService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RegisterClient(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/QuickRideService/RegisterClient',
            protofiles_dot_quick__ride__pb2.RegisterRequest.SerializeToString,
            protofiles_dot_quick__ride__pb2.RegisterResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RequestRide(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/QuickRideService/RequestRide',
            protofiles_dot_quick__ride__pb2.RideRequest.SerializeToString,
            protofiles_dot_quick__ride__pb2.RideResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DriverNotify(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/QuickRideService/DriverNotify',
            protofiles_dot_quick__ride__pb2.DriverRequest.SerializeToString,
            protofiles_dot_quick__ride__pb2.DriverResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SendRideResponse(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/QuickRideService/SendRideResponse',
            protofiles_dot_quick__ride__pb2.RideAccept.SerializeToString,
            protofiles_dot_quick__ride__pb2.RideAcceptMessage.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RideStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/QuickRideService/RideStatus',
            protofiles_dot_quick__ride__pb2.StatusRequest.SerializeToString,
            protofiles_dot_quick__ride__pb2.StatusResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CompleteRide(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/QuickRideService/CompleteRide',
            protofiles_dot_quick__ride__pb2.RideComplete.SerializeToString,
            protofiles_dot_quick__ride__pb2.CompleteReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ServerStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/QuickRideService/ServerStatus',
            protofiles_dot_quick__ride__pb2.ServerStatusRequest.SerializeToString,
            protofiles_dot_quick__ride__pb2.ServerStatusResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)