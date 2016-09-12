def ratio(x,y):
    "jjjjj"
    return x/y
def answertolife():
    ""
    return 42

def think():
    ""
    return ('fuck yeah!')

def comple_base(base):
    ""
    if base in 'Aa':
        return 'T'
    elif base in 'Tt':
        return 'A'
    elif base in 'Gg':
        return 'C'
    else:
        return 'G'

seq = 'ATCGCGGGCGTTTAGATGTAGT'

def comple_seq(seq):
    ""
    rev_comp=''
    for base in reversed(seq):
        rev_comp += comple_base(base)
    return rev_comp

def complement_base(base, material='DNA'):
    """Returns the Watson-Crick complement of a base."""

    if base == 'A' or base == 'a':
        if material == 'DNA':
            return 'T'
        elif material == 'RNA':
            return 'U'
    elif base == 'T' or base == 't' or base == 'U' or base == 'u':
        return 'A'
    elif base == 'G' or base == 'g':
        return 'C'
    else:
        return 'G'

def reverse_complement(seq, material='DNA'):
    """Compute reverse complement of a sequence."""

    # Initialize reverse complement
    rev_seq = ''

    # Loop through and populate list with reverse complement
    for base in reversed(seq):
        rev_seq += complement_base(base, material=material)

    return rev_seq


def add_three_numbers(a,b,c):
    ""
    return a+b+c
