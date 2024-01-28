import telebot
import time
from datetime import date
import time
from datetime import datetime
from datetime import datetime
from datetime import datetime, timedelta


bot = telebot.TeleBot('6487252741:AAFOYo2PBeFXoBNOP2aNfQD7aT03C0mVBSk')



stickers_data = {
    1: {
        1: f"8:50 - Укр мова\n10:35 - Алгебра \n12:30 - Інформатика \n14:15 - немає",
        2: f"8:50 - Всесвітня\n10:35 - Фізика \n12:30 - Астрономія \n14:15 - Технології",
        3: f"8:50 - Геометрія\n10:35 - Англ мова \n12:30 - Алгебра \n14:15 - ШПД Фізика",
        4: f"8:50 - Захист \n10:35 - Фізра \n12:30 - Біологія \n14:15 - ШПД Математика",
        5: f"8:50 - Фізика \n10:35 - Англ \n12:30 - Алгебра \n14:15 - Укр літ "
    },
    2: {
        1:  f"8:50 - Укр мова\n10:35 - Алгебра \n12:30 - Інфа \n14:15 - Англ мова ",
        2: f"8:50 - Зарубіжна\n 10:35 - Фізика \n12:30 - Геометрія\n14:15 - ШПД Укр мова",
        3: f"8:50 - Геометрія \n10:35 - Географія \n12:30 - Англ мова \n14:15 - Фізра",
        4: f"8:50 - Захист \n 10:35 - Біологія \n12:30 - Хімія \n14:15 - Історія укр ",
        5: f"8:50 - Укр літ\n 10:35 - Алгебра \n12:30 - Англ \n14:15 - ШПД Математика"
    },
    3: {
        1: f"8:50 - Укр мова\n10:35 - Алгебра \n12:30 - Інформатика \n14:15 - немає",
        2: f"8:50 - Всесвітня \n10:35 - Фізика \n12:30 - Астрономія \n14:15 - Технології",
        3: f"8:50 - Геометрія \n10:35 - Англ мова \n12:30 - Алгебра \n14:15 - ШПД Фізика",
        4: f"8:50 - Історія укр\n10:35 - Фізра \n12:30 - Хі14:15 - ШПД Укр мова ",
        5: f"8:50 - Фізика \n10:35 - Англ \n12:30 - Алгебра \n14:15 - Укр літ "
    },
    4: {
        1: f"8:50 - Укр мова \n10:35 - Алгебра \n12:30 - Технології \n14:15 - Англ мова ",
        2: f"8:50 - Зарубіжна \n10:35 - Фізика \n12:30 - Геометрія\n14:15 - ШПД Укр мова",
        3: f"8:50 - Геометрія \n10:35 - Географія \n12:30 - Англ мова \n14:15 - Фізра",
        4: f"8:50 - Захист \n10:35 - Біологія \n12:30 - Хімія \n14:15 - Історія укр ",
        5: f"8:50 - Укр літ\n10:35 - Алгебра \n12:30 - Англ \n14:15 - ШПД Математика"
    }
}

time_data = [['08:50:00', '09:35:00'], ['09:35:00', '09:40:00'], ['09:40:00', '10:25:00'],
                ['10:25:00', '10:35:00'],
                ['10:35:00', '11:20:00'], ['11:20:00', '11:25:00'], ['11:25:00', '12:10:00'],
                ['12:10:00', '12:30:00'],
                ['12:30:00', '13:15:00'], ['13:15:00', '13:20:00'], ['13:20:00', '14:00:00'],
                ['14:00:00', '14:15:00'],
                ['14:15:00', '15:00:00'], ['15:00:00', '15:05:00'], ['15:05:00', '15:50:00']]

time_names = ['перша пара перша півпара', 'маленька перерва', "перша пара друга півпара",
            'перша велика пара',
            'друга пара перша півпара', 'маленька перерва', 'друга пара друга півпара',
            'друга велика перерва',
            'третя пара перша півпара', 'маленька перерва', 'третя пара друга півпара',
            'третя велика перерва',
            'четверта пара перша півпара', 'маленька перерва', 'четверта пара друга півпара']
