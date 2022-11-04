def correct_var(*args, change=1):
    global universe
    universe = list(universe)
    idx = 0
    ans = 0
    for i in args:
        m = {}
        for j in i:
            if j not in m:
                m[j] = 1
            else:
                m[j] += 1
        cur = 0
        if change % 2 == 0:
            for j in i:
                if m[j] % 2 == 0:
                    cur += 1
        else:
            for j in i:
                if m[j] % 2 == 1:
                    cur += 1
        if cur != 0:
            universe[idx] = round(cur / len(i), 1)
            ans += 1
        idx += 1
    universe = tuple(universe)
    return ans
