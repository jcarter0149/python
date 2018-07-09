stockDict = {'GM': 'General Motors', 'CAT': 'Caterpillar', 'EK': 'Eastman Kodak'}

purchases = [ ('GM', 100, '10-sep-2001', 48),
    ('CAT', 100, '1-apr-1999', 24),
    ('EK', 200, '1-jul-1998', 56)]

for company, v in stockDict.items():
    if company == purchases[0][0]:
        print(v, purchases[0][1] * purchases[0][3], purchases[0][2])
    elif company == purchases[1][0]:
        print(v, purchases[1][1] * purchases[1][3], purchases[1][2])
    elif company == purchases[2][0]:
        print(v, purchases[2][1] * purchases[2][3], purchases[2][2])