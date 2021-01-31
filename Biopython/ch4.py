# For working with simple data like FASTA we can skip this chapter
# This needed for richly annonated sequence data (e.g. GenBank, EMBL)
# SeqRecord allows higher level features (e.g. identifiers and features)
#   to be associated with a sequence
# class attributes: seq, id, name, description, letter_annotations, 
#                   annotations (dictionary), features, dbxrefs (database cross-references) 
from Bio.SeqRecord import SeqRecord

# creating a sequence (usually we read it from a file)
from Bio.Seq import Seq
seq=Seq("GATC")
seq_r=SeqRecord(seq)
print(seq_r.id)
seq_r.id="A2323A"
print("ID:",seq_r.id)
seq_r.description="Our sequence"
print("Descrition:",seq_r.description)
print("Seq:", seq_r.seq)

# annotations (dictionary) and letter_annotation
seq_r.annotations={"Creator":"A"}
print(seq_r.annotations["Creator"])
seq_r.annotations["evidence"]="None"
print(seq_r.annotations)
print(seq_r.annotations["evidence"])
seq_r.letter_annotations["phred"]=[40,40,38,30]
print(seq_r.letter_annotations)

from Bio import SeqIO
# from FASTA file
rec=SeqIO.read("NC_005816.fna","fasta")
print(rec)
print('-'*20)
# from GenBank file
rec=SeqIO.read("NC_005816.gb","genbank")
print(rec.dbxrefs)
print(len(rec.features))

# SeqFeature : describes a region on a parent sequence (typically SeqRecord)
#       the region is described with a location of object (typically range between two positions)
# SeqFeature attributes : type (e.g. 'CDS', 'gene), 
#                         location (includes ref, ref_db and strand),
#                         qualifiers (add. info.), sub_features (joins,later -> CompoundLocation)
# position : single position 5,10 (may be fuzzy <100, >200 e.g)
# location : region bounded by positions 5..20
# fuzzy position classes:
#       ExactPosition (5), BeforePosition (<5), AfterPosition (>5)
#       WithinPosition ((1.5)), OnOfPosition, UnknownPosition (?) 

from Bio import SeqFeature
start_pos=SeqFeature.AfterPosition(5)
end_pos=SeqFeature.BetweenPosition(position= 9, left=8, right=9)
loc=SeqFeature.FeatureLocation(start_pos, end_pos)
print(loc)
print(int(loc.start))
print(int(loc.end))

# iterating over features and finding out a location
from Bio import SeqIO
snp=4350
rec=SeqIO.read("NC_005816.gb","genbank")
for feature in rec.features:
    if snp in feature:
        print(feature.type, feature.qualifiers.get("db_xref"))

# SeqFeatures doesn't contain a sequence (it has a parent sequence)
from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature, FeatureLocation
seq=Seq("ACCGAGACGGCAAAGGCTAGCATAGGTATGAGACTTCCTTCCTGCCAGTGCTGAGGAACTGGGAGCCTAC")
feature=SeqFeature(FeatureLocation(5,18),type="gene",strand=-1)
# method 1
feature_seq=seq[feature.location.start : feature.location.end]
feature_seq=feature_seq.reverse_complement()
print(feature_seq)
# method 2
feature_seq=feature.extract(seq)
print(feature_seq)

# we can't compare SeqRecords, but we can compare their attributes

# References for citation in SeqFeature.References

# format the SeqRecord to fiel format e.g. FASTA
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
rec= SeqRecord(
    Seq(
        "MMYQQGCFAGGTVLRLAKDLAENNRGARVLVVCSEITAVTFRGPSETHLDSMVGQALFGD"
        "GAGAVIVGSDPDLSVERPLYELVWTGATLLPDSEGAIDGHLREVGLTFHLLKDVPGLISK"
        "NIEKSLKEAFTPLGISDWNSTFWIAHPGGPAILDQVEAKLGLKEEKMRATREVLSEYGNM"
        "SSAC"
    ), id="gi|14150838|gb|AAK54648.1|AF376133_1",
    description="chalcone synthase [Cucumis sativus]"
)
print(rec.format("fasta"))

# # Slicing
from Bio import SeqIO
rec=SeqIO.read("NC_005816.gb","genbank")
# the length of the sequence
print(len(rec))
print(len(rec.features))
print(rec.features[20])
sub_rec=rec[4300:4800]
print(sub_rec)
print(len(sub_rec))
print(len(sub_rec.features))
sub_rec.descrition="Yersinia pestis biovar Microtus str. 91001 plasmid pPCP1,partial."
sub_rec.annotations["molecule_type"]="DNA"
print(sub_rec.format("genbank"))

# we can add two sequences
left=rec[:10]
right=rec[30:]
new=left+right
new.annotations=rec.annotations.copy()
print(new)
# reverce complement
print(new.reverse_complement(id="Testing"))