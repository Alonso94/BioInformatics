#!/bin/bash

${TRINITY_HOME}/Trinity --seqType fq --max_memory 2G \
              --single SRRxxxx.fastq \
              --SS_lib_type F --no_normalize_reads