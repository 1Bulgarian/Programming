def func(op, a, b):
    if op == "+":
        return(plus(a,b))
    elif op == "-":
        return(minus(a,b))
    elif op == "*":
        return(po(a,b))
    elif op == "/":
        return(div(a,b))
    else:
        print("Невалидна операция")
        return 0


def plus(a, b):
    S = a + b
    return S
def minus(a, b):
    S = a - b
    return S
def po(a, b):
    S = a * b
    return S
def div(a, b):
    S = a/b
    return S

x = input("Каква операция да бъде? [+, -, *, /]: ")
a = int(input("Числото а: "))
b = int(input("Числото b: "))

print(func(x, a, b))