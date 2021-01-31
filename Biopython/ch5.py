# formats: https://biopython.org/wiki/SeqIO
from Bio import SeqIO
# parse: gives iterator of SeqRecord objects
rec_it=SeqIO.parse("ls_orchid.fasta","fasta")
first=next(rec_it)
print(first)
print(first.id)
second=next(rec_it)
print(second)

recs=list(rec_it)
print(recs[-1])

all_species= [sq.annotations["organism"]
                for sq in SeqIO.parse("ls_orchid.gbk","genbank")]
print(all_species)
all_species= [sq.description.split()[1]
                for sq in SeqIO.parse("ls_orchid.fasta","fasta")]
print(all_species)

# total length
with open("ls_orchid.gbk") as handle:
    print(sum(len(r) for r in SeqIO.parse(handle,"gb")))

# for zipped files (gzip or bz2) ("rt" in both cases)
import gzip
with gzip.open("ls_orchid.gbk.gz","rt") as handle:
    print(sum(len(r) for r in SeqIO.parse(handle,"gb")))

# from the net from NCBI (fasta or gb)
from Bio import Entrez
Entrez.email = 'A.N.Other@example.com'
with Entrez.efetch(
    db="nucleotide", rettype="fasta", retmode="text", id="6273291"
    ) as handle:
    rec=SeqIO.read(handle,"fasta")
print(rec.id, len(rec.features))
# we can use parse

# parsing SwissProt from net
from Bio import ExPASy
with ExPASy.get_sprot_raw("O23729") as handle:
    rec=SeqIO.read(handle,"swiss")
print(rec)

# to_dict() is memory demanding
# index() read only dictionary
# index_db() better memory management (SQL3Lite database)

# 1. to_dict()
orchid_dict = SeqIO.to_dict(SeqIO.parse("ls_orchid.gbk", "genbank"))
print(len(orchid_dict))
# random keys
print(orchid_dict.keys())
print(orchid_dict["Z78512.1"].description)

# from fasta we can specify keys
orchid_dict = SeqIO.to_dict(SeqIO.parse("ls_orchid.fasta", "fasta"))
print(orchid_dict.keys())

def get_accession(record):
    parts = record.id.split("|")
    assert len(parts) == 5 and parts[0] == "gi" and parts[2] == "emb"
    return parts[3]

orchid_dict = SeqIO.to_dict(SeqIO.parse("ls_orchid.fasta", "fasta"), key_function=get_accession)
print(orchid_dict.keys())

# 2. Indexed file
orchid_dict = SeqIO.index("ls_orchid.gbk", "genbank")
print(orchid_dict)
orchid_dict.close()
# write rows to a file
orchid_dict = SeqIO.index("ls_orchid.gbk", "genbank")
with open("selected.dat","wb") as out: 
    for acc in ['Z78533.1','Z78445.1']:
        out.write(orchid_dict.get_raw(acc))

# 3. database