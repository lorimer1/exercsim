PROTEIN_LOOKUP = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "STOP",
    "UAG": "STOP",
    "UGA": "STOP",
}


def proteins(strand: str):
    codons = [strand[index : index + 3] for index in range(0, len(strand), 3)]

    result: list = []
    for codon in codons:
        protein = PROTEIN_LOOKUP[codon]
        if protein == "STOP":
            break
        result.append(protein)
    return result
