#12321
#12321

def palindrom(chislo):
    a = []
    b = []
    for i in chislo:
        a.append(i)
    a.reverse()

    for i in a:
        b.append(i)
    a.reverse()

    for i in range(len(a)):
        if a[i] != b[i]:
            return 0
    return 1

n = input("Въведете число: ")
print(palindrom(n))