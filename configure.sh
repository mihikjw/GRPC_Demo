#!/bin/bash

# install requirements
brew install cmake
pip3 install -r requirements.txt

# configure python demo
cd python_demo
python3 proto_generator.py
cd ..

# configure cpp demo
cd cpp_demo
cmake .
cd ..