#!/bin/bash
sudo apt install -y cmake samtools jellyfish bowtie2 salmon libzma-dev autoconf libproxy-dev libz-dev
git clone https://github.com/trinityrnaseq/trinityrnaseq.git
cd trinityrnaseq
git checkout tags/v2.11.0
git submodule update --init --recursive
make
make plugins
make install
echo 'export TRINITY_HOME=/usr/local/bin/trinityrnaseq' >> ~/.bashrc
echo 'alias Trinity=$TRINITY_HOME/Trinity' >> ~/.bashrc
