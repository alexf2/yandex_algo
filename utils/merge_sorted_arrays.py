def merge_ordered_arrays(a1, a2):
    len1, len2 = len(a1), len(a2)

    if len1 == 0:
        return a2[:]
    if len2 == 0:
        return a1[:]

    res = [None] * (len1 + len2)
    i, i1, i2 = 0, 0, 0

    while i1 < len1 or i2 < len2:
        if i1 >= len1:
            # если правый массив длиннее
            res[i] = a2[i2]
            i2 += 1
        elif i2 >= len2:
            # если левый массив длиннее
            res[i] = a1[i1]
            i1 += 1
        else:
            # общая часть
            if a1[i1] < a2[i2]:
                res[i] = a1[i1]
                i1 += 1
            else:
                res[i] = a2[i2]
                i2 += 1

        i += 1

    return res
