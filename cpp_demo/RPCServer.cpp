#include "RPCServer.h"

using namespace Server;

RPCServer::RPCServer(const std::string &address) {
    if (address.length()) {
        fAddress = address;
    }
}

RPCServer::~RPCServer() {}

grpc::Status RPCServer::GetIdentity(grpc::ServerContext* context, const demo::Identity* inputData, demo::Identity* resultData) {
    resultData->set_name("Jeremy Soultrain");
    resultData->set_location("C++ Endpoint");
    return grpc::Status::OK;
}

std::string RPCServer::GetAddress() {
    return fAddress;
}