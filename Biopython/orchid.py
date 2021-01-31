from Bio import SeqIO, Seq

from_file= SeqIO.parse("ls_orchid.fasta","fasta")
for seq in from_file:
    # print(len(seq))
    # print(seq.seq.count("GCAT"))
    print(seq.seq.transcribe())
    print(seq.seq.translate())