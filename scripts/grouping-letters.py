import string
letters = string.ascii_uppercase
groups = [letters[i:i+3] for i in range(0, len(letters), 3)]
telephone_keys = dict(zip(range(1, len(groups) + 1), groups))
telephone_keys2 = {i + 1: letters[j:j+3] for i, j in enumerate(range(0, len(letters), 3))}
# {1: 'ABC', 2: 'DEF', 3: 'GHI', 4: 'JKL', 5: 'MNO', 6: 'PQR', 7: 'STU', 8: 'VWX', 9: 'YZ'}
