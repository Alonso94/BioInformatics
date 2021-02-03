#!/bin/bash

git clone https://github.com/trinityrnaseq/trinityrnaseq.git
cd trinityrnaseq
git checkout tags/v2.11.0
git submodule update --init --recursive
make
make plugins
make install
sudo apt install -y samtools jellyfish bowtie2 salmon
echo 'export TRINITY_HOME=/usr/local/bin/trinityrnaseq' >> ~/.bashrc
echo 'alias Trinity=$TRINITY_HOME/Trinity' >> ~/.bashrc