
condon_tuple = ('UAA','UGA','UAG')
condon = input('put condon here:')
if condon == 'AUG':
    print('this condon is the start condon.')
elif condon in condon_tuple:
    print('this is the stop condon.')
else:
    print('this is neither start nor stop condon.')
