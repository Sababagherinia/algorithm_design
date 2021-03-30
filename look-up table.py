#multiplication by look-up table
def lookup(a, b):
    table = [1,2,4,3,6,9,4,8,12,16,5,10,15,20,25,6,12,18,24,30,36,7,14,21,28,35,42,49,8,16,24,32,40,48,56,64,9,18,27,36,45,54,63,72,81]
    if a>b:
        g = a
        l = b
    else:
        g = b
        l = a
    t = str(g)
    n = len(t)
    if n == 1:
        i = int(g*(g-1)/2+l)
        return table[i-1]
    else:
        m = int(n/2)
        x = int(g/(10**m))
        y = g%(10**m)
        w = int(l/(10**m))
        z = l%(10**m)
        r = lookup(x+y, w+z)
        p = lookup(x, w)
        q = lookup(y, z)
        return p*(10**(2*m))+(r - p - q)*(10**m)+q


print(lookup(34,66))

