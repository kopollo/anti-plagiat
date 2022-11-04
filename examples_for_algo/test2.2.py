def correct_var(*args, change=1):
    global res
    res = list(res)
    kx = 0
    ans = 0
    for i in args:
        sl = {}
        for j in i:
            if j not in sl:
                sl[j] = 1
            else:
                sl[j] += 1
        cur = 0
        if change % 2 == 0:
            for j in i:
                if sl[j] % 2 == 0:
                    cur += 1
        else:
            for j in i:
                if sl[j] % 2 == 1:
                    cur += 1
        if cur != 0:
            res[kx] = round(cur / len(i), 1)
            ans += 1
        kx += 1
    res = tuple(res)
    return ans

