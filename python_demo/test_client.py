
"""
A script to let you test the gRPC server endpoints as you're developing
"""

import grpc
import demo_pb2_grpc as demo
import demo_pb2 as demo_struct


def get_identity(stub):
    "returns the identity of the given stub"
    name = ""
    location = ""
    error = ""

    try:
        req_data = demo_struct.Identity(name="Michael Wittgreffe", location="Python Test Client")
        res_data = stub.GetIdentity(req_data)

        if res_data:
            if res_data.name and res_data.location:
                name = res_data.name
                location = res_data.location
            else:
                error = "Unable To Find Name Or Location"
        else:
            error = "Server Returned Incomplete"
    except Exception:
        error = "Exception Contacting Endpoint"

    return name, location, error


def main():
    cpp_address = 'localhost:6001'

    # get data from C++ demo app
    with grpc.insecure_channel(cpp_address) as channel:
        stub = demo.DemoStub(channel)
        name, location, error = get_identity(stub)

        if not len(error):
            print("Hello, I'm " + name + " From The " + location)
        else:
            print(error)


if __name__ == "__main__":
    print("Beginning Script")
    main()
    print("Script Complete")
