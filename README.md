# dinuclCount

dinuclCount.py


A script that finds the total count of all the
dinucleotides for all the species and the count of each dinucleotide for each species for all fasta
files in a directory. If you have to following fasta files:
Fasta1.fa
>Arenirhops plectocarpus
ATACATATTGCGTTTTTTTGTCTTTTTATCCGCCCCCTTGGGGGGGA
Fasta2.fa
>Arenirhops plectocarpus
GGGATACATATTGCGTTGGGGGTTTTTGTCTTTTTATGGGGGCTTAGGG
>Helicophytum noctramus
CGAGCGCCGGGGTTGAATAACGTAGGGGGGGGGCTCGGGGATCTCTATACATTCTCGACAATCTATCGAG
CGCATCGTAATAGCCTCCAA
The output would be:
Arenirhops plectocarpus
Dinucleotide AA Count 0
Dinucleotide AC Count 1
Dinucleotide AG Count 0
Dinucleotide AT Count 4
Dinucleotide CA Count 1
Dinucleotide CC Count 5
Dinucleotide CG Count 2
Dinucleotide CT Count 2
Dinucleotide GA Count 1
Dinucleotide GC Count 2
Dinucleotide GG Count 6
Dinucleotide GT Count 2
Dinucleotide TA Count 3
Dinucleotide TC Count 2
Dinucleotide TG Count 3
Dinucleotide TT Count 12
Arenirhops plectocarpusDinucleotide AA Count 0
Dinucleotide AC Count 1
Dinucleotide AG Count 1
Dinucleotide AT Count 4
Dinucleotide CA Count 1
Dinucleotide CC Count 0
Dinucleotide CG Count 1
Dinucleotide CT Count 2
Dinucleotide GA Count 1
Dinucleotide GC Count 2
Dinucleotide GG Count 12
Dinucleotide GT Count 3
Dinucleotide TA Count 4
Dinucleotide TC Count 1
Dinucleotide TG Count 4
Dinucleotide TT Count 11
Helicophytum noctramus
Dinucleotide AA Count 5
Dinucleotide AC Count 3
Dinucleotide AG Count 4
Dinucleotide AT Count 8
Dinucleotide CA Count 4
Dinucleotide CC Count 3
Dinucleotide CG Count 9
Dinucleotide CT Count 6
Dinucleotide GA Count 5
Dinucleotide GC Count 6
Dinucleotide GG Count 14
Dinucleotide GT Count 3
Dinucleotide TA Count 7
Dinucleotide TC Count 9
Dinucleotide TG Count 1
Dinucleotide TT Count 2
Total dinucleotide counts
Dinucleotide AA Count 5
Dinucleotide AC Count 5
Dinucleotide AG Count 5
Dinucleotide AT Count 16
Dinucleotide CA Count 6
Dinucleotide CC Count 8
Dinucleotide CG Count 12Dinucleotide CT Count 10
Dinucleotide GA Count 7
Dinucleotide GC Count 10
Dinucleotide GG Count 32
Dinucleotide GT Count 8
Dinucleotide TA Count 14
Dinucleotide TC Count 12
Dinucleotide TG Count 8
Dinucleotide TT Count 25

The script takes in one argument which is a directory.

GChain.py

A script that will find all non-overlapping three nucleotides
leading and tailing a G chain (which is a sequence of three or more Gs). If there isn’t three
nucleotide leading or tailing the chain, it will print out as many as there are (which can be
zero, if so print of ‘NONE’). Using the same fasta files, the module’s output should be
Arenirhops plectocarpus
Lead = CTT Tail = A
Cryptosisymbrium exubercaulis
Lead = NONE Tail = ATA
Lead = GTT Tail = TTT
Lead = TAT Tail = CTT
Lead = A Tail = NONE
Helicophytum noctramus
Lead = GCC Tail = TTG
Lead = GTA Tail = CTC
Lead = NONE Tail = ATC
The script takes in one argument which is a
directory.
