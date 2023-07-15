RNA_DICT = {"G": "C", "C": "G", "T": "A", "A": "U"}


def to_rna(dna_strand):
    if len(dna_strand) == 0:
        return ""
    return "".join([RNA_DICT[c] for c in dna_strand])
