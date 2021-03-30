#multiplicatoin using addition
def multi(a, b):
    p = 0
    if a>b:
        m = b
        n = a
    else:
        m = a
        n = b
    for i in range(0,m):
        p = p + n
    return p
def complex(a, b, c, d):
    p = ''
    x = multi(a ,c)
    y = multi(b ,d)
    w = multi(a ,d)
    z = multi(c ,b)
    x1 = x - y
    y1 = w + z
    p = str(x1) + ' + i' + str(y1)
    return p
def main():
    print(multi(10, 15))
    print(complex(12, 5, 3, 8))


main()
