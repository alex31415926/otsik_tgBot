# encoding: utf8
#author Alexander Shapovalov avasplit@gmail.com
import telebot
from telebot import types
import logging
import time
import datetime
import config

bot = telebot.TeleBot(config.token)

#logger = telebot.logger
#telebot.logger.basicConfig(filename='filename.log', level=logging.DEBUG,
#                    format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.basicConfig(format='%(asctime)s - %(levelname)s - %(messsage)s',
#                    level=logging.INFO,
#                    filename='bot.log'
#
logging.basicConfig(filename="sample.log", level=logging.ERROR)

print("бот работает")

Qfile1 = "formA.txt"
Qfile2 = "formB.txt"
qwestionsA = ['0']
qwestionsB = []

shkala1Q = [1, 9, 17, 25, 33, 41]
shkala2Q = [2, 10, 18, 26, 34, 42]
shkala3Q = [3, 11, 19, 27, 35, 43]
shkala4Q = [4, 12, 20, 28, 36, 44]
shkala5Q = [5, 13, 21, 29, 37, 45]
shkala6Q = [6, 14, 22, 30, 38, 46]
shkala7Q = [7, 15, 23, 31, 39, 47]
shkala8Q = [8, 16, 24, 32, 40, 48]

invertQ = [5, 10, 12, 13, 18, 24, 25, 36, 27, 31, 33, 35, 47]

roles = ['role_1', 'role_2', 'role_3', 'role_4', 'role_5', 'role_6', 'role_7']
olds = range(6,100)
olds2 = []
for i in olds:
    olds2.append(str(i))

def loadQwestions(file1, file2):
    file1 = open(file1, encoding="utf8")
    #file2 = open(file2)

    global qwestionsA
    global qwestionsB

    for string in file1:
        qwestionsA.append(string)

    #for string in file2:
    #    qwestionsB.append(string)

qurrentData = []

loadQwestions(Qfile1, Qfile2)
qwestionsLen = len(qwestionsA) - 1

ansv1 = "Совершенно соответствует"
ansv2 = "Вполне соответсвует"
ansv3 = "Трудно сказать"
ansv4 = "Почти не соответствует"
ansv5 = "Совершенно не соответствует"

ansvN = ""
userdataPul = {}

def qwestInlineKeyboard():
    keyboard = types.InlineKeyboardMarkup()
    ansv1_button = types.InlineKeyboardButton(text=ansv1, callback_data="5")
    keyboard.add(ansv1_button)
    ansv2_button = types.InlineKeyboardButton(text=ansv2, callback_data="4")
    keyboard.add(ansv2_button)
    ansv3_button = types.InlineKeyboardButton(text=ansv3, callback_data="3")
    keyboard.add(ansv3_button)
    ansv4_button = types.InlineKeyboardButton(text=ansv4, callback_data="2")
    keyboard.add(ansv4_button)
    ansv5_button = types.InlineKeyboardButton(text=ansv5, callback_data="1")
    keyboard.add(ansv5_button)
    return keyboard

@bot.message_handler(commands=["start"])
def welcome_start(message):
    id = message.from_user.id
    #print(message.from_user.first_name)

    userdata = {'userid':'',
            'first_name':'',
            'last_name':'',
            'username': '',
            'qurrentQ': 0,
            'scales': {
                '1': 0,
                '2': 0,
                '3': 0,
                '4': 0,
                '5': 0,
                '6': 0,
                '7': 0,},
            'ansvers': [],
            'sex': "n",
            'role': "0",
            'old':0,
            'message_id':0,
            }

    userdataPul[id] = userdata

    userdataPul[id]['userid'] = id
    userdataPul[id]['first_name'] = message.from_user.first_name
    userdataPul[id]['last_name'] = message.from_user.last_name
    userdataPul[id]['username'] = message.from_user.username

    userdataPul[id]['scales']['1'] = 0
    userdataPul[id]['scales']['2'] = 0
    userdataPul[id]['scales']['3'] = 0
    userdataPul[id]['scales']['4'] = 0
    userdataPul[id]['scales']['5'] = 0
    userdataPul[id]['scales']['6'] = 0
    userdataPul[id]['scales']['7'] = 0
    userdataPul[id]['scales']['8'] = 0
    userdataPul[id]['qurrentQ'] = 0
    userdataPul[id]['ansvers'] = []

    keyboard_start = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text="Начать", callback_data="start32")
    keyboard_start.add(key_yes)
    startMessage = ('Этот опросник позволит Вам выявить основные черты Вашей индивидуальности. Постарайтесь долго не обдумывать вопросы, отвечайте по первому побуждению.'
                    'Так как данный вопросник не содержит "правильных" и "неправильных" ответов, старайтесь оценку "трудно сказать" использовать как можно реже. Спасибо за сотрудничество.')
    message = bot.send_message(
        message.chat.id,
        startMessage,
        reply_markup=keyboard_start
    )
    userdataPul[id]['message_id'] = message.id
    #bot.register_next_step_handler(message, inputPersonalData(id))
    #inputPersonalData(id)