@bot.message_handler(commands=['start'])
def start(message):
    today = date.today()
    bot.reply_to(message, ('Привіт' + ' \N{Smiling Face with Open Mouth and Smiling Eyes}.' +  ' Цей бот зручно зберігає розклади в телеграмі' + '\n' + 'Команди:\n/diary_today - Розклад сьогодні\n/diary_tomorrow - Розклад завтра\n/time - Найближча перерва або пара\n/week - Розклад на тиждень' + '\n\n' + '\N{watch}'))
    print()



def calc_difference(start_date, cur_date):
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    cur_date = datetime.strptime(cur_date, '%Y-%m-%d')

    # Calculate the difference between the two dates
    delta = cur_date - start_date

    # Extract the number of days from the timedelta object
    days_passed = delta.days

    return days_passed + 1

def calc_week(num_days):

    if num_days <= 7:
        return(1, num_days)
    else:
        weeks = num_days // 7
        days = num_days % 7

        if days == 0 and weeks >= 1:
            if weeks <= 4:
                return(weeks,days)
            else:
                return (weeks % 4)
        elif days != 0 and weeks >= 1:
            return (weeks + 1, days)


@bot.message_handler(commands=['diary_today'])
def diary_sender1(message):
    today = date.today()
    start_date = '2024-01-22'
    message_txt = ''
    print(str(today))
    if str(today)[5:7] == '01' and str(today)[8:] == '21':
        bot.reply_to(message, f"Броускі чіл сьогодні немає пар. Сьогодні - НЕДІЛЯ")
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJ1mmWtD8YH3qUAAZxdAqBaj1X6Kf4SJgACCAADwDZPE29sJgveGptpNAQ')
    else:
        cur_date = str(today)
        calc_difference(start_date, cur_date)
        num_days = calc_difference(start_date, cur_date)
        print(str((calc_week(num_days))))
        week = str((calc_week(num_days)))[1]
        day = str((calc_week(num_days)))[-2]
        print('week - ', int(week))
        print('day - ', int(day))
        if int(day) == 0:
            bot.reply_to(message, f"Броускі чіл сьогодні немає пар. Сьогодні - НЕДІЛЯ")
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJ1mmWtD8YH3qUAAZxdAqBaj1X6Kf4SJgACCAADwDZPE29sJgveGptpNAQ')
        elif int(day) == 6:
            bot.reply_to(message, f"Броускі чіл сьогодні немає пар. Сьогодні - СУБОТА")
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJ1mmWtD8YH3qUAAZxdAqBaj1X6Kf4SJgACCAADwDZPE29sJgveGptpNAQ')
        else:
            message_txt += 'Сьогодні ось такий розклад:' + '\n'
            message_txt += stickers_data[int(week)][int(day)]
    response = message_txt + '\n\n' + '\N{watch}'
    bot.send_message(message.chat.id, response)

@bot.message_handler(commands=['diary_tomorrow'])
def diary_sender2(message):
    today = date.today()
    start_date = '2024-01-22'
    cur_date = str(today)
    message_txt = ''
    print(cur_date)
    if cur_date == '2024-01-21':
        print('hey')
        message_txt += ('Завтра - ПОНЕДІЛОК' + '\N{skull}.' + 'Буде такий розклад:')
        message_txt += '\n' + stickers_data[1][1]
    else:
        calc_difference(start_date, cur_date)
        num_days = calc_difference(start_date, cur_date)
        print(str((calc_week(num_days))))
        week = str((calc_week(num_days)))[1]
        day = str((calc_week(num_days)))[-2]
        print('week - ', int(week))
        print('day - ', int(day))
        if int(day) == 7:
            message_txt += ('Завтра - ПОНЕДІЛОК' + '\N{skull}.' + 'Буде такий розклад:')
            message_txt += '\n' +stickers_data[int(week) + 1][1]
        elif int(day) == 6:
            message_txt += ('Броускі чіл завтра  немає пар. Завтра - НЕДІЛЯ ' + '\N{Face with Cowboy Hat}.' + ' В понеділок розклад буде такий:')
            message_txt += '\n' + stickers_data[int(week) + 1][1]
        elif int(day) == 5:
            message_txt += ('Броускі чіл завтра  немає пар. Завтра - Субота ' + '\N{Face with Cowboy Hat}.' + ' В понеділок розклад буде такий:')
            message_txt += '\n' + stickers_data[int(week) + 1][1]
        else:
            message_txt += f" Завтра буде такий розклад: "
            message_txt += '\n' + stickers_data[int(week)][int(day) + 1]
    response = message_txt + '\n\n' + '\N{watch}'
    bot.send_message(message.chat.id, response)

