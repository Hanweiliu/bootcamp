
def complement_base(base):
    """Returns the Watson-Crick complement of a base."""

    if base == 'A' or base == 'a':
        return 'T'
    elif base == 'T' or base == 't':
        return 'A'
    elif base == 'G' or base == 'g':
        return 'C'
    else:
        return 'G'


def reverse_complement(seq):
    """Compute reverse complement of a sequence."""

    # Initialize reverse complement
    rev_seq = ''

    # Loop through and populate list with reverse complement
    for base in seq:
        rev_seq += complement_base(base)

    return rev_seq[::-1]
# 1.3b
def reverse_complement(seq):
    """Compute reverse complement of a sequence."""

    # Initialize rev_seq to a lowercase seq
    rev_seq = seq.lower()

    # Substitute bases
    rev_seq = rev_seq.replace('t', 'A')
    rev_seq = rev_seq.replace('a', 'T')
    rev_seq = rev_seq.replace('g', 'C')
    rev_seq = rev_seq.replace('c', 'G')

    return rev_seq[::-1]
# 1.4
def longest_common_substring(s1, s2):
    """Return one of the longest common substrings"""

    # Make sure s1 is the shorter
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    # Start with the entire sequence and shorten
    substr_len = len(s1)
    while substr_len > 0:
        # Try all substrings
        for i in range(len(s1) - substr_len + 1):
            if s1[i:i+substr_len] in s2:
                return s1[i:i+substr_len]

        substr_len -= 1

    # If we haven't returned, there is no common substring
    return ''
# 1.5 a
def parens_count(struc):
    """
    Ensures there are equal number of open and closed parentheses
    in structure.
    """
    return struc.count('(') == struc.count(')')

    print(parens_count('(((..(((...)).))))'))
    print(parens_count('(((..(((...)).)))'))
#1.5b
def dot_parens_to_bp(struc):
    """
    Convert a dot-parens structure to a list of base pairs.
    Return False if the structure is invalid.
    """

    if not parens_count(struc):
        print('Error in input structure.')
        return False

    # Initialize list of open parens and list of base pairs
    open_parens = []
    bps = []

    # Scan through string
    for i, x in enumerate(struc):
        if x == '(':
            open_parens.append(i)
        elif x == ')':
            if len(open_parens) > 0:
                bps.append((open_parens.pop(), i))
            else:
                print('Error in input structure.')
                return False

    # Return the result as a tuple
    return tuple(sorted(bps))
# 1.5 c
def hairpin_check(bps):
    """Check to make sure no hairpins are too short."""
    for bp in bps:
        if bp[1] - bp[0] < 4:
            print('A hairpin is too short.')
            return False

    # Everything checks out
    return True
# 1.5 d
def rna_ss_validator(seq, sec_struc, wobble=True):
    """Validate and RNA structure"""

    # Convert structure to base pairs
    bps = dot_parens_to_bp(sec_struc)

    # If this failed, the structure was invalid
    if not bps:
        return False

    # Do the hairpin check
    if not hairpin_check(bps):
        return False

    # Possible base pairs
    if wobble:
        ok_bps = ('gc', 'cg', 'au', 'ua', 'gu', 'ug')
    else:
        ok_bps = ('gc', 'cg', 'au', 'ua')

    # Check complementarity
    for bp in bps:
        bp_str = (seq[bp[0]] + seq[bp[1]]).lower()
        if bp_str not in ok_bps:
            print('Invalid base pair.')
            return False

    # Everything passed
    return True
    print('Should be True:')
    print(rna_ss_validator('GCAUCUAUGC', '(((....)))'))
    print(rna_ss_validator('GCAUCUAUGU', '(((....)))'))
    print(rna_ss_validator('GCAUCUAUGU', '(.(....).)'))

    print('\nShould be False:')
    print(rna_ss_validator('GCAUCUACGC', '(((....)))'), '\n')
    print(rna_ss_validator('GCAUCUAUGU', '(((....)))', wobble=False), '\n')
    print(rna_ss_validator('GCAUCUAUGU', '(.(....)).'), '\n')
    print(rna_ss_validator('GCCCUUGGCA', '(.((..))).'),'\n')
