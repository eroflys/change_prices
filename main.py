# from telegram import Update
#from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
import time

import telebot
from pyexpat.errors import messages
from requests import get, post
#from datetime import datetime
from telethon.sync import TelegramClient
from telethon.sync import TelegramClient
from telethon import functions, types
import io


# with io.open("tests.py", 'r', encoding='utf-8') as file:
#     exec(file.read())
# print(1)
# api_id = 263
# api_hash = 'hash'
# client = TelegramClient('session_name', api_id, api_hash)
# texts = {'dyson': [296], 'iMac': [292], 'playstation': [295], 'iPad': [291], 'Watch': [289], 'MacBook': [290],
#                'iPhone 11_12_13': [297], 'iPhone 14': [298], 'iPhone 15': [299], 'iPhone 16': [300],
#                'airpods': [288]}  # Example message IDs
# client.start()

# async def get_channel_messages(channel_id, message_ids):
#     global texts
#     for i in message_ids:
#         try:
#             messages = await client.get_messages(channel_id, ids=message_ids[i])
#             for message in messages:
#                 texts[i] = str(message.text)
#         except Exception as e:
#             print(f"Error: {e}")

# def get_channel_messages(channel_id, message_ids):
#     global texts
#     global client
#     for i in message_ids:
#         try:
#             messages = client.get_messages(channel_id, ids=message_ids[i])
#             for message in messages:
#                 texts[i] = str(message.text)
#         except Exception as e:
#             print(f"Error: {e}")
#
# def get_ms():
#
#     global texts
#
#
#
#     channel_id = 'icity_store'
#     message_ids = {'dyson': [296], 'iMac': [292], 'playstation': [295], 'iPad': [291], 'Watch': [289], 'MacBook': [290], 'iPhone 11_12_13': [297], 'iPhone 14': [298], 'iPhone 15': [299], 'iPhone 16': [300], 'airpods': [288]} # Example message IDs
#     get_channel_messages(channel_id, message_ids)
#     print(1)


# def get_ms():
#
#     global texts
#
#
#
#     channel_id = 'icity_store'
#     message_ids = {'dyson': [296], 'iMac': [292], 'playstation': [295], 'iPad': [291], 'Watch': [289], 'MacBook': [290], 'iPhone 11_12_13': [297], 'iPhone 14': [298], 'iPhone 15': [299], 'iPhone 16': [300], 'airpods': [288]} # Example message IDs
#     client.start()
#     client.loop.run_until_complete(get_channel_messages(channel_id, message_ids))
#     client.disconnect()
#     print(1)