# 8.50 - 9.35, 9.35-9.40, 9.40-10.25, 10.25-10.35
#
#
#


def is_within_boundaries(time1_str, time2_str, current_time_str):
    time_format = "%H:%M:%S"

    # Convert strings to datetime objects
    time1 = datetime.strptime(time1_str, time_format)
    time2 = datetime.strptime(time2_str, time_format)
    current_time = datetime.strptime(current_time_str, time_format)

    # Check if current_time is within the boundaries
    if time1 <= current_time < time2:
        return True
    else:
        return False

def time_difference(input1, input2):
    # Convert string inputs to datetime objects
    time_format = "%H:%M:%S"
    datetime1 = datetime.strptime(input1, time_format)
    datetime2 = datetime.strptime(input2, time_format)

    # Calculate the time difference
    time_diff = datetime2 - datetime1

    # Extract hours and minutes from the time difference
    hours, remainder = divmod(time_diff.seconds, 3600)
    minutes, _ = divmod(remainder, 60)

    # Build the output string
    output = ""
    if hours > 0:
        output += f"{hours} годину{'s' if hours > 1 else ''} "
    if minutes > 0 and minutes!= 1:
        output += f"{minutes} хвилин"
    elif minutes > 0 and minutes == 1:
        output += f"{minutes} хвилину"

    return output if output else "0 minutes"

@bot.message_handler(commands=['time'])
def diary_sender2(message):

    current_datetime = datetime.now()

    # Subtract two hours from the current datetime
    result_datetime = current_datetime + timedelta(hours=2)

    # Format the result as a string
    result_time = result_datetime.strftime('%H:%M:%S')
    #bot.reply_to(message, result_time )
    if is_within_boundaries('08:50:00', '15:50:00', result_time) == False:
        message_txt = 'Броускі чіл. Зараз НЕМАЄ пар'
    for i in range(len(time_data)):
        if is_within_boundaries(time_data[i][0], time_data[i][1], str(result_time)):
           if 'перерва' in time_names[i].lower():

                message_txt = 'Зараз - '+ str(time_names[i]) + '\n' + 'Наступна півпара/пара буде через - ' + str(time_difference(result_time, time_data[i][1]))
           elif 'пара' in time_names[i].lower():
                if 'четверта' not in time_names[i] and 'друга' not in time_names[i] and 'маленька' in time_names[i + 1].lower():

                    message_txt = 'Зараз - '+ str(time_names[i]) + '\n' + 'Наступна маленька перерва буде через - ' + str(time_difference(result_time, time_data[i][1]))

                elif 'четверта' not in time_names[i] and 'друга' not in time_names[i] and 'велика' in time_names[i + 1].lower():
                    message_txt = 'Зараз - '+ str(time_names[i]) + '\n' + 'Наступна велика перерва буде через - ' + str(time_difference(result_time, time_data[i][1]))
                else:
                      message_txt = 'Зараз - '+ str(time_names[i]) + '\n' + 'Закінчення пари через - ' + str(time_difference(result_time, time_data[i][1]))

    output = message_txt + '\n\n' + '\N{watch}'
    bot.reply_to(message, output )

