import os
import subprocess
from grpc_tools import protoc


def clean_file(path):
    "deletes the given file if it exists"
    if len(path):
        if os.path.isfile(path):
            os.remove(path)
        return True
    return False


class ProtoGenerator():
    "class for generating proto files in the various required languages"

    @staticmethod
    def generate_proto_files():
        "generates all the required files for the demo"
        if ProtoGenerator.generate_python_files():
            return True
        return False

    @staticmethod
    def generate_python_files():
        "generates the python files"
        file1 = "demo_pb2_grpc.py"
        file2 = "demo_pb2.py"

        clean_file(file1)
        clean_file(file2)

        protoc.main(('', '-I.', '--python_out=.', '--grpc_python_out=.', 'demo.proto'))

        if os.path.isfile(file2) and os.path.isfile(file1):
            return True

        return False


if __name__ == "__main__":
    ProtoGenerator.generate_proto_files()
