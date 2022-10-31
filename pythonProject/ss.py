#age=int(input("Сколько вы хотели бы прожить: "))
#age2=int(input("На сколько себя чувстуете: "))
#form=(age*age2)//100
#print("Ваш психологический возраст: ",form)

data=int(input("Введите число "))
month=int(input("Введите месяц рождения "))
if (data>=21 and data<=31 and month==3)or(data>=1 and data<=19 and month==4):
    print("Ваш знак зодиака: Овен")
elif (data>=20 and data<=30 and month==4)or(month==5 and data>=1 and data<=20):
    print("Ваш знак зодиака: Телец")
elif (data>=21 and data<=31 and month==5)or(month==6 and data>=1 and data<=21):
    print("Ваш знак зодиака: Близнецы")
elif (data>=22 and data<=30 and month==6)or(month==7 and data>=1 and data<=22):
    print("Ваш знак зодиака: Рак")
elif (data>=23 and data<=31 and month==7)or(month==8 and data>=1 and data<=22):
    print("Ваш знак зодиака: Лев")
elif (data>=23 and data<=31 and month==8)or(month==9 and data>=1 and data<=20):
    print("Ваш знак зодиака: Дева")
elif (data>=23 and data<=30 and month==9)or(month==10 and data>=1 and data<=23):
    print("Ваш знак зодиака: Весы")
elif (data>=24 and data<=31 and month==10)or(month==11 and data>=1 and data<=22):
    print("Ваш знак зодиака: Cкорпион")
elif (data>=23 and data<=30 and month==11)or(month==12 and data>=1 and data<=21):
    print("Ваш знак зодиака: Cтрелец")
elif (data>=22 and data<=31 and month==12)or(month==1 and data>=1 and data<=20):
    print("Ваш знак зодиака: Козерог")
elif (data>=21 and data<=31 and month==2)or(month==3 and data>=1 and data<=18):
    print("Ваш знак зодиака: Водолей")
elif (data>=19 and data<=28 and month==3)or(month==4 and data>=1 and data<=20):
    print("Ваш знак зодиака: Рыбы")