@bot.callback_query_handler(func=lambda call: call.data == 'start32')
def process_start_button(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    inputSex(callback_query.from_user.id)
    #nextQ(callback_query.from_user.id)


def inputSex(id):
    keyboard = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text="М", callback_data="sexM")
    key2 = types.InlineKeyboardButton(text="Ж", callback_data="sexW")
    keyboard.add(key1, key2)
    #print(id)
    #bot.send_message(id, "Укажите ваш пол", reply_markup=keyboard)
    bot.edit_message_text(chat_id = id, message_id = userdataPul[id]['message_id'], text="Укажите ваш пол", reply_markup=keyboard)

"""
@bot.callback_query_handler(func=lambda c: True)
def process_all_button(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    print("all calldata")
"""


@bot.callback_query_handler(func=lambda call: call.data == 'sexM' or call.data == 'sexW')
def process_sex_button(callback_query: types.CallbackQuery):
    #print('process_sex_button')
    #print(callback_query.message)
    global userdataPul
    bot.answer_callback_query(callback_query.id)
    id = callback_query.from_user.id

    if not id in userdataPul:
        bot.send_message(id, "начните с команды /start")
        return

    if userdataPul[id]['sex'] == "m" or userdataPul[id]['sex'] == "w":
        #print(userdataPul[id]['sex'])
        bot.send_message(id, "пол уже указан")
        return

    if callback_query.data == 'sexM':
        userdataPul[callback_query.from_user.id]['sex'] = "m"
    elif callback_query.data == 'sexW':
        userdataPul[callback_query.from_user.id]['sex'] = "w"

    #bot.register_next_step_handler(callback_query.message, inputRole)
    inputRole(id)

def inputRole(id):
    keyboard = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text="Студент", callback_data="role_1")
    key2 = types.InlineKeyboardButton(text="Школьник", callback_data="role_2")
    key3 = types.InlineKeyboardButton(text="Гос. служащий", callback_data="role_3")
    key4 = types.InlineKeyboardButton(text="Пенсионер", callback_data="role_4")
    key5 = types.InlineKeyboardButton(text="Фрилансер", callback_data="role_5")
    key6 = types.InlineKeyboardButton(text="Безработный", callback_data="role_6")
    key7 = types.InlineKeyboardButton(text="Домохозяйка", callback_data="role_7")
    keyboard.add(key1, key2, key3, key4, key5, key6, key7)
    #bot.send_message(id, "Укажите вау социальную роль", reply_markup=keyboard)
    bot.edit_message_text(chat_id=id,message_id=userdataPul[id]['message_id'], text="Укажите вау социальную роль", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data in roles)
def process_role_button(callback_query: types.CallbackQuery):
    #print('process_role_button')
    global userdataPul
    bot.answer_callback_query(callback_query.id)
    id = callback_query.from_user.id

    if not id in userdataPul:
        bot.send_message(id, "начните с команды /start")
        return

    userdataPul[id]['role'] = callback_query.data
    inputOld(id)
    #nextQ(id)

def inputOld(id):
    keyboard = types.InlineKeyboardMarkup(row_width=8)
    buttons = []
    for i in range(6, 100):
        button = types.InlineKeyboardButton(text=i, callback_data=i)
        buttons.append(button)
    keyboard.add(*buttons)
    #bot.send_message(id, "Укажите ваш возраст", reply_markup=keyboard)
    bot.edit_message_text(chat_id = id, message_id = userdataPul[id]['message_id'], text = "Укажите ваш возраст", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data in olds2)
