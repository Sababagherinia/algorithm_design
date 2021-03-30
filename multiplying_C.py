#multiplying using method C
def M_C(a, b, m, n):
    p = 0
    a = a * 10**m
    b = b * 10**n
    m = m + n
    m = 10**m
    if a>b:
        mul = a
        div = b
    else:
        mul = b
        div = a
    if div == 1:
        p = mul
        return p/m
    else:
        while div >= 1:
            if div%2 != 0:
                p = mul + p
            div = div/2
            mul = mul * 2
        return p/m

def main():
    x = input("please enter your numbers plus the length of your decimal parts:(press enter after you write all the arguments)\n")
    y = x.split()
    p = M_C(float(y[0]),float(y[1]),int(y[2]),int(y[3]))
    print(p)

main()
