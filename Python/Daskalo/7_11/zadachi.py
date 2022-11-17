#За да може кода, който искате да пуснете да работи, маркирайте го и натиснете Ctrl + K + U
#За да закоментирате код, маркирайте го и натиснете Ctrl + K + C

#Задача 6
# import random
# n = int(input("Моля въведете брой на случайни букви: "))

# #Цифрите [65-90] за буквите [А-Z] в ASCII, както [97-122] са [a-z]
# letters = ""

# #За да използваме и главните и малки букви, правим първо рандомайзър, който избира 1 или 2 и спрямо този отговор добавя главна или малка буква
# for i in range(n):
#     rand = random.randrange(0,2)
#     if rand == 1:
#         rand = random.randrange(65,90)
#         letters += chr(rand)
#     else:
#         rand = random.randrange(97,122)
#         letters += chr(rand)

# #Със set правим множество (колекция, в която няма повторения)
# #Проверяваме в тази колекция дали се съдържа буква, зададена от клавиатурата
# s = set(letters)
# print(letters)
# l = input("Въведете буква: ")[0]
# if l in s:
#     print(F"{l} се съдържа в стринга.")
# else:
#     print(F"{l} не се съдържа в стринга.")


# #Създаваме for цикъл, който проверява всяка една от буквите в рандомизирания стринг, като ги добавя в списък
# ltrs = {}
# for i in range(len(letters)):
#     if F"{letters[i]}" in ltrs:
#         r = ltrs.get(F"{letters[i]}")
#         ltrs.update({F"{letters[i]}": r + 1})
#     else:
#         ltrs.update({F"{letters[i]}": 1})

# for x,y in ltrs.items():
#     print(F"{x}: {y}")




#Задача 7

import random

dict = {
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
}
value = []

keys = dict.keys()
values = dict.values()

ran = random.randrange(10,15)
for (key, value) in dict.items():
    if value == ran:
        print(value)
        break
rans = []
for i in range(10):
    rar = random.randrange(0,15)
    rans.append(rar)

broqch = 0
for i in rans:
    for (key, value) in dict.items():
        if value == i:
            print(F"{broqch}: {i}: {key}")
            broqch +=1
            break



#Задача 8

# #[12,3,456,78]
# n = input("Въведете списък от числа: ")

# #Махаме [ ] ,
# n = n.replace('[', ' ')
# n = n.replace(']', ' ')
# n = n.replace(',', ' ')

# #Правим празен лист, и сплитваме тримнатия стринг на отделни елементи в листа.
# asd = []
# asd = n.split()
# print(asd)

# #Изпечатваме всичко на един ред, заедно
# for i in asd:
#     print(i, end="")