for n in range(3, 10000 + 1):
    stroka = '0' + '5' * n
    while '55' in stroka or '150' in stroka or '555' in stroka:
        if '55' in stroka:
            stroka = stroka.replace('55', '165', 1)
        elif '150' in stroka:
            stroka = stroka.replace('150', '5090', 1)
        elif '555' in stroka:
            stroka = stroka.replace('555', '50', 1)

#for digit in stroka:
    #if ... and digit % 2 != 0:

#if result > 100000:
#   print(n)
