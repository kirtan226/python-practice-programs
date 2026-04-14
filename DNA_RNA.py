"""
Write a function to transcribe a DNA sequence to mRNA.

Replace each nucleotide in the DNA sequence with its corresponding mRNA nucleotide.
of DNA, adenine (A) pairs with uracil (U) in RNA, cytosine (C) pairs with guanine (G),
 guanine (G) pairs with cytosine (C), and thymine (T) pairs with adenine (A).

input:'ATGC'
output:"UACG"

Reason: of the given DNA sequence 'ATGC', 'A' is replaced by 'U', 'T' by 'A', 'G' by 'C',
and 'C' by 'G'. Hence, the transcribed mRNA sequence is 'UACG.

Input:TACG
Output:AUGC

Input:CGTA
Output:GCAU
"""

def transcribe_to_mrna(dna):
    convert = {'A': 'U','T': 'A','C': 'G','G': 'C'}
    new=''

    for i in dna:
        new+=convert[i]
    return new

    # new = ''
    # for i in range(len(dna)):
    #     if dna[i] == 'A':
    #         new += 'U'
    #     elif dna[i] == 'C':
    #         new += 'G'
    #     elif dna[i] == 'G':
    #         new += 'C'
    #     elif dna[i] == 'T':
    #         new += 'A'
    # return new
print(transcribe_to_mrna("TACG"))