def process_old_button(callback_query: types.CallbackQuery):
    #print('process_old_button')
    global userdataPul
    bot.answer_callback_query(callback_query.id)
    id = callback_query.from_user.id

    if not id in userdataPul:
        bot.send_message(id, "начните с команды /start")
        return

    if userdataPul[id]['old'] != 0:
        bot.send_message(id, "возраст уже указан")
        return

    userdataPul[id]['old'] = callback_query.data
    nextQ(id)

#@bot.callback_query_handler(func=lambda c: 0 or 1 or 2 or 3 or 4)
@bot.callback_query_handler(func=lambda c: c.data == '1' or c.data == '2' or c.data == '3' or c.data == '4' or c.data == '5')
def process_callback_button(callback_query: types.CallbackQuery):
    #print('process_answer_button')
    global userdataPul
    global qwestionsLen
    id = callback_query.from_user.id
    bot.answer_callback_query(callback_query.id)

    if not id in userdataPul:
        bot.send_message(id, "Нет данных. Начните с команды /start")
        return


    answer(int(callback_query.data), id)
    #time.sleep(.1)

    if userdataPul[id]['qurrentQ'] == qwestionsLen:
        check_results(userdataPul[id]['ansvers'], id)
        print_results(id)
    elif userdataPul[id]['qurrentQ'] < qwestionsLen:
        nextQ(id)

    else:
        bot.send_message(id, "произошла ошибочка")

def nextQ(id):
    global userdataPul
    keyboard = qwestInlineKeyboard()
    #print(id)
    #print("пп: "+str(userdataPul[id]['qurrentQ']))
    userdataPul[id]['qurrentQ'] += 1
    if userdataPul[id]['message_id'] == 0:
        message = bot.send_message(id, qwestionsA[userdataPul[id]['qurrentQ']], reply_markup=keyboard)
        userdataPul[id]['message_id'] = message.id
    else:
        bot.edit_message_text(chat_id = id, message_id = userdataPul[id]['message_id'], text = qwestionsA[userdataPul[id]['qurrentQ']], reply_markup=keyboard )

    #userdataPul[id]['message_id'] = bot.send_message(id, qwestionsA[userdataPul[id]['qurrentQ']], reply_markup=keyboard)

def answer(button, id):
    global invertQ
    global userdataPul
    qurrentQ = userdataPul[id]['qurrentQ']

    userdataPul[id]['ansvers'].append(button)

def check_results(resultsData, id):
    index = 1

    def replaceAnswer(answer):
            if answer == 5:
                return 1
            elif answer == 4:
                return 2
            elif answer == 3:
                return 3
            elif answer == 2:
                return 4
            elif answer == 1:
                return 5

    for answer in resultsData:
        if index in invertQ:
            answer = replaceAnswer(answer)

        if index in shkala1Q:
            userdataPul[id]['scales']['1'] += answer
        elif index in shkala2Q:
            userdataPul[id]['scales']['2'] += answer
        elif index in shkala3Q:
            userdataPul[id]['scales']['3'] += answer
        elif index in shkala4Q:
            userdataPul[id]['scales']['4'] += answer
        elif index in shkala5Q:
            userdataPul[id]['scales']['5'] += answer
        elif index in shkala6Q:
            userdataPul[id]['scales']['6'] += answer
        elif index in shkala7Q:
            userdataPul[id]['scales']['7'] += answer
        elif index in shkala8Q:
            userdataPul[id]['scales']['8'] += answer
        index += 1

