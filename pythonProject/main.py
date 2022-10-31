import telebot
from telebot import types

bot = telebot.TeleBot("5722986130:AAFxW3XjZUflZYfG1m0c9DaRXi_sXBQWHIs")
age = 0
age2 = 0
data=0
mounth=0



@bot.message_handler(commands=["start"])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('🌏 Узнать знак зодиака')
    keyboard.row("👁 Узнать психологический возраст")
    bot.send_message(message.chat.id, 'Добро пожаловать', reply_markup=keyboard)



@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "👁 Узнать психологический возраст" or message.text=="Узнать психологический возраст" or message.text=="узнать психологический возраст":
        bot.send_message(message.from_user.id,"Слышали ли вы фразу: «Я молод/молода душой»? Я уверена, что хоть раз, да слышали. Приходилось ли вам задумываться, о чем это? Да-да, это как раз о том, что внутреннее самоощущение своего возраста человеком не совпадает с тем, что написано у него в паспорте. Возможно, и вы сами замечали за собой такое. Речь как раз и идет о психологическом возрасте, который очень часто отличается от возраста фактического, физиологического.")
        bot.send_message(message.from_user.id,"Психологический возраст – это субъективное внутреннее ощущение своего возраста самим человеком. При этом психологический возраст, конечно же, влияет на мысли, чувства, стиль поведения человека, и в конечном счете, на весь его образ жизни.")
        bot.send_message(message.from_user.id, "Шаг 1: определяемся с тем, сколько вы хотели бы прожить. Конечно же, не все в наших руках, но у каждого из нас есть определенные представления о желаемом количестве лет жизни.")
        bot.send_message(message.from_user.id,"Сколько вы хотели бы прожить?🕰\n\nВ ответе запишите число без лишних символов.Например: 30")
        bot.register_next_step_handler(message, age_func)
    if message.text=="🌏 Узнать знак зодиака" or message.text=="Узнать знак зодиака" or message.text=="знак зодиака":
        bot.send_message(message.from_user.id,"Знаки зодиака — это 12 расположенных вдоль эклиптики (круга, по которому Солнце проходит видимый с Земли путь в течение года) созвездий. В астрологии считается, что каждый человек относится к тому или иному знаку в соответствии с датой своего рождения. Эти данные используются для составления гороскопов.")
        bot.send_message(message.from_user.id,"Знак зодиака зависит от дня рождения человека. Европейский астрологический круг начинается с Овна в марте.")
        bot.send_message(message.from_user.id,"Введите день вашего рождения\nНапример 15")
        bot.register_next_step_handler(message,func_zodiac)
def age_func(message):
    global age
    age = int(message.text)
    bot.send_message(message.from_user.id,"Шаг 2: определяем в процентом соотношении, насколько, по вашему мнению, вы реализовались в жизни на сегодняшний день, т.е. в том числе реализовали свои мечты, желания и намеченные планы на жизнь. Здесь нет каких-то точных показателей реализованности/нереализованности. Все опять же упирается в ваше субъективное мнение, самоощущение.")
    bot.send_message(message.from_user.id, "На сколько вы реализованы?📈\n\nВ ответе запишите число без лишних символов.Например: 30")
    bot.register_next_step_handler(message, func)
def func(message):
    global age2
    age2 = int(message.text)
    for i in range(1, 4):
        bot.send_message(message.from_user.id, "Идет подсчет...✨")
    formula = (age * age2) // 100
    bot.reply_to(message, "Ваш психологический возраст: " + str(formula))
    bot.send_message(message.from_user.id, "Чтобы перейти обратно в меню напишите /start")
def func_zodiac(message):
    global data
    data=int(message.text)
    bot.send_message(message.from_user.id,"Введите месяц ващего рождения \nНапример 6")
    bot.register_next_step_handler(message,examination)
def examination(message):
    global mounth
    mounth=int(message.text)
    if (data >= 21 and data <= 31 and mounth == 3) or (data >= 1 and data <= 19 and mounth == 4):
        bot.send_message(message.from_user.id,"Ваш знак зодиака: Овен")
    elif (data >= 20 and data <= 30 and mounth == 4) or (mounth == 5 and data >= 1 and data <= 20):
        bot.send_message(message.from_user.id, "Ваш знак зодиака: Телец")
    elif (data >= 21 and data <= 31 and mounth == 5) or (mounth == 6 and data >= 1 and data <= 21):
        bot.send_message(message.from_user.id, "Ваш знак зодиака: Близнецы")
    elif (data >= 22 and data <= 30 and mounth == 6) or (mounth == 7 and data >= 1 and data <= 22):
        bot.send_message(message.from_user.id, "Ваш знак зодиака: Рак")
    elif (data >= 23 and data <= 31 and mounth == 7) or (mounth == 8 and data >= 1 and data <= 22):
        bot.send_message(message.from_user.id, "Ваш знак зодиака: Лев")
    elif (data >= 23 and data <= 31 and mounth == 8) or (mounth == 9 and data >= 1 and data <= 20):
        bot.send_message(message.from_user.id, "Ваш знак зодиака: Дева")
    elif (data >= 23 and data <= 30 and mounth == 9) or (mounth == 10 and data >= 1 and data <= 23):
        bot.send_message(message.from_user.id, "Ваш знак зодиака: Весы")
    elif (data >= 24 and data <= 31 and mounth == 10) or (mounth == 11 and data >= 1 and data <= 22):
        bot.send_message(message.from_user.id, "Ваш знак зодиака: Скорпион")
    elif (data >= 23 and data <= 30 and mounth == 11) or (mounth == 12 and data >= 1 and data <= 21):
        bot.send_message(message.from_user.id, "Ваш знак зодиака: Стрелец")
    elif (data >= 22 and data <= 31 and mounth == 12) or (mounth == 1 and data >= 1 and data <= 20):
        bot.send_message(message.from_user.id, "Ваш знак зодиака: Козерог")
    elif (data >= 21 and data <= 31 and mounth == 2) or (mounth == 3 and data >= 1 and data <= 18):
        bot.send_message(message.from_user.id, "Ваш знак зодиака: Водолей")

    elif (data >= 19 and data <= 28 and mounth == 3) or (mounth == 4 and data >= 1 and data <= 20):
        bot.send_message(message.from_user.id, "Ваш знак зодиака: Рыбы")
    bot.send_message(message.from_user.id, "Чтобы перейти обратно в меню напишите /start")

bot.infinity_polling()