# price = int(''.join(i.split('-')[1].split('.'))[:5]) * 1.1
# # Checking prices for iphones 11 64
    # max_price = 5000
    # colours11_64 = {'11 64 Black-': False, '11 64 White-': False, '11 64 Blue-': False, '11 64 Purple-': False}
    # for i in colours11_64:
    #     if check_colour(i, html_format):
    #         colours11_64[i] = True
    #         if int(''.join(html_format.split(i)[1][:6].split('.'))) * 1.1 > max_price:
    #             max_price = int(''.join(html_format.split(i)[1][:6].split('.')))
    #
    # if colours11_64['11 64 Black-']:
    #     black11_64 = int(''.join(html_format.split('11 64 Black-')[1][:6].split('.'))) * 1.1
    # else:
    #     black11_64 = max_price * 1.1
    # if colours11_64['11 64 White-']:
    #     white11_64 = int(''.join(html_format.split('11 64 White-')[1][:6].split('.'))) * 1.1
    # else:
    #     white11_64 = max_price * 1.1
    # if colours11_64['11 64 Blue-']:
    #     blue11_64 = int(''.join(html_format.split('11 64 Blue-')[1][:6].split('.'))) * 1.1
    # else:
    #     blue11_64 = max_price * 1.1
    # if colours11_64['11 64 Purple-']:
    #     purple11_64 = int(''.join(html_format.split('11 64 Purple-')[1][:6].split('.'))) * 1.1
    # else:
    #     purple11_64 = max_price * 1.1
    #
    #
    # #Checking prices for iphone 11 128
    # max_price = 5000
    # colours11_128 = {'11 128 Black-': False, '11 128 White-': False, '11 128 Red-': False, '11 128 Yellow-': False, '11 128 Purple-': False}
    # for i in colours11_128:
    #     if check_colour(i, html_format):
    #         colours11_128[i] = True
    #         if int(''.join(html_format.split(i)[1][:6].split('.'))) * 1.1 > max_price:
    #             max_price = int(''.join(html_format.split(i)[1][:6].split('.')))
    # if colours11_128['11 128 Black-']:
    #     black11_128 = int(''.join(html_format.split('11 128 Black-')[1][:6].split('.'))) * 1.1
    # else:
    #     black11_128 = max_price * 1.1
    # if colours11_128['11 128 White-']:
    #     white11_128 = int(''.join(html_format.split('11 128 White-')[1][:6].split('.'))) * 1.1
    # else:
    #     white11_128 = max_price * 1.1
    # if colours11_128['11 128 Red-']:
    #     red11_128 = int(''.join(html_format.split('11 128 Red-')[1][:6].split('.'))) * 1.1
    # else:
    #     red11_128 = max_price * 1.1
    # if colours11_128['11 128 Purple-']:
    #     purple11_128 = int(''.join(html_format.split('11 128 Purple-')[1][:6].split('.'))) * 1.1
    # else:
    #     purple11_128 = max_price * 1.1
    # if colours11_128['11 128 Yellow-']:
    #     yellow11_128 = int(''.join(html_format.split('11 128 Yellow-')[1][:6].split('.'))) * 1.1
    # else:
    #     yellow11_128 = max_price * 1.1
    #
    #
    # #Checking prices for iphone 12 mini 64
    # max_price = 5000
    # colours12_mini_64 = {'12 mini 64 White-': False, '12 mini 64 Blue-': False, '12 mini 64 Purple-': False, '12 mini 64 Green-': False,
    #                  '12 mini 64 Red-': False}
    # for i in colours12_mini_64:
    #     if check_colour(i, html_format):
    #         colours12_mini_64[i] = True
    #         if int(''.join(html_format.split(i)[1][:6].split('.'))) * 1.1 > max_price:
    #             max_price = int(''.join(html_format.split(i)[1][:6].split('.')))
    # if colours12_mini_64['12 mini 64 White-']:
    #     white12_mini_64 = int(''.join(html_format.split('12 mini 64 White-')[1][:6].split('.'))) * 1.1
    # else:
    #     white12_mini_64 = max_price * 1.1
    # if colours12_mini_64['12 mini 64 Blue-']:
    #     blue12_mini_64 = int(''.join(html_format.split('12 mini 64 Blue-')[1][:6].split('.'))) * 1.1
    # else:
    #     blue12_mini_64 = max_price * 1.1
    # if colours12_mini_64['12 mini 64 Purple-']:
    #     purple12_mini_64 = int(''.join(html_format.split('12 mini 64 Purple-')[1][:6].split('.'))) * 1.1
    # else:
    #     purple12_mini_64 = max_price * 1.1
    # if colours12_mini_64['12 mini 64 Green-']:
    #     green12_mini_64 = int(''.join(html_format.split('12 mini 64 Green-')[1][:6].split('.'))) * 1.1
    # else:
    #     green12_mini_64 = max_price * 1.1
    # if colours12_mini_64['12 mini 64 Red-']:
    #     red12_mini_64 = int(''.join(html_format.split('12 mini 64 Red-')[1][:6].split('.'))) * 1.1
    # else:
    #     red12_mini_64 = max_price * 1.1
    #
    #
    # #Checking prices for iphone 12 mini 128
    # max_price = 5000
    # colours12_mini_128 = {'12 mini 128 White-': False, '12 mini 128 Blue-': False,
    #                      '12 mini 128 Green-': False,
    #                      '12 mini 128 Red-': False}
    # for i in colours11_128:
    #     if check_colour(i, html_format):
    #         colours12_mini_64[i] = True
    #         if int(''.join(html_format.split(i)[1][:6].split('.'))) * 1.1 > max_price:
    #             max_price = int(''.join(html_format.split(i)[1][:6].split('.')))
    # if colours12_mini_64['12 mini 64 White-']:
    #     white12_mini_64 = int(''.join(html_format.split('12 mini 64 White-')[1][:6].split('.'))) * 1.1
    # else:
    #     white12_mini_64 = max_price * 1.1
    # if colours11_128['12 mini 64 Blue-']:
    #     blue12_mini_64 = int(''.join(html_format.split('12 mini 64 Blue-')[1][:6].split('.'))) * 1.1
    # else:
    #     blue12_mini_64 = max_price * 1.1
    # if colours11_128['12 mini 64 Purple-']:
    #     purple12_mini_64 = int(''.join(html_format.split('12 mini 64 Purple-')[1][:6].split('.'))) * 1.1
    # else:
    #     purple12_mini_64 = max_price * 1.1
    # if colours11_128['12 mini 64 Green-']:
    #     green12_mini_64 = int(''.join(html_format.split('12 mini 64 Green-')[1][:6].split('.'))) * 1.1
    # else:
    #     green12_mini_64 = max_price * 1.1
    # if colours11_128['12 mini 64 Red-']:
    #     red12_mini_64 = int(''.join(html_format.split('12 mini 64 Red-')[1][:6].split('.'))) * 1.1
    # else:
    #     red12_mini_64 = max_price * 1.1

