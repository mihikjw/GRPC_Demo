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
    name = ""
    location = ""
    error = ""

    with grpc.insecure_channel(address) as channel:
        stub = demo.DemoStub(channel)
        name, location, error = get_identity(stub)

    return name, location, error