def print_results(id):
    global userdataPul

    def savedata():
        time = str(datetime.datetime.today()).replace(':', "-")
        time = time[0:19]
        filename = time + "-" + str(userdataPul[id]['userid'])

        datafile = open("results/"+filename, 'w')
        datafile.write(str(userdataPul[id]['ansvers'])+"\n")
        datafile.write(str(userdataPul[id]['userid'])+"\n")

        #if userdataPul[id]['username'] == None:
        #    datafile.write('none'+"\n")
        #else:
        #    datafile.write(userdataPul[id]['username']+"\n")

        #if userdataPul[id]['first_name'] == None:
        #    datafile.write('none'+"\n")
        #else:
        #    print(userdataPul[id]['first_name'])
        #    datafile.write(userdataPul[id]['first_name']+"\n")

        #if userdataPul[id]['last_name'] == None:
        #    datafile.write('none'+"\n")
        #else:
            #print(callback_query.from_user.last_name)
        #    datafile.write(userdataPul[id]['last_name']+"\n")

        datafile.write(userdataPul[id]['sex']+"\n")
        datafile.write(userdataPul[id]['role']+"\n")
        datafile.write(userdataPul[id]['old']+"\n")



        datafile.flush()
        datafile.close()

    scales_names = ["Шкала 1. Выраженность аффективных переживаний субъекта и его отношения к ним",
                    "Шкала 2. Степень опредмеченности желания субъекта",
                    "Шкала 3. Cтепень активности взаимодействия субъекта с реальностью",
                    "Шкала 4. Умение прогнозировать результат предпринимаемых действий",
                    "Шкала 5. Межличностное взаимодействие субъекта",
                    "Шкала 6. Cостояние самооценки субъекта",
                    "Шкала 7. Отношение к негативному опыту и степень фиксированности на имеющихся затруднениях"]

    sh1 = userdataPul[id]['scales']['1']
    sh2 = userdataPul[id]['scales']['2']
    sh3 = userdataPul[id]['scales']['3']
    sh4 = userdataPul[id]['scales']['4']
    sh5 = userdataPul[id]['scales']['5']
    sh6 = userdataPul[id]['scales']['6']
    sh7 = userdataPul[id]['scales']['7']
    sh8 = userdataPul[id]['scales']['8']
    scales = [sh1, sh2, sh3, sh4, sh5, sh6, sh7]
    userdataPul[id]['qurrentQ'] = 0

    scales_results = []
    for scale, scale_name in zip(scales, scales_names):
        if scale < 12:
            scales_results.append(f"{scale_name}\n{scale}/30\nДисфункция\n")
        elif scale > 24:
            scales_results.append(f"{scale_name}\n{scale}/30\nКомпенсация\n")
        else:
            scales_results.append(f"{scale_name}\n{scale}/30\nНорма")

    for result in scales_results:
        bot.send_message(id, result)
        time.sleep(1)

    text = '[интерпретация шкал](https://alex31415926.github.io)'
    bot.send_message(id, text, parse_mode='MarkdownV2')

    samoopredmechivanie = (sh1 + sh2 + sh3 + sh7) / 4
    samootsenivanie = (sh4 + sh6 + sh3 + sh7) / 4
    samoformirovanie = (sh1 + sh5 + sh3 + sh7) / 4
    samootojdestvlenie = (sh1 + sh2 + sh4 + sh6) / 4
    samopredyavlenie = (sh1 + sh5 + sh1 + sh2) / 4
    samoodobrenie = (sh1 + sh5 + sh4 + sh6) / 4

    mech_names = ["Механизм самоопредмечивания",
                    "Механизм самооценивания",
                    "Механизм самоформирования",
                    "Механизм самоотеждествления",
                    "Механизм самоопределения",
                    "Механизм самоодобрения"]

    subversions = ["Инверсная", "Нарциссическая", "Инфантильная", "Симбиотическая", "Производная", "Отчужденная"]

    mechs_stats = [samoopredmechivanie, samootsenivanie, samoformirovanie,
        samootojdestvlenie, samopredyavlenie, samoodobrenie]
    mechs = ""
    mechs = list(zip(mech_names, mechs_stats, subversions))

    results2 = []
    for mech, subv in zip(mechs, subversions):
        if mech[1] < 12:
            currentSub = "Дисфункция"
            results2.append(f"{mech[0]}: {mech[1]}\n{currentSub}.\n{mech[2]} субъектность")
        elif mech[1] > 24:
            currentSub = "Компенсация"
            results2.append(f"{mech[0]}: {mech[1]}\n{currentSub}.{mech[2]} субъектность")
        else:
            currentSub = "Норма"
            results2.append(f"{mech[0]}: {mech[1]}\n{currentSub}.")


    for str2, num in zip(results2, range(1, 7)):
        bot.send_message(id, str2)

    text = '[интерпретация механизмов](https://alex31415926.github.io/interpretation.html)'
    bot.send_message(id, text, parse_mode='MarkdownV2')

    text = '[статистика](https://psyservice-cfuv.ru/data/documents/otiscstat.php)'
    bot.send_message(id, text, parse_mode='MarkdownV2')


    savedata()
    #print(userdataPul[id])
    del userdataPul[id]
    #print(userdataPul[callback_query.from_user.id])





bot.polling(non_stop=True, interval=1)