# # def start(update, context):
# #     update.message.reply_text('1')
#
#
# def chlvl(update, context):
#     update.message.reply_text('1')
#
# # def change(chanel_name, message_id, new_text):
# #     bot.editMessageText(chat_id='@manygays', message_id=2, text='228777')
#
#
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
#
#
# async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
#
#
# async def precho(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await context.bot.editMessageText(chat_id='@manygays', message_id=3, text='228777')
#
#
# def get_data():
#     response = get('https://t.me/BigSaleApple/11200')
#     html_format = str(response.content)
#     print(html_format)
#
# def main():
#     application = ApplicationBuilder().token('token').build()
#
#     start_handler = CommandHandler('start', start)
#     change_handler = CommandHandler('change', precho)
#     echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
#     application.add_handler(start_handler)
#     application.add_handler(change_handler)
#     application.add_handler(echo_handler)
#
#     get_data()
#     application.run_polling()
#
#
# if __name__ == '__main__':
#     main()

bot = telebot.TeleBot('token')
# https://api.telegram.org/bottoken/channels.getMessages?

def normal_form(message):
    res = ''
    for i in message:
        if i == '*' or i == '_':
            pass


def del_b_u(message):
    res = message
    while '<b>' in res:
        res = res[:res.index('<b>')] + res[res.index('<b>') + 3:]
    while '</b>' in res:
        res = res[:res.index('</b>')] + res[res.index('</b>') + 4:]
    while '<u>' in res:
        res = res[:res.index('<u>')] + res[res.index('<u>') + 3:]
    while '</u>' in res:
        res = res[:res.index('</u>')] + res[res.index('</u>') + 4:]
        return res
def get_prices(prices):
    res = ''
    price = prices.lower().split('2 sim')[0]
    var = []
    for i in price:
        if i.isdigit():
            res += i
        else:
            if i != '.' and i != '_' and i != '*' and len(res) > 0:
                var.append(int(res))
                break

    if len(res) != 0:
        var.append(int(res))
    if len(var) > 0:
        if sorted(var)[-1] < 20000:
            print(var)
            print(prices)
        return sorted(var)[-1]
    else:
        return False


def ch_pr(dict, name, price):
    if name in dict:
        if dict[name] < price:
            return False
    return True


