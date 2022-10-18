import sys
s = sys.stdin

for line in s:
    a = line.split()
    res = []
    f = int(a[0])
    if len(a[-1]) == 1:
        need = '0'
    else:
        need = a[-1][-2]
    for i in range(1, len(a) - 1):
        cur = a[i]
        if len(cur) > 1:
            if cur[-2] == need and int(cur) % f != 0:
                res.append(a[i])
    print('...'.join(res))

