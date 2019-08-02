
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
    except Exception as ex:
        error = "Exception Contacting Endpoint: " + ex.__str__()

    return name, location, error


def make_request(address):
    with grpc.insecure_channel(address) as channel:
        stub = demo.DemoStub(channel)
        name, location, error = get_identity(stub)

        if not len(error):
            return "Hello, I'm " + name + " From The " + location
        else:
            return error


def main():
    cpp_address = 'localhost:6001'
    python_address = 'localhost:6002'

    print(make_request(cpp_address))
    print(make_request(python_address))


if __name__ == "__main__":
    print("Beginning Script")
    main()
    print("Script Complete")