def converter(number):
    n = int(number)
    if n >= 100000:
        res = str(n)[:3] + '.' + str(n)[3:] + '₽'
    elif 1000 <= n < 10000:
        res = str(n)[:1] + '.' + str(n)[1:] + '₽'
    elif n < 1000:
        res = str(n) + '₽'
    else:
        res = str(n)[:2] + '.' + str(n)[2:] + '₽'
    return res

def chlcj(pr, txt: str):
    if pr in txt:
        return('\\' + pr).join(txt.split(pr))
    return txt

def normal(txt: str):
    tt = txt
    tt = chlcj('-', tt)
    tt = chlcj('.', tt)
    tt = chlcj('<', tt)
    tt = chlcj('>', tt)
    tt = chlcj('(', tt)
    tt = chlcj(')', tt)
    tt = chlcj('+', tt)
    while '__' in tt:
        a = tt.index('__')
        tt = tt[:a] + '_' + tt[a + 2:]
    while '**' in tt:
        a = tt.index('**')
        tt = tt[:a] + '*' + tt[a + 2:]
    su = 0
    sr = 0
    uu = 0
    ur = 0
    u = 0
    for i in tt:
        u += 1
        if i == '_':
            ur += 1
            uu = u
        if i == '*':
            sr += 1
            su = u
    if ur % 2 != 1:
        tt = tt[:uu] + '_' + tt[uu:]
    if sr % 2 != 0:
        tt = tt[:su] + '*' + tt[su:]
    return tt


def new_price(txt: str):
    tt = txt
    pr = tt.split('-')
    tt = '-'.join(pr[:-1]) + '- ' + converter(int(get_prices(pr[-1]) * 1.07))
    return tt


def check_colour(colour, message):
    if len(message.split(colour)) == 1:
        return False
    else:
        return True


def i11_12_13(texts):
    msg = texts['iPhone 11_12_13'].split('\n')
    message = ''
    for i in msg:
        if '₽' not in i:
            message += (i) + '\n'
        else:
            message += new_price(i) + '\n'
    message += '\n**НАВИГАЦИЯ**🧭🗺️\n\n🧑‍💻Для связи:\n\n@Karloff\\_Devices\n+7(903) 322-00-00\n\n@Vladejslavoi\n+7 (928) 654-54-53\n\n\nМы работаем:\nПн-Сб с 10:00 до 21:00\n🗺️Г. Москва,\nметро Багратионовская,\nТЦ «Горбушка ул.Барклая 8,\n123 павильон.\n\nДоставка по Москве🚗\nРегионам России и странам СНГ✈️'
    return normal(message)
    # post('https://api.telegram.org/bottoken/editMessageText?chat_id=@testchannel1102&message_id=5&parse_mode=HTML&text=' + message)
    # print(message)
    # return message
    # context.bot.editMessageText(chat_id='@karloffdevices', message_id=441, parse_mode='HTML', text=message)
    # response = get('https://t.me/karloffdevices/441')
    # if del_b_u(message) not in str(response.text).split('meta property="og:description" content="')[1].split('">')[0]:
    #     return message
    #     # post('https://api.telegram.org/bottoken/editMessageText?chat_id=@karloffdevices&message_id=441&parse_mode=HTML&text='+message)
    # else:
    #     return message

def i16(texts):
    msg = texts['iPhone 16'].split('\n')
    message = ''
    for i in msg:
        if '₽' not in i:
            message += (i) + '\n'
        else:
            message += new_price(i) + '\n'
    message += '\n**НАВИГАЦИЯ**🧭🗺️\n\n🧑‍💻Для связи:\n\n@Karloff\\_Devices\n+7(903) 322-00-00\n\n@Vladejslavoi\n+7 (928) 654-54-53\n\n\nМы работаем:\nПн-Сб с 10:00 до 21:00\n🗺️Г. Москва,\nметро Багратионовская,\nТЦ «Горбушка ул.Барклая 8,\n123 павильон.\n\nДоставка по Москве🚗\nРегионам России и странам СНГ✈️'
    return normal(message)
    # context.bot.editMessageText(chat_id='@karloffdevices', message_id=440, parse_mode='HTML', text=message)
    # response = get('https://t.me/karloffdevices/440')
    # if message not in str(response.text):
    #     post(
    #         'https://api.telegram.org/bottoken/editMessageText?chat_id=@karloffdevices&message_id=440&parse_mode=HTML&text=' + message)


