#Задача 2
import random

n = int(input("Задайте брой на цифри: "))

a = []
b = []

randoms = []
for i in range(n):
    #Вариант ако искаме да въвеждаме числата ръчно
    # a.append(int(input(F"Число за a[{i}]=")))

    #Вариант ако искаме да въвеждаме напълно случайни числа (n на брой)
    a.append(random.randrange(1,10))
    print(a[i])

#С много благодарности към бай Иван, че ми съкрати по-долната изгъзлица
for i in range(1, (n-1)*2, 2):
    a.insert(i, a[i] + a[i-1])

print(a)
# if n % 2 == 0:
#     for i in range(0, n):
#         if i % 2 == 0:
#             b.append(a[i])
#             k = a[i+1]
#             k += a[i]
#             b.append(k)
#         else:
#             b.append(a[i])
# else:
#     for i in range(0, n):
#         if i % 2 == 0:
#             if i != n-1:
#                 b.append(a[i])
#                 k = a[i+1]
#                 k += a[i]
#                 b.append(k)
#             else:
#                 d = a[i-1]
#                 p = d + a[i]
#                 b.append(p)
#                 b.append(a[i])
#         else:
#             b.append(a[i])
print(b)


# #Задача 3
# letters = input("")

# ltrs = {}
# for i in range(len(letters)):
#     if F"{letters[i]}" in ltrs:
#         r = ltrs.get(F"{letters[i]}")
#         ltrs.update({F"{letters[i]}": r + 1})
#     else:
#         ltrs.update({F"{letters[i]}": 1})

# ltrs_sorted = sorted(ltrs.items(), key=lambda x: x[0], reverse=False)

# for x,y in ltrs_sorted:
#     print(F"{x}:{y}", end=" ")



# #Задача 4

# n = (int(input("Въведете число: ")))
# a = []
# b = []
# for i in range(1, n+1):
#     a.append(i)
# print(a)

# for i in range(n, -1, -1):
#     if(i != 0):
#         b.append(i)
# print(b)

# ab = {}
# for i in range(n):
#     ab[a[i]] = b[i]

# print(ab)