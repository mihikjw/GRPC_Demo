#ifndef RPC_SERVER_H_
#define RPC_SERVER_H_

#include <string>
#include <grpc/grpc.h>
#include "protosource/demo.grpc.pb.h"

namespace Server {

class RPCServer final: public demo::Demo::Service {
    public:
        RPCServer(const std::string &address);
        ~RPCServer();
        grpc::Status GetIdentity(grpc::ServerContext* context, const demo::Identity* inputData, demo::Identity* resultData) override;
        std::string GetAddress();
    private:
        std::string fAddress;
};

};

#endif  //RPC_SERVER_H_