def i14(texts):
    msg = texts['iPhone 14'].split('\n')
    message = ''
    for i in msg:
        if '₽' not in i:
            message += (i) + '\n'
        else:
            message += new_price(i) + '\n'
    message += '\n**НАВИГАЦИЯ**🧭🗺️\n\n🧑‍💻Для связи:\n\n@Karloff\\_Devices\n+7(903) 322-00-00\n\n@Vladejslavoi\n+7 (928) 654-54-53\n\n\nМы работаем:\nПн-Сб с 10:00 до 21:00\n🗺️Г. Москва,\nметро Багратионовская,\nТЦ «Горбушка ул.Барклая 8,\n123 павильон.\n\nДоставка по Москве🚗\nРегионам России и странам СНГ✈️'
    return normal(message)
    # context.bot.editMessageText(chat_id='@karloffdevices', message_id=439, parse_mode='HTML', text=message)
    # response = get('https://t.me/karloffdevices/439')
    # if message not in str(response.text):
    #     post(
    #         'https://api.telegram.org/bottoken/editMessageText?chat_id=@karloffdevices&message_id=439&parse_mode=HTML&text=' + message)


def i15(texts):
    msg = texts['iPhone 15'].split('\n')
    message = ''
    for i in msg:
        if '₽' not in i:
            message += (i) + '\n'
        else:
            message += new_price(i) + '\n'
    message += '\n**НАВИГАЦИЯ**🧭🗺️\n\n🧑‍💻Для связи:\n\n@Karloff\\_Devices\n+7(903) 322-00-00\n\n@Vladejslavoi\n+7 (928) 654-54-53\n\n\nМы работаем:\nПн-Сб с 10:00 до 21:00\n🗺️Г. Москва,\nметро Багратионовская,\nТЦ «Горбушка ул.Барклая 8,\n123 павильон.\n\nДоставка по Москве🚗\nРегионам России и странам СНГ✈️'
    return normal(message)
    # if message not in str(response.text):
    #     print(message)
    #     post(
    #         'https://api.telegram.org/bottoken/editMessageText?chat_id=@karloffdevices&message_id=777&parse_mode=HTML&text=' + message)



def watch(texts):
    msg = texts['Watch'].split('\n')
    message = ''
    for i in msg:
        if '₽' not in i:
            message += (i) + '\n'
        else:
            message += new_price(i) + '\n'
    message += '\n**НАВИГАЦИЯ**🧭🗺️\n\n🧑‍💻Для связи:\n\n@Karloff\\_Devices\n+7(903) 322-00-00\n\n@Vladejslavoi\n+7 (928) 654-54-53\n\n\nМы работаем:\nПн-Сб с 10:00 до 21:00\n🗺️Г. Москва,\nметро Багратионовская,\nТЦ «Горбушка ул.Барклая 8,\n123 павильон.\n\nДоставка по Москве🚗\nРегионам России и странам СНГ✈️'
    return normal(message)


def dyson(texts):
    msg = texts['dyson'].split('\n')
    message = ''
    for i in msg:
        if '₽' not in i:
            message += (i) + '\n'
        else:
            message += new_price(i) + '\n'
    message += '\nДля связи:\n\n@Karloff\\_Devices\n+7(903) 322-00-00\n'
    return normal(message)


def playstation(texts):
    msg = texts['playstation'].split('\n')
    message = ''
    for i in msg:
        if '₽' not in i:
            message += (i) + '\n'
        else:
            message += new_price(i) + '\n'
    message += '\nДля связи:\n\n@Karloff\\_Devices\n+7(903) 322-00-00\n'
    return normal(message)


