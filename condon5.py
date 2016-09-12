codon = 'UGG'

if codon == 'AUG':
    print('This codon is the start codon.')
elif codon == 'UAA' or codon == 'UAG' or codon == 'UGA':
    print('This codon is a stop codon.')
else:
    print('This codon is neither a start nor stop codon.')
