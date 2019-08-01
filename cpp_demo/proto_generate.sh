#!/bin/bash
protoc --grpc_out protosource --cpp_out protosource --plugin=protoc-gen-grpc=$1 -I . demo.proto