def find_price(text):
    pd = 0
    n = False
    ix = 0
    f = False
    for i in text:
        if not f and (i.isdigit() or (pd > 0 and i == '.')):
            n = ix
            pd = 1
            f = True
        elif i.isdigit() or (pd > 0 and i == '.') and f:
            if not n:
                n = ix
            pd += 1
        else:
            f = False
            pass
        ix += 1
    return [text[:n], get_prices(text[n:])]

def iMac(texts):
    msg = texts['iMac'].split('\n')
    message = ''
    for i in msg:
        if '₽' not in i:
            message += i + '\n'
        else:
            message += new_price(i) + '\n'
    message += '\nДля связи:\n\n@Karloff\\_Devices\n+7(903) 322-00-00\n'
    return normal(message)


def macBook(texts: dict):
    msg = texts['MacBook'].split('\n')
    message = ''
    for i in msg:
        if '₽' not in i:
            message += (i) + '\n'
        else:
            message += new_price(i) + '\n'
    mf = '—————————————————'.join(message.split('—————————————————')[:3]) + 'Продолжение в следующем сообщении>>>'
    ms = '—————————————————'.join(message.split('—————————————————')[3:]) + '\nДля связи:\n\n@Karloff\\_Devices\n+7(903) 322-00-00\n'
    return [normal(mf), normal(ms)]


# def android():
#     response = get('https://t.me/BigSaleApple/10982')
#     response1 = get('https://t.me/BigSaleApple/10983')
#     html_format = str(response.text).split('месяцев  - 8.000')[1].split('\n') + str(response1.text).split('Гарантия 14 дней со дня покупки')[1].split('\n')
#     google = {}
#     samsung = {}
#     samsung_tab = {}
#     poco = {}
#     xiaomi = {}
#     headphones = {}
#     watch = {}
#     for i in html_format:
#         # print(i)
#         if 'watch' in i.lower() or 'amazfit' in i.lower():
#             print(i)
#             price = int(find_price(i)[1]) * 1.1
#             if price > 1000:
#                 watch[find_price(i)[0]] = price
#         if 'buds' in i.lower() or 'wireless' in i.lower() or 'ear' in i.lower() or 'tws' in i.lower() or 'soundcore' in i.lower() or 'sony wh' in i.lower():
#             price = int(find_price(i)[1]) * 1.1
#             print(find_price(i)[1], find_price(i)[0], 'z v o')
#             if price > 1000:
#                 headphones[find_price(i)[0]] = price
#         if 'pixel' in i.lower():
#             price = int(find_price(i)[1]) * 1.1
#             if price > 1000:
#                 google[find_price(i)[0]] = price
#         if 'pixel' in i.lower() or 'a15' in i.lower() or 'a25' in i.lower() or 'a35' in i.lower() or 'a54' in i.lower() or 's23' in i.lower() or 'a55' in i.lower() or 's24' in i.lower() or 'flip' in i.lower():
#             price = int(find_price(i)[1]) * 1.1
#             if price > 1000:
#                 samsung[find_price(i)[0]] = price
#         if 'tab' in i.lower():
#             price = int(find_price(i)[1]) * 1.1
#             if price > 1000:
#                 samsung_tab[find_price(i)[0]] = price
#         if 'poco' in i.lower():
#             price = int(find_price(i)[1]) * 1.1
#             if price > 1000:
#                 poco[find_price(i)[0]] = price
#         if 'note' in i.lower() or 'mi' in i.lower():
#             price = int(find_price(i)[1]) * 1.1
#             if price > 1000:
#                 xiaomi[find_price(i)[0]] = price
#
#     message1 = '''<b><u>Представляем вам большой ассортимент техники ANDROID</u></b>
#
# Мы не вписали все цвета и модели, по этому по конкретной модели можете уточнять:
# @Karloff_Devices_manager'''
#     if len(google) != 0:
#         message1 += '\n<b>Google Pixel</b>\n\n'
#         for i in google:
#             message1 += i + converter(google[i]) + '\n'
#     if len(samsung) != 0:
#         message1 += '\n<b>Samsung</b>\n\n'
#         for i in samsung:
#             message1 += i + converter(samsung[i]) + '\n'
#     if len(poco) != 0:
#         message1 += '\n<b>Poco</b>\n\n'
#         for i in poco:
#             message1 += i + converter(poco[i]) + '\n'
#     if len(xiaomi) != 0:
#         message1 += '\n<b>Xiaomi</b>\n\n'
#         for i in xiaomi:
#             message1 += i + converter(xiaomi[i]) + '\n'
#     message1 += '\nПродолжение в следующем сообщении>>>'
#     message = ''
#     if len(samsung_tab) != 0:
#         message += '\n<b>Samsung Tab</b>\n\n'
#         for i in samsung_tab:
#             message += i + converter(samsung_tab[i]) + '\n'
#     if len(watch) != 0:
#         message += '\n<b>Часы</b>\n\n'
#         for i in watch:
#             message += i + converter(watch[i]) + '\n'
#     if len(headphones) != 0:
#         message += '\n<b>Наушники</b>\n\n'
#         for i in headphones:
#             message += i + converter(headphones[i]) + '\n'
#     message += '''Для заказа и по вопросам пишите
# @karloff_Devices_manager
# Whatsapp
# https://wa.me/79098440000
#
# Доставка по Москве
# Регионам России и странам СНГ
#
# Самовывоз: Москва, ул.Барклая 8, 123 павильон
#
# #Android'''
#     # print(message1, message)
#     return [message1, message]


