"""
MyPackage - A simple package for loading FASTA files.
"""

__version__ = '0.1.0'


def load_fasta(filename):
    sequences = {}
    with open(filename, 'r') as file:
        current_id = None
        current_seq = []
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if current_id is not None:
                    sequences[current_id] = ''.join(current_seq)
                current_id = line[1:]  # Remove '>'
                current_seq = []
            else:
                current_seq.append(line)
        if current_id is not None:
            sequences[current_id] = ''.join(current_seq)
    return sequences