@bot.message_handler(commands=['week'])
def diary_sender5(message):
    today = date.today()
    start_date = '2024-01-22'
    cur_date = str(today)
    message_txt = ''
    print(cur_date)
    if cur_date == '2024-01-21':
        print('hey')
        message_txt += ('Завтра - ПОНЕДІЛОК' + '\N{skull}.' + 'Буде такий розклад:')
        message_txt += '\n' + stickers_data[1][1]
    else:
        calc_difference(start_date, cur_date)
        num_days = calc_difference(start_date, cur_date)
        print(str((calc_week(num_days))))
        week = str((calc_week(num_days)))[1]
        day = str((calc_week(num_days)))[-2]
        print('week - ', int(week))
        print('day - ', int(day))
        if int(day) == 0:
            message_txt += ('Наступний тиждень буде - ' + str(week) + '\N{skull}.' + 'Протягом тидня буде такий розклад:')
            message_txt += '\n' + 'Понеділок' + '\n' +stickers_data[int(week) + 1][1] + '\n'
            message_txt += '\n' + 'Вівторок' + '\n' +stickers_data[int(week) + 1][2] + '\n'
            message_txt += '\n' + 'Середа' + '\n' +stickers_data[int(week) + 1][3] + '\n'
            message_txt += '\n' + 'Четвер' + '\n' +stickers_data[int(week) + 1][4] + '\n'
            message_txt += '\n' + 'Пятниця' + '\n' +stickers_data[int(week) + 1][5] + '\n'

        elif int(day) == 6:
            message_txt += ('Броускі чіл завтра  немає пар. Завтра - НЕДІЛЯ ' + '\N{Face with Cowboy Hat}.' + 'Наступний тиждень буде - ' + str(week) + ':')
            message_txt += '\n' + 'Понеділок' + '\n' +stickers_data[int(week) + 1][1] + '\n'
            message_txt += '\n' + 'Вівторок' + '\n' +stickers_data[int(week) + 1][2] + '\n'
            message_txt += '\n' + 'Середа' + '\n' +stickers_data[int(week) + 1][3] + '\n'
            message_txt += '\n' + 'Четвер' + '\n' +stickers_data[int(week) + 1][4] + '\n'
            message_txt += '\n' + 'Пятниця' + '\n' +stickers_data[int(week) + 1][5] + '\n'
        elif int(day) == 5:
            message_txt += ('Броускі чіл завтра  немає пар. Завтра - Субота ' + '\N{Face with Cowboy Hat}.' + 'Наступний тиждень буде - ' + str(week) + ':')
            message_txt += '\n' + 'Понеділок' + '\n' +stickers_data[int(week) + 1][1] + '\n'
            message_txt += '\n' + 'Вівторок' + '\n' +stickers_data[int(week) + 1][2] + '\n'
            message_txt += '\n' + 'Середа' + '\n' +stickers_data[int(week) + 1][3] + '\n'
            message_txt += '\n' + 'Четвер' + '\n' +stickers_data[int(week) + 1][4] + '\n'
            message_txt += '\n' + 'Пятниця' + '\n' +stickers_data[int(week) + 1][5] + '\n'
        else:
            message_txt += 'Тиждень - ' +  str(week) + '. Протягом тижня ось такий розклад:'



            message_txt += '\n' + 'Понеділок' + '\n' +stickers_data[int(week) ][1] + '\n'
            message_txt += '\n' + 'Вівторок' + '\n' +stickers_data[int(week) ][2] + '\n'
            message_txt += '\n' + 'Середа' + '\n' +stickers_data[int(week) ][3] + '\n'
            message_txt += '\n' + 'Четвер' + '\n' +stickers_data[int(week) ][4] + '\n'
            message_txt += '\n' + 'Пятниця' + '\n' +stickers_data[int(week) ][5] + '\n'



    response = message_txt + '\n\n' + '\N{watch}'
    bot.send_message(message.chat.id, response)




bot.infinity_polling(none_stop=True)
