from Bio.Seq import Seq

my_seq=Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
for index, letter in enumerate(my_seq):
    print("%i %s" % (index, letter))

# length
print(len(my_seq))
# first element
print(my_seq[22])
#last element
print(my_seq[-1])

print(my_seq.count("GC"))

from Bio.SeqUtils import GC
print(GC(my_seq))

#slicing
print(my_seq[1:4])
# starting from 0 with step 3
print(my_seq[1::2])
print(my_seq[1:6:2])
#reverse
print(my_seq[::-1])
print(my_seq[22:35])

my_seq2=Seq("EVRNAK")
print(my_seq+my_seq2)
print(my_seq2+my_seq)

list_of_seqs = [Seq("ACGT"), Seq("AACC"), Seq("GGTT")]
res=Seq("NnN").join(list_of_seqs)
print(res)

print(res.upper())
# print(res.lower())

#find
print("CG" in res)

print(my_seq)
#complement
print(my_seq.complement())
# reverse complement
print(my_seq.reverse_complement())

#Transcription
coding_dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
template_dna = coding_dna.reverse_complement()
print(template_dna)
messenger_rna = coding_dna.transcribe()
print(messenger_rna)
print(messenger_rna.back_transcribe())
print(messenger_rna.translate())
print(coding_dna.translate())

# NCBI table number or name
print(coding_dna.translate(table="Vertebrate Mitochondrial"))
print(coding_dna.translate(table=2, stop_symbol="@"))
print(coding_dna.translate(to_stop=True))

from Bio.Data import CodonTable
standard_table = CodonTable.unambiguous_dna_by_name["Standard"]
mito_table = CodonTable.unambiguous_dna_by_name["Vertebrate Mitochondrial"]
print(mito_table)
print(mito_table.stop_codons)
print(mito_table.start_codons)
print(mito_table.forward_table["ACG"])

my_seq[1]="N"

mutable_seq=my_seq.tomutable()
# or
from Bio.Seq import MutableSeq
mutable_seq = MutableSeq('GCCATTGTAATGGGCCGCTGAAAGGGTGCCCGA')

mutable_seq[5]="A"
print(mutable_seq)
del mutable_seq[4]
mutable_seq.remove('A')
print(mutable_seq)
new_seq=mutable_seq.toseq()
print(new_seq)

from Bio.Seq import UnknownSeq
unk=UnknownSeq(10)
print(unk)
unk=UnknownSeq(10,character="A")
print(unk)
unk_protein = unk.translate()
print(unk_protein)
