import math


def grad(egn):
    grad = egn[6:9]
    grad = int(grad)

    if grad <= 139: return "Варна"
    elif grad >= 140 and grad <= 169: return "Велико Търново"
    elif grad >= 170 and grad <= 183: return "Видин"
    elif grad >= 184 and grad <= 217: return "Враца"
    elif grad >= 218 and grad <= 233: return "Габрово"
    elif grad >= 234 and grad <= 281: return "Кърджали"
    elif grad >= 282 and grad <= 301: return "Кюстендил"
    elif grad >= 302 and grad <= 319: return "Ловеч"
    elif grad >= 320 and grad <= 341: return "Монтана"
    elif grad >= 342 and grad <= 377: return "Пазарджик"
    elif grad >= 378 and grad <= 395: return "Перник"
    elif grad >= 396 and grad <= 435: return "Плевен"
    elif grad >= 436 and grad <= 501: return "Пловдив"
    elif grad >= 502 and grad <= 527: return "Разград"
    elif grad >= 528 and grad <= 555: return "Русе"
    elif grad >= 556 and grad <= 575: return "Силистра"
    elif grad >= 576 and grad <= 601: return "Сливен"
    elif grad >= 602 and grad <= 623: return "Смолян"
    elif grad >= 624 and grad <= 721: return "София - град"
    elif grad >= 722 and grad <= 751: return "София - окръг"
    elif grad >= 752 and grad <= 789: return "Стара Загора"
    elif grad >= 790 and grad <= 821: return "Добрич"
    elif grad >= 822 and grad <= 843: return "Търговище"
    elif grad >= 844 and grad <= 871: return "Хасково"
    elif grad >= 872 and grad <= 903: return "Шумен"
    elif grad >= 904 and grad <= 925: return "Ямбол"
    else: return "Друг/Неизвестен"

def birthdate(egn):
    birth = egn[:6]
    den = birth[4:6]
    mesec = birth[2:4]
    godina = birth[:2]

    gd = int(mesec[:1])

    #Роден 21-ви век, проверява месеца дали е преди или след октомври
    if gd == 4:
        return (f"{den}/0{mesec[1:]}/20{godina}")
    elif gd == 5:
        return (f"{den}/1{mesec[1:]}/20{godina}")


    #Роден 20-и век
    elif gd == 0:
        return (f"{den}/0{mesec[1:]}/19{godina}")
    elif gd == 1:
        return (f"{den}/1{mesec[1:]}/19{godina}")


    #Роден 19-и век, проверява месеца дали е преди или след октомври
    elif gd == 2:
        return (f"{den}/0{mesec[1:]}/18{godina}")
    elif gd == 3:
        return (f"{den}/1{mesec[1:]}/18{godina}")

    else: 
        return 0

def kontrolna(egn):
    c = []
    for i in egn:
        c.append(int(i))
    ctrl = float(c[0]*2 + c[1]*4 + c[2]*8 + c[3]*5 + c[4]*10 + c[5]*9 + c[6]*7 + c[7]*3 + c[8]*6)
    x = math.floor(ctrl / 11)
    ct = ctrl - x*11
    if(ct == c[9]):
        return 1
    else:
        return 0

def EGN_Checker(egn):
    if len(egn) == 10:
        bd = birthdate(egn)
        c = kontrolna(egn)
        g = grad(egn)

        if bd != 0:
            if c != 0:
                return (F"Рожденна дата {bd}, Роден в {g}, с валидна контролна цифра")
            else:
                return "ЕГН-то е невалидно"
        else:
            return "ЕГН-то е невалидно"

    else:
        return "ЕГН-то е невалидно"



#0344306447
text = input("Моля въведете ЕГН: ")
print(EGN_Checker(text))