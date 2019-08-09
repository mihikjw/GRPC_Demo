# GRPC_Demo
A demo project for GRPC, containing a simple webpage hooked-up to gRPC endpoints in C++ and Python. Additional examples may be added in future releases.

# Requirements
Purely for running the example, you simply require Docker:
- Docker
    - Ubuntu Install: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04
    - Mac Install: https://docs.docker.com/docker-for-mac/install/

# Running The Example
- From the root of the repository, run 'docker-compose up -d' to start the services (note: the initial build may take some time)
- Navigate to 'http://localhost' to view the webpage (default port is 80, defined in docker-compose.yml)