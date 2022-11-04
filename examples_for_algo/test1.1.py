import sys
s = sys.stdin

for line in s:
    res = line.split()
    res = []
    f = int(res[0])
    if len(res[-1]) == 1:
        need = '0'
    else:
        need = res[-1][-2]
    for i in range(1, len(res) - 1):
        cur = res[i]
        if len(cur) > 1:
            if cur[-2] == need and int(cur) % f != 0:
                res.append(res[i])
    print('...'.join(res))

