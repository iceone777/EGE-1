for w in range(2):
    for x in range(2):
        for z in range(2):
            for y in range(2):
                f = not(((((w and x) == x) or True) <= z) or (not(x)) and y)
                if f == 0:
                    print(w, z, x, y, '|', f * 1)