def ipad(texts):
    msg = texts['iPad'].split('\n')
    message = ''
    for i in msg:
        if '₽' not in i:
            message += (i) + '\n'
        else:
            message += new_price(i) + '\n'
    message += '\n**НАВИГАЦИЯ**🧭🗺️\n\n🧑‍💻Для связи:\n\n@Karloff\\_Devices\n+7(903) 322-00-00\n\n@Vladejslavoi\n+7 (928) 654-54-53\n\n\nМы работаем:\nПн-Сб с 10:00 до 21:00\n🗺️Г. Москва,\nметро Багратионовская,\nТЦ «Горбушка ул.Барклая 8,\n123 павильон.\n\nДоставка по Москве🚗\nРегионам России и странам СНГ✈️'
    return normal(message)


def airpods(texts):
    msg = texts['airpods'].split('\n')
    message = ''
    for i in msg:
        if '₽' not in i:
            message += (i) + '\n'
        else:
            message += new_price(i) + '\n'
    message += '\n**НАВИГАЦИЯ**🧭🗺️\n\n🧑‍💻Для связи:\n\n@Karloff\\_Devices\n+7(903) 322-00-00\n\n@Vladejslavoi\n+7 (928) 654-54-53\n\n\nМы работаем:\nПн-Сб с 10:00 до 21:00\n🗺️Г. Москва,\nметро Багратионовская,\nТЦ «Горбушка ул.Барклая 8,\n123 павильон.\n\nДоставка по Москве🚗\nРегионам России и странам СНГ✈️'
    return normal(message)


