#!/bin/bash

wget --output-document trans.tar.gz https://github.com/TransDecoder/TransDecoder/archive/refs/tags/TransDecoder-v5.5.0.tar.gz
tar -xzvf trans.tar.gz
sudo rm trans.tar.gz
echo 'export PATH=$PATH:$PWD/TransDecoder-TransDecoder-v5.5.0' >> ~/.bashrc