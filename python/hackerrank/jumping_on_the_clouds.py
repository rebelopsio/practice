def jumpingOnClouds(c):
    i = 0
    j = 0
    while i < len(c) - 2:
        if c[i+2]:
            i = i + 1
            j += 1
        else:
            i = i + 2
            j += 1
    if i < len(c) - 1:
        j += 1
    return j
