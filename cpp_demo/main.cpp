#include "RPCServer.h"

#include <grpcpp/server.h>
#include <grpcpp/server_builder.h>
#include <grpcpp/security/server_credentials.h>

#include <memory>


int main(int argc, char* args[]) {
    std::unique_ptr<Server::RPCServer> service(new Server::RPCServer("0.0.0.0:1234"));

    if (service.get()) {
        grpc::ServerBuilder builder;
        builder.AddListeningPort(service->GetAddress(), grpc::InsecureServerCredentials()); 
        builder.RegisterService(service.get());
        std::unique_ptr<grpc::Server> server(builder.BuildAndStart());

        if (server.get()) {
            server->Wait();
        }
    }
}