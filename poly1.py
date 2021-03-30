#polynomial algorithm 1
def poly_1(a ,x):
    sum1 = a[0]
    for i in range(1,len(a)):
        sum1 = sum1 + (a[i]*(x**i))
    return sum1

a = []
n = int(input("tedad jomalat ra vared konid: "))
for i in range(0,n):
    k = int(input("sabete "+str(i)+"om ra vared konid: "))
    a.append(k)
x = int(input("motaghayere khod ra vared konid: "))

print(poly_1(a ,x))
