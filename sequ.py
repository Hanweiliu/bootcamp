seq = 'AGCUGCUGCAGCUUUUGCCCAUG'
start_condon = 'AUG'
for i, _ in enumerate(seq):
    if seq[i:i+3] == start_condon:
        print('the start condon start at:',i)
        break
else:
    print('start condon not in sequence.')
