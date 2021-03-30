#searching for a number in fibonacci series
def search(x):
    if x == 0:
        return True
    else:
        c = 0
        a = 0
        b = 1
        while x > c:
            c = a + b
            if x == c:
                return True
            else:
                a = b
                b = c
        return False

def main():
    x = int(input("please enter your number:\n"))
    p = search(x)
    if p == 1:
        print("your number is in fibonacci sequence")
    else:
        print("your number is not in fibonacci sequence")

main()
