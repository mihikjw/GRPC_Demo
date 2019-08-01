cmake_minimum_required(VERSION 3.7.2)
project(demo)

# setup cmake
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(_GRPC_CPP_PLUGIN_EXECUTABLE /usr/local/bin/grpc_cpp_plugin)
list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}/cmake")
list(APPEND CMAKE_PREFIX_PATH "/usr/local/lib")

# find packages
find_package(Protobuf REQUIRED)
find_package(gRPC REQUIRED)

# generate c++ protobufs
set(PROTO_SRC_DIR ${CMAKE_CURRENT_BINARY_DIR})
execute_process(
  COMMAND bash ./proto_generate.sh "${_GRPC_CPP_PLUGIN_EXECUTABLE}"
  OUTPUT_VARIABLE CPP_PROTO_GEN_OUT)

# add sources
file(GLOB SOURCES
    *.cpp
    protosource/*.cc
)

# add includes
include_directories(.)

# create executable and link
add_executable(demo ${SOURCES})
target_link_libraries(
  demo
  gRPC::grpc++_reflection
  protobuf::libprotobuf)