@bot.message_handler(commands=['help', 'start'])
def start(message):
    # try:
    texts = {}
    try:
        with io.open("example.txt", 'r', encoding='utf-8') as file:
            a = str(file.read())
            a = a.split(' -=-=- ')
            for i in a[:-1]:
                texts[i.split(' +++ ')[0]] = i.split(' +++ ')[1]
    except:
        bot.reply_to(message, 'Поддождите около 1.5 минут и запрос выполнится')
        time.sleep(90)
        bot.reply_to(message, 'Начинается выполнение')
    # try:
    #     texts = get_ms()
    # except:
    #     texts = {'1': 0}
    #     bot.reply_to(message, 'Какая то ошибка')
    try:
        bot.edit_message_text(chat_id='@karloffdevices', message_id=442, parse_mode='MarkdownV2', text=playstation(texts))
        bot.reply_to(message, 'playstation r')
    except:
        bot.reply_to(message, 'playstation o')
    try:
        bot.edit_message_text(chat_id='@karloffdevices', message_id=1145, parse_mode='MarkdownV2', text=dyson(texts))
        bot.reply_to(message, 'dyson r')
    except:
        bot.reply_to(message, 'dyson o')
    try:
        bot.edit_message_text(chat_id='@karloffdevices', message_id=441, parse_mode='MarkdownV2', text=i11_12_13(texts))
        bot.reply_to(message, '11 r')
    except:
        bot.reply_to(message, '11 o')
    try:
        bot.edit_message_text(chat_id='@karloffdevices', message_id=440, parse_mode='MarkdownV2', text=i16(texts))
        bot.reply_to(message, '16 r')
    except:
        bot.reply_to(message, '16 o')
    try:
        bot.edit_message_text(chat_id='@karloffdevices', message_id=439, parse_mode='MarkdownV2', text=i14(texts))
        bot.reply_to(message, '14 r')
    except:
        bot.reply_to(message, '14 o')
    try:
        bot.edit_message_text(chat_id='@karloffdevices', message_id=100, parse_mode='MarkdownV2', text=ipad(texts))
        bot.reply_to(message, 'iPad r')
    except:
        bot.reply_to(message, 'iPad o')
    try:
        bot.edit_message_text(chat_id='@karloffdevices', message_id=625, parse_mode='MarkdownV2', text=macBook(texts)[0])
        bot.edit_message_text(chat_id='@karloffdevices', message_id=626, parse_mode='MarkdownV2', text=macBook(texts)[1])
        bot.reply_to(message, 'macBook r')
    except:
        bot.reply_to(message, 'macBook o')
    try:
        bot.edit_message_text(chat_id='@karloffdevices', message_id=944, parse_mode='MarkdownV2', text=iMac(texts))
        bot.reply_to(message, 'iMac r')
    except:
        bot.reply_to(message, 'iMac o')
    try:
        bot.edit_message_caption(chat_id='@karloffdevices', message_id=69, parse_mode='MarkdownV2', caption=airpods(texts))
        bot.reply_to(message, 'airpods r')
    except:
        bot.reply_to(message, 'airpods o')
    try:
        bot.edit_message_text(chat_id='@karloffdevices', message_id=1582, parse_mode='MarkdownV2', text=watch(texts))
        bot.reply_to(message, 'watch r')
    except:
        bot.reply_to(message, 'watch o')
    # try:
    #     t = android()
    #     bot.edit_message_text(chat_id='@karloffdevices', message_id=127, parse_mode='HTML', text=t[0])
    #     bot.edit_message_text(chat_id='@karloffdevices', message_id=128, parse_mode='HTML', text=t[1])
    #     bot.reply_to(message, 'Android r')
    # except:
    #     bot.reply_to(message, 'Android o')



    try:
        # bot.reply_to(message, i15(texts), parse_mode='MarkdownV2')
        bot.edit_message_text(chat_id='@karloffdevices', message_id=848, parse_mode='MarkdownV2',
                                 text=i15(texts))
        bot.reply_to(message, '15 r')
    except:
        bot.reply_to(message, '15 o')
    # response = get('https://t.me/karloffdevices/777')
    # print(response.text)
    # markup = telebot.util.quick_markup({'Заказать': {'url': 'https://t.me/Vladejslavoi'}})
    # bot.edit_message_reply_markup(chat_id='@karloffdevices', message_id=777, reply_markup=telebot.util.quick_markup({}))
    # print('x')
    # bot.edit_message_text(chat_id='@karloffdevices', message_id=777, parse_mode='HTML', text=i15(), reply_markup=markup)
    # bot.reply_to(message, 'Changed')
    # except:
    #     await context.bot.send_message(chat_id=update.effective_chat.id, text="Error")


# response = get('https://t.me/BigSaleApple/11192')
# print(str(response.text))
def main():
    bot.infinity_polling()

    # i11and12()
    # i13()
    # i14()
    # i15()

    # get()
# i11and12()
if __name__ == '__main__':
    main()




# https://t.me/karloffdevices/368
