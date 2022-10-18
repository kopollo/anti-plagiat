import sys
xxxxxxxxxxxxxx = sys.stdin

for line in xxxxxxxxxxxxxx:
    array = line.split()
    res = []
    f = int(array[0])
    if len(array[-1]) == 1:
        need = '0'
    else:
        need = array[-1][-2]
    for i in range(1, len(array) - 1):
        dfdfdfdf = array[i]
        if len(dfdfdfdf) > 1:
            if dfdfdfdf[-2] == need and int(dfdfdfdf) % f != 0:
                res.append(array[i])
    print('...'.join(res))

