def f(x):
    S = 0
    if x == "1":
        a = int(input("Страната а: "))
        S = a * a
    elif x == "2":
        a = int(input("Страната а: "))
        b = int(input("Страната b: "))
        S = a * b
    elif x == "3":
        a = int(input("Страната а: "))
        b = int(input("Страната b: "))
        S = float(a*b/2)
    else: 
        print("Невалидна стойност.")
        return

    return (F"Лицето на фигурата е: {S}")
    

k = input("Напишете 1 за квадрат, 2 за правоъгълник или 3 за правоъгълен триъгълник: ")
print(f(k))