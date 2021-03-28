#!/bin/bash

wget --output-document sratoolkit.tar.gz https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/2.11.0/sratoolkit.2.11.0-ubuntu64.tar.gz
sudo rm sratoolkit.tar.gz
echo 'export PATH=$PATH:$PWD/sratoolkit.2.11.0-ubuntu64/bin' >> ~/.bashrc
source ~/.bashrc
vdb-config -i