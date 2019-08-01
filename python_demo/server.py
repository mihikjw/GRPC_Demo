
from concurrent import futures
import grpc
import time

import demo_pb2_grpc
import demo_pb2

ONE_DAY_IN_SECONDS = 60 * 60 * 24


class DemoServicer(demo_pb2_grpc.DemoServicer):
    "class for handling requests to the gRPC server"

    def GetIdentity(self, request, context):
        "handles requests for the 'rpc GetIdentity' endpoints"
        return demo_pb2.Identity(name="Eggs-Benedict Cumberland", location="Python3 Endpoint")


if __name__ == "__main__":
    print("Server Starting")

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    demo_pb2_grpc.add_DemoServicer_to_server(
        DemoServicer(),
        server
    )
    server.add_insecure_port("0.0.0.0:1234")
    server.start()

    try:
        while True:
            time.sleep(ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)
