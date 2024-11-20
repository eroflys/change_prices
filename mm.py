# from telegram import Update
#from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
import telebot
from requests import get, post
#from datetime import datetime



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
#     application = ApplicationBuilder().token('tokeb').build()
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

bot = telebot.TeleBot('tokeb')

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
            if i != '.' and len(res) > 0:
                var.append(int(res))
                res = ''
    if len(res) != 0:
        var.append(int(res))
    if len(var) > 0:
        return sorted(var)[0]
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
    else:
        res = str(n)[:2] + '.' + str(n)[2:] + '₽'
    return res


def check_colour(colour, message):
    if len(message.split(colour)) == 1:
        return False
    else:
        return True


def i11and12():
    response = get('https://t.me/BigSaleApple/12116')
    html_format = str(response.text).split('iPhone 11/12/SE')[1].split('">')[0].split('Уценённый товар')[0].split('\n')
    iphones11_64 = {}
    iphones11_128 = {}
    iphones12mini64 = {}
    iphones12mini128 = {}
    iphones12mini256 = {}
    iphones12_64 = {}
    iphones12_128 = {}
    iphones12_256 = {}
    iphones12_pro_128 = {}
    iphones12_pro_256 = {}
    iphones12_pro_max = {}
    for i in html_format:
        if len(i) < 5 or 'RFB' in i or 'rfb' in i.lower() or 'замена' in i.lower() or '🇺🇸' in i or '🇭🇰' in i or '🇨🇳' in i:
            continue
        #12 mini
        if '12 mini 64' in i.lower() or '12  mini 64' in i.lower() or '12 mini  64' in i.lower() or '12  mini  64' in i.lower():
            name = i.split('-')[0]
            price = int(get_prices(i.split('-')[1])) * 1.1
            iphones12mini64[name] = price
        if '12 mini 128' in i.lower() or '12  mini 128' in i.lower() or '12 mini  128' in i.lower() or '12  mini  128' in i.lower():
            name = i.split('-')[0]
            price = int(get_prices(i.split('-')[1])) * 1.1
            iphones12mini128[name] = price
        if '12 mini 256' in i.lower() or '12  mini 256' in i.lower() or '12 mini  256' in i.lower() or '12  mini  256' in i.lower():
            name = i.split('-')[0]
            price = int(get_prices(i.split('-')[1])) * 1.1
            iphones12mini256[name] = price
        #11
        if '11 64' in i.lower() or '11  64' in i:
            name = i.split('-')[0]
            price = int(get_prices(i.split('-')[1])) * 1.1
            iphones11_64[name] = price
        if '11 128' in i.lower() or '11  128' in i:
            name = i.split('-')[0]
            price = int(get_prices(i.split('-')[1])) * 1.1
            iphones11_128[name] = price
        #12
        if '12 64' in i.lower() or '12  64' in i:
            name = i.split('-')[0]
            price = int(get_prices(i.split('-')[1])) * 1.1
            iphones12_64[name] = price
        if '12 128' in i.lower() or '12  128' in i:
            name = i.split('-')[0]
            price = int(get_prices(i.split('-')[1])) * 1.1
            iphones12_128[name] = price
        if '12 256' in i.lower() or '12  256' in i:
            name = i.split('-')[0]
            price = int(get_prices(i.split('-')[1])) * 1.1
            iphones12_256[name] = price
        #12 pro
        if '12 pro 128' in i.lower() or '12 pro  128' in i.lower():
            name = i.split('-')[0]
            price = int(get_prices(i.split('-')[1])) * 1.1
            iphones12_pro_128[name] = price
        if '12 pro 256' in i.lower() or '12 pro  256' in i.lower():
            name = i.split('-')[0]
            price = int(get_prices(i.split('-')[1])) * 1.1
            iphones12_pro_256[name] = price
        #12 pro max
        if '12 pro max 512' in i.lower() or '12  pro max 512' in i.lower() or '12 pro max  512' in i.lower() or '12 pro  max 512' in i.lower():
            name = i.split('-')[0]
            price = int(get_prices(i.split('-')[1])) * 1.1
            iphones12_pro_max[name] = price
    message = '<b><u>ПРАЙС на новые IPhone 11/12</u></b>'
    if len(iphones11_64) != 0 or len(iphones11_128) != 0:
        message += '\n\n<b>IPhone 11 64/128 Gb</b>\n\n'
        for i in iphones11_64:
            message += i + ' - ' + converter(iphones11_64[i]) + '\n'
        message += '\n'
        for i in iphones11_128:
            message += i + ' - ' + converter(iphones11_128[i]) + '\n'
    if len(iphones12mini64) != 0 or len(iphones12mini128) != 0 or len(iphones12mini256) != 0:
        message += '\n\n<b>iPhone 12 Mini 64/128/256</b>\n\n'
        for i in iphones12mini64:
            message += i + ' - ' + converter(iphones12mini64[i]) + '\n'
        message += '\n'
        for i in iphones12mini128:
            message += i + ' - ' + converter(iphones12mini128[i]) + '\n'
        message += '\n'
        for i in iphones12mini256:
            message += i + ' - ' + converter(iphones12mini256[i]) + '\n'
    if len(iphones12_64) != 0 or len(iphones12_128) != 0 or len(iphones12_256) != 0:
        message += '\n\n<b>iPhone 12 64/128/256</b>\n\n'
        for i in iphones12_64:
            message += i + ' - ' + converter(iphones12_64[i]) + '\n'
        message += '\n'
        for i in iphones12_128:
            message += i + ' - ' + converter(iphones12_128[i]) + '\n'
        message += '\n'
        for i in iphones12_256:
            message += i + ' - ' + converter(iphones12_256[i]) + '\n'
    if len(iphones12_pro_128) != 0 or len(iphones12_pro_256) != 0:
        message += '\n\n<b>iPhone 12 Pro 128/256</b>\n\n'
        for i in iphones12_pro_128:
            message += i + ' - ' + converter(iphones12_pro_128[i]) + '\n'
        message += '\n'
        for i in iphones12_pro_256:
            message += i + ' - ' + converter(iphones12_pro_256[i]) + '\n'
    if len(iphones12_pro_max) != 0:
        message += '\n\n<b>iPhone 12 Pro Max 512 Gb</b>\n\n'
        for i in iphones12_pro_max:
            message += i + ' - ' + converter(iphones12_pro_max[i]) + '\n'
    message += '\n<b>НАВИГАЦИЯ</b>🧭🗺️\n\n🧑‍💻Для связи:\n\n@Karloff_Devices\n+7(903) 322-00-00\n\n@Vladejslavoi\n+7 (928) 654-54-53\n\n\nМы работаем:\nПн-Сб с 10:00 до 21:00\n🗺️Г. Москва,\nметро Багратионовская,\nТЦ «Горбушка ул.Барклая 8,\n123 павильон.\n\nДоставка по Москве🚗\nРегионам России и странам СНГ✈️'
    # post('https://api.telegram.org/bot/editMessageText?chat_id=@testchannel1102&message_id=5&parse_mode=HTML&text=' + message)
    # print(message)
    # return message
    # context.bot.editMessageText(chat_id='@karloffdevices', message_id=441, parse_mode='HTML', text=message)
    response = get('https://t.me/karloffdevices/441')
    if del_b_u(message) not in str(response.text).split('meta property="og:description" content="')[1].split('">')[0]:
        return message
        # post('https://api.telegram.org/bot/editMessageText?chat_id=@karloffdevices&message_id=441&parse_mode=HTML&text='+message)
    else:
        return message

def i13():
    response = get('https://t.me/BigSaleApple/12117')
    html_format = str(response.text).split('месяцев - 10.000₽')[1].split('Уценённый товар')[0].split('\n')
    iphones13mini128 = {}
    iphones13mini256 = {}
    iphones13mini512 = {}
    iphones13_128 = {}
    iphones13_256 = {}
    iphones13_512 = {}
    iphones13_pro_max_128 = {}
    iphones13_pro_max_256 = {}
    for i in html_format:
        if len(i) < 5 or 'RFB' in i or 'rfb' in i.lower() or '🇺🇸' in i or '🇭🇰' in i or '🇨🇳' in i:
            continue
        #13mini
        if '-' in i:
            if '13 mini 128' in i.lower() or '13  mini 128' in i.lower() or '13 mini  128' in i.lower() or '13  mini  128' in i.lower():
                name = i.split('-')[0]
                price = int(get_prices(i.split('-')[1])) * 1.1
                iphones13mini128[name] = price
            if '13 mini 256' in i.lower() or '13  mini 256' in i.lower() or '13 mini  256' in i.lower() or '13  mini  256' in i.lower():
                name = i.split('-')[0]
                price = int(get_prices(i.split('-')[1])) * 1.1
                iphones13mini256[name] = price
            if '13 mini 512' in i.lower() or '13  mini 512' in i.lower() or '13 mini  512' in i.lower() or '13  mini  512' in i.lower():
                name = i.split('-')[0]
                price = int(get_prices(i.split('-')[1])) * 1.1
                iphones13mini512[name] = price
            #13
            if '13 128' in i.lower() or '13  128' in i:
                name = i.split('-')[0]
                price = int(get_prices(i.split('-')[1])) * 1.1
                iphones13_128[name] = price
            if '13 256' in i.lower() or '13  256' in i:
                name = i.split('-')[0]
                price = int(get_prices(i.split('-')[1])) * 1.1
                iphones13_256[name] = price
            if '13 512' in i.lower() or '13  512' in i:
                name = i.split('-')[0]
                price = int(get_prices(i.split('-')[1])) * 1.1
                iphones13_512[name] = price
            #13promax
            if '13 pro max 128' in i.lower() or '13  pro max 128' in i.lower() or '13 pro max  128' in i.lower() or '13 pro  max 128' in i.lower():
                name = i.split('-')[0]
                price = int(get_prices(i.split('-')[1])) * 1.1
                iphones13_pro_max_128[name] = price
            if '13 pro max 256' in i.lower() or '13  pro max 256' in i.lower() or '13 pro max  256' in i.lower() or '13 pro  max 256' in i.lower():
                name = i.split('-')[0]
                price = int(get_prices(i.split('-')[1])) * 1.1
                iphones13_pro_max_256[name] = price
    message = '<b><u>ПРАЙС на новые IPhone 13</u></b>'
    if len(iphones13mini128) != 0 or len(iphones13mini256) != 0 or len(iphones13mini512) != 0:
        message += '\n\n<b>IPhone 13 Mini 128/256/512 Gb</b>\n\n'
        for i in iphones13mini128:
            message += i + ' - ' + converter(iphones13mini128[i]) + '\n'
        message += '\n'
        for i in iphones13mini256:
            message += i + ' - ' + converter(iphones13mini256[i]) + '\n'
        message += '\n'
        for i in iphones13mini512:
            message += i + ' - ' + converter(iphones13mini512[i]) + '\n'
    if len(iphones13_128) != 0 or len(iphones13_256) != 0 or len(iphones13_512) != 0:
        message += '\n\n<b>IPhone 13 128/256/512 Gb</b>\n\n'
        for i in iphones13_128:
            message += i + ' - ' + converter(iphones13_128[i]) + '\n'
        message += '\n'
        for i in iphones13_256:
            message += i + ' - ' + converter(iphones13_256[i]) + '\n'
        message += '\n'
        for i in iphones13_512:
            message += i + ' - ' + converter(iphones13_512[i]) + '\n'
    if len(iphones13_pro_max_128) != 0 or len(iphones13_pro_max_256) != 0:
        message += '\n\n<b>IPhone 13 Pro Max 128/256 Gb</b>\n\n'
        for i in iphones13_pro_max_128:
            message += i + ' - ' + converter(iphones13_pro_max_128[i]) + '\n'
        message += '\n'
        for i in iphones13_pro_max_256:
            message += i + ' - ' + converter(iphones13_pro_max_256[i]) + '\n'
    message += '\n<b>НАВИГАЦИЯ</b>🧭🗺️\n\n🧑‍💻Для связи:\n\n@Karloff_Devices\n+7(903) 322-00-00\n\n@Vladejslavoi\n+7 (928) 654-54-53\n\n\nМы работаем:\nПн-Сб с 10:00 до 21:00\n🗺️Г. Москва,\nметро Багратионовская,\nТЦ «Горбушка ул.Барклая 8,\n123 павильон.\n\nДоставка по Москве🚗\nРегионам России и странам СНГ✈️\n\n#IPhone13'
    # post('https://api.telegram.org/bottokeb/editMessageText?chat_id=@testchannel1102&message_id=4&parse_mode=HTML&text=' + message)
    # print(message)
    response = get('https://t.me/karloffdevices/440')
    return message
    # context.bot.editMessageText(chat_id='@karloffdevices', message_id=440, parse_mode='HTML', text=message)
    # response = get('https://t.me/karloffdevices/440')
    # if message not in str(response.text):
    #     post(
    #         'https://api.telegram.org/bottokeb/editMessageText?chat_id=@karloffdevices&message_id=440&parse_mode=HTML&text=' + message)


def i14():
    response = get('https://t.me/BigSaleApple/12118')
    html_format = str(response.text).split('12 месяцев - 10.000')[1].split('Уценённый товар')[0].split('\n')
    iphone14_128 = {}
    iphone14_256 = {}
    iphone14_512 = {}
    iphone14_plus_128 = {}
    iphone14_plus_256 = {}
    iphone14_plus_512 = {}
    iphone14_pro_128 = {}
    iphone14_pro_256 = {}
    iphone14_pro_512 = {}
    iphone14_pro_1tb = {}
    iphone14_pro_max_128 = {}
    iphone14_pro_max_256 = {}
    iphone14_pro_max_512 = {}
    iphone14_pro_max_1tb = {}
    for i in html_format:
        if len(i) < 5 or 'RFB' in i or 'rfb' in i.lower() or '/' in i.lower() or '🇺🇸' in i or '🇭🇰' in i or '🇨🇳' in i:
            continue
        #14
        if '14 128' in i.lower() or '14  128' in i.lower():
            name = i.split('-')[0]
            price = int(get_prices(i.split('-')[1])) * 1.1
            iphone14_128[name] = price
        if '14 256' in i.lower() or '14  256' in i.lower():
            name = i.split('-')[0]
            price = int(get_prices(i.split('-')[1])) * 1.1
            iphone14_256[name] = price
        if '14 512' in i.lower() or '14  512' in i.lower():
            name = i.split('-')[0]
            price = int(get_prices(i.split('-')[1])) * 1.1
            iphone14_512[name] = price
        #14 plus
        if '14 plus 128' in i.lower() or '14  plus 128' in i.lower() or '14 plus  128' in i.lower() or '14  plus  128' in i.lower():
            name = i.split('-')[0]
            price = int(get_prices(i.split('-')[1])) * 1.1
            iphone14_plus_128[name] = price
        if '14 plus 256' in i.lower() or '14  plus 256' in i.lower() or '14 plus  256' in i.lower() or '14  plus  256' in i.lower():
            name = i.split('-')[0]
            price = int(get_prices(i.split('-')[1])) * 1.1
            iphone14_plus_256[name] = price
        if '14 plus 512' in i.lower() or '14  plus 512' in i.lower() or '14 plus  512' in i.lower() or '14  plus  512' in i.lower():
            name = i.split('-')[0]
            price = int(get_prices(i.split('-')[1])) * 1.1
            iphone14_plus_512[name] = price
        #14 pro
        if '14 pro 128' in i.lower() or '14  pro 128' in i.lower() or '14 pro  128' in i.lower() or '14  pro  128' in i.lower():
            name = i.split('-')[0]
            price = int(get_prices(i.split('-')[1])) * 1.1
            iphone14_pro_128[name] = price
        if '14 pro 256' in i.lower() or '14  pro 256' in i.lower() or '14 pro  256' in i.lower() or '14  pro  256' in i.lower():
            name = i.split('-')[0]
            price = int(get_prices(i.split('-')[1])) * 1.1
            iphone14_pro_256[name] = price
        if '14 pro 512' in i.lower() or '14  pro 512' in i.lower() or '14 pro  512' in i.lower() or '14  pro  512' in i.lower():
            name = i.split('-')[0]
            price = int(get_prices(i.split('-')[1])) * 1.1
            iphone14_pro_512[name] = price
        if '14 pro 1tb' in i.lower() or '14  pro 1tb' in i.lower() or '14 pro  1tb' in i.lower() or '14  pro  1tb' in i.lower():
            name = i.split('-')[0]
            price = int(get_prices(i.split('-')[1])) * 1.1
            iphone14_pro_1tb[name] = price
        #14 pro max
        if '14 pro max 128' in i.lower() or '14  pro max 128' in i.lower() or '14 pro max  128' in i.lower() or '14  pro max  128' in i.lower():
            name = i.split('-')[0]
            price = int(get_prices(i.split('-')[1])) * 1.1
            iphone14_pro_max_128[name] = price
        if '14 pro max 256' in i.lower() or '14  pro max 256' in i.lower() or '14 pro max  256' in i.lower() or '14  pro max  256' in i.lower():
            name = i.split('-')[0]
            price = int(get_prices(i.split('-')[1])) * 1.1
            iphone14_pro_max_256[name] = price
        if '14 pro max 512' in i.lower() or '14  pro max 512' in i.lower() or '14 pro max  512' in i.lower() or '14  pro max  512' in i.lower():
            name = i.split('-')[0]
            price = int(get_prices(i.split('-')[1])) * 1.1
            iphone14_pro_max_512[name] = price
        if '14 pro max 1tb' in i.lower() or '14  pro max 1tb' in i.lower() or '14 pro max  1tb' in i.lower() or '14  pro max  1tb' in i.lower():
            name = i.split('-')[0]
            price = int(get_prices(i.split('-')[1])) * 1.1
            iphone14_pro_max_1tb[name] = price
    message = '<b><u>ПРАЙС на новые IPhone 14</u></b>'
    if len(iphone14_128) != 0 or len(iphone14_256) != 0 or len(iphone14_512) != 0:
        message += '\n\n<b>14 128/ 256 /512</b>\n\n'
        for i in iphone14_128:
            message += i + ' - ' + converter(iphone14_128[i]) + '\n'
        message += '\n'
        for i in iphone14_256:
            message += i + ' - ' + converter(iphone14_256[i]) + '\n'
        message += '\n'
        for i in iphone14_512:
            message += i + ' - ' + converter(iphone14_512[i]) + '\n'
    if len(iphone14_plus_128) != 0 or len(iphone14_plus_256) != 0 or len(iphone14_plus_512) != 0:
        message += '\n\n<b>14 Plus 128/ 256 /512</b>\n\n'
        for i in iphone14_plus_128:
            message += i + ' - ' + converter(iphone14_plus_128[i]) + '\n'
        message += '\n'
        for i in iphone14_plus_256:
            message += i + ' - ' + converter(iphone14_plus_256[i]) + '\n'
        message += '\n'
        for i in iphone14_plus_512:
            message += i + ' - ' + converter(iphone14_plus_512[i]) + '\n'
    if len(iphone14_pro_128) != 0 or len(iphone14_pro_256) != 0 or len(iphone14_pro_512) != 0:
        message += '\n\n<b>14 Pro 128/256/512/1tb</b>\n\n'
        for i in iphone14_pro_128:
            message += i + ' - ' + converter(iphone14_pro_128[i]) + '\n'
        message += '\n'
        for i in iphone14_pro_256:
            message += i + ' - ' + converter(iphone14_pro_256[i]) + '\n'
        message += '\n'
        for i in iphone14_pro_512:
            message += i + ' - ' + converter(iphone14_pro_512[i]) + '\n'
        message += '\n'
        for i in iphone14_pro_1tb:
            message += i + ' - ' + converter(iphone14_pro_1tb[i]) + '\n'
    if len(iphone14_pro_max_128) != 0 or len(iphone14_pro_max_256) != 0 or len(iphone14_pro_max_512) != 0:
        message += '\n\n<b>14 PRO MAX 128/256/512/1tb</b>\n\n'
        for i in iphone14_pro_max_128:
            message += i + ' - ' + converter(iphone14_pro_max_128[i]) + '\n'
        message += '\n'
        for i in iphone14_pro_max_256:
            message += i + ' - ' + converter(iphone14_pro_max_256[i]) + '\n'
        message += '\n'
        for i in iphone14_pro_max_512:
            message += i + ' - ' + converter(iphone14_pro_max_512[i]) + '\n'
        message += '\n'
        for i in iphone14_pro_max_1tb:
            message += i + ' - ' + converter(iphone14_pro_max_1tb[i]) + '\n'
    message += '\n\n🧑‍💻Для связи:\n\n@Karloff_Devices\n+7(903) 322-00-00\n\n@Vladejslavoi\n+7 (928) 654-54-53\n\n\nМы работаем:\nПн-Сб с 10:00 до 21:00\n🗺️Г. Москва,\nметро Багратионовская,\nТЦ «Горбушка ул.Барклая 8,\n123 павильон.\n\nДоставка по Москве🚗\nРегионам России и странам СНГ✈️\n\nIPhone14'
    # post('https://api.telegram.org/bottokeb/editMessageText?chat_id=@testchannel1102&message_id=3&parse_mode=HTML&text=' + message)
    return message
    # context.bot.editMessageText(chat_id='@karloffdevices', message_id=439, parse_mode='HTML', text=message)
    # response = get('https://t.me/karloffdevices/439')
    # if message not in str(response.text):
    #     post(
    #         'https://api.telegram.org/bottokeb/editMessageText?chat_id=@karloffdevices&message_id=439&parse_mode=HTML&text=' + message)


def i15():
    response = get('https://t.me/BigSaleApple/12119')
    html_format = str(response.text).split('месяцев - 10.000₽')[1].split('🍎')[0].split('Уценённый товар')[0].split('\n')
    response = get('https://t.me/BigSaleApple/12149')
    html_format1 = str(response.text).split('месяцев - 10.000₽')[1].split('🍎')[0].split('Уценённый товар')[0].split('\n')
    html_format.extend(html_format1)
    iphone15_128 = {}
    iphone15_256 = {}
    iphone15_512 = {}
    iphone15_plus_128 = {}
    iphone15_plus_256 = {}
    iphone15_plus_512 = {}
    iphone15_pro_128 = {}
    iphone15_pro_256 = {}
    iphone15_pro_512 = {}
    iphone15_pro_1tb = {}
    iphone15_pro_max_256 = {}
    iphone15_pro_max_512 = {}
    iphone15_pro_max_1tb = {}
    for i in html_format:
        if len(i) < 5 or 'RFB' in i or 'rfb' in i.lower() or 'актив' in i.lower() or '/' in i.lower() or '🇺🇸' in i or '🇭🇰' in i or '🇨🇳' in i:
            continue
        #15
        if '-' in i:
            if '1' in i.split('-')[1] or '2' in i.split('-')[1] or '3' in i.split('-')[1] or '4' in i.split('-')[1] or '5' in i.split('-')[1] or '6' in i.split('-')[1] or '7' in i.split('-')[1] or '8' in i.split('-')[1] or '9' in i.split('-')[1] or '0' in i.split('-')[1]:
                if '15 128' in i.lower() or '15  128' in i:
                    name = i.split('-')[0]
                    price = int(get_prices(i.split('-')[1])) * 1.1
                    if ch_pr(iphone15_128, name, price):
                        iphone15_128[name] = price
                if '15 256' in i.lower() or '15  256' in i:
                    name = i.split('-')[0]
                    price = int(get_prices(i.split('-')[1])) * 1.1
                    if ch_pr(iphone15_256, name, price):
                        iphone15_256[name] = price
                if '15 512' in i.lower() or '15  512' in i:
                    name = i.split('-')[0]
                    price = int(get_prices(i.split('-')[1])) * 1.1
                    if ch_pr(iphone15_512, name, price):
                        iphone15_512[name] = price
                #15 plus
                if '15 plus 128' in i.lower():
                    name = i.split('-')[0]
                    price = int(get_prices(i.split('-')[1])) * 1.1
                    if ch_pr(iphone15_plus_128, name, price):
                        iphone15_plus_128[name] = price
                if '15 plus 256' in i.lower():
                    name = i.split('-')[0]
                    price = int(get_prices(i.split('-')[1])) * 1.1
                    if ch_pr(iphone15_plus_256, name, price):
                        iphone15_plus_256[name] = price
                if '15 plus 512' in i.lower():
                    name = i.split('-')[0]
                    price = int(get_prices(i.split('-')[1])) * 1.1
                    if ch_pr(iphone15_plus_512, name, price):
                        iphone15_plus_512[name] = price
                #15 pro
                if '15 pro 128' in i.lower():
                    name = i.split('-')[0]
                    price = int(get_prices(i.split('-')[1])) * 1.1
                    if ch_pr(iphone15_pro_128, name, price):
                        iphone15_pro_128[name] = price
                if '15 pro 256' in i.lower():
                    name = i.split('-')[0]
                    price = int(get_prices(i.split('-')[1])) * 1.1
                    if ch_pr(iphone15_pro_256, name, price):
                        iphone15_pro_256[name] = price
                if '15 pro 512' in i.lower():
                    name = i.split('-')[0]
                    price = int(get_prices(i.split('-')[1])) * 1.1
                    if ch_pr(iphone15_pro_512, name, price):
                        iphone15_pro_512[name] = price
                if '15 pro 1tb' in i.lower():
                    name = i.split('-')[0]
                    price = int(get_prices(i.split('-')[1])) * 1.1
                    if ch_pr(iphone15_pro_1tb, name, price):
                        iphone15_pro_1tb[name] = price
                #15 pro max
                if '15 pro max 256' in i.lower():
                    name = i.split('-')[0]
                    price = int(get_prices(i.split('-')[1])) * 1.1
                    if ch_pr(iphone15_pro_max_256, name, price):
                        iphone15_pro_max_256[name] = price
                if '15 pro max 512' in i.lower():
                    name = i.split('-')[0]
                    price = int(get_prices(i.split('-')[1])) * 1.1
                    if ch_pr(iphone15_pro_max_512, name, price):
                        iphone15_pro_max_512[name] = price
                if '15 pro max 1tb' in i.lower():
                    name = i.split('-')[0]
                    price = int(get_prices(i.split('-')[1])) * 1.1
                    if ch_pr(iphone15_pro_max_1tb, name, price):
                        iphone15_pro_max_1tb[name] = price
    message = '<b><u>ПРАЙС на новые IPhone 15</u></b>'
    if len(iphone15_128) != 0 or len(iphone15_256) != 0 or len(iphone15_512) != 0:
        message += '\n\n              <b>15 128/ 256 /512</b>\n\n'
        for i in iphone15_128:
            message += i + ' - ' + converter(iphone15_128[i]) + '\n'
        message += '\n'
        for i in iphone15_256:
            message += i + ' - ' + converter(iphone15_256[i]) + '\n'
        message += '\n'
        for i in iphone15_512:
            message += i + ' - ' + converter(iphone15_512[i]) + '\n'
    if len(iphone15_plus_128) != 0 or len(iphone15_plus_256) != 0 or len(iphone15_plus_512) != 0:
        message += '\n'
        for i in iphone15_plus_128:
            message += i + ' - ' + converter(iphone15_plus_128[i]) + '\n'
        message += '\n'
        for i in iphone15_plus_256:
            message += i + ' - ' + converter(iphone15_plus_256[i]) + '\n'
        message += '\n'
        for i in iphone15_plus_512:
            message += i + ' - ' + converter(iphone15_plus_512[i]) + '\n'
    if len(iphone15_pro_128) != 0 or len(iphone15_pro_256) != 0 or len(iphone15_pro_512) != 0 or len(iphone15_pro_1tb) != 0:
        message += '\n\n              <b>15 Pro 128/ 256/ 512/ 1Tb</b>\n\n'
        for i in iphone15_pro_128:
            message += i + ' - ' + converter(iphone15_pro_128[i]) + '\n'
        message += '\n'
        for i in iphone15_pro_256:
            message += i + ' - ' + converter(iphone15_pro_256[i]) + '\n'
        message += '\n'
        for i in iphone15_pro_512:
            message += i + ' - ' + converter(iphone15_pro_512[i]) + '\n'
        message += '\n'
        for i in iphone15_pro_1tb:
            message += i + ' - ' + converter(iphone15_pro_1tb[i]) + '\n'
    if len(iphone15_pro_max_256) != 0 or len(iphone15_pro_max_512) != 0 or len(iphone15_pro_max_1tb) != 0:
        message += '\n\n              <b>15 Pro Max 256/ 512/ 1TB</b>\n\n'
        for i in iphone15_pro_max_256:
            message += i + ' - ' + converter(iphone15_pro_max_256[i]) + '\n'
        message += '\n'
        for i in iphone15_pro_max_512:
            message += i + ' - ' + converter(iphone15_pro_max_512[i]) + '\n'
        message += '\n'
        for i in iphone15_pro_max_1tb:
            message += i + ' - ' + converter(iphone15_pro_max_1tb[i]) + '\n'
    message += '''

 15      
Чехлы 

iPhone 15 Pro Max Silicone Case
Clear Case 9.000
Black 8.500
Clay 8.500
Cypress 8.500
Guava 8.500
Light Pink 8.500
Orange Sorbet 8.500
Storm Blue 8.500
Winter Blue 8.500

iPhone 15 Pro  Silicone Case
Black -9.000
Cypress 8.500
iPhone 15 Pro  Guava 8.500
iPhone 15 Pro Light Pink 8.500
iPhone 15 Pro Orange Sorbet 8.500
iPhone 15 Pro Storm Blue 8.500
iPhone 15 Pro Winter Blue  8.500

Wallet with MagSafe
Black /Evergreen /Pacific Blue /Taupe -9.000

🧑‍💻Для связи:

@Karloff_Devices
+7(903) 322-00-00

@Vladejslavoi
+7 (928) 654-54-53

Мы работаем:
Пн-Сб с 10:00 до 21:00
🗺️Г. Москва, 
метро Багратионовская, 
ТЦ «Горбушка ул.Барклая 8, 
123 павильон.

Доставка по Москве 🚗
Регионам России и странам СНГ✈️

#iphone15'''
    # post('https://api.telegram.org/bottokeb/editMessageText?chat_id=@testchannel1102&message_id=2&parse_mode=HTML&text=' + message)

    # response = get('https://t.me/karloffdevices/777')
    return message
    # if message not in str(response.text):
    #     print(message)
    #     post(
    #         'https://api.telegram.org/bottokeb/editMessageText?chat_id=@karloffdevices&message_id=777&parse_mode=HTML&text=' + message)







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

def iMac():
    response = get('https://t.me/BigSaleApple/11186')
    html_format = str(response.text).split('+12 месяцев')[1].split('\n')
    iMacM1 = {}
    iMacM3 = {}
    for i in html_format:
        if 'imac' in i.lower() and 'm1' in i.lower():
            name = find_price(i)[0]
            price = int(find_price(i)[1]) * 1.1
            if ch_pr(iMacM1, name, price) and price > 1000:
                iMacM1[name] = price

        if 'imac' in i.lower() and 'm3' in i.lower():
            name = find_price(i)[0]
            price = int(find_price(i)[1]) * 1.1
            if ch_pr(iMacM3, name, price) and price > 1000:
                iMacM3[name] = price
    message = '<b><u>Прайс на новые iMac</u></b>\n'
    if len(iMacM1) != 0:
        message += '\n<b>iMac M1</b>\n\n'
        for i in iMacM1:
            message += i + converter(iMacM1[i]) + '\n\n'
    if len(iMacM3) != 0:
        message += '\n<b>iMac M3</b>\n\n'
        for i in iMacM3:
            message += i + converter(iMacM3[i]) + '\n\n'
    message += '''@Karloff_Devices
+7 (903) 322-00-00

@Vladejslavoi  
+7 (928) 654-54-53 

🕰️Пн-Сб с 10:00 до 21:00
Мы находимся по адресу: г Москва, ул. Барклая 8, 123 павильон.🏙️'''
    return message







def macBook():
    response = get('https://t.me/BigSaleApple/11384')
    response1 = get('https://t.me/BigSaleApple/11510')
    html_format = str(response.text).split('+12 месяцев')[1].split('\n') + str(response1.text).split('+12 месяцев')[1].split('\n')
    mac_mini = {}
    mb_air_m1_13_2020 = {}
    mb_air_m2_13_2022 = {}
    mb_air_m3_13_2024 = {}
    mb_air_m2_15_2023 = {}
    mb_air_m3_15_2024 = {}
    mb_pro_m2_13_2022 = {}
    mb_pro_m2_14_2022 = {}
    mb_pro_m3_14_2023 = {}
    mb_pro_m1_16_20212 = {}
    mb_pro_m2_16_2022 = {}
    mb_pro_m3_16_2023 = {}
    for i in html_format:
        if 'актив' not in i.lower() and 'rfb' not in i.lower():
            if 'mac mini' in i.lower():
                price = int(find_price(i)[1]) * 1.1
                if price > 1000:
                    mac_mini[find_price(i)[0]] = price
            if 'air' in i.lower() and '13' in i.lower() and 'm1' in i.lower():
                price = int(find_price(i)[1]) * 1.1
                if price > 1000:
                    mb_air_m1_13_2020[find_price(i)[0]] = price
            if 'air' in i.lower() and '13' in i.lower() and 'm2' in i.lower():
                price = int(find_price(i)[1]) * 1.1
                if price > 1000:
                    mb_air_m2_13_2022[find_price(i)[0]] = price
            if 'air' in i.lower() and '13' in i.lower() and 'm3' in i.lower():
                price = int(find_price(i)[1]) * 1.1
                if price > 1000:
                    mb_air_m3_13_2024[find_price(i)[0]] = price
            if 'air' in i.lower() and '15' in i.lower() and 'm2' in i.lower():
                price = int(find_price(i)[1]) * 1.1
                if price > 1000:
                    mb_air_m2_15_2023[find_price(i)[0]] = price
            if 'air' in i.lower() and '15' in i.lower() and 'm3' in i.lower():
                price = int(find_price(i)[1]) * 1.1
                if price > 1000:
                    mb_air_m3_15_2024[find_price(i)[0]] = price
            if 'pro' in i.lower() and '13' in i.lower() and 'm2' in i.lower():
                price = int(find_price(i)[1]) * 1.1
                if price > 1000:
                    mb_pro_m2_13_2022[find_price(i)[0]] = price
            if 'pro' in i.lower() and '14' in i.lower() and 'm2' in i.lower():
                price = int(find_price(i)[1]) * 1.1
                if price > 1000:
                    mb_pro_m2_14_2022[find_price(i)[0]] = price
            if 'pro' in i.lower() and '14' in i.lower() and 'm3' in i.lower():
                price = int(find_price(i)[1]) * 1.1
                if price > 1000:
                    mb_pro_m3_14_2023[find_price(i)[0]] = price
            if 'pro' in i.lower() and '16' in i.lower() and 'm1' in i.lower():
                price = int(find_price(i)[1]) * 1.1
                if price > 1000:
                    mb_pro_m1_16_20212[find_price(i)[0]] = price
            if 'pro' in i.lower() and '16' in i.lower() and 'm2' in i.lower():
                price = int(find_price(i)[1]) * 1.1
                if price > 1000:
                    mb_pro_m2_16_2022[find_price(i)[0]] = price
            if 'pro' in i.lower() and '16' in i.lower() and 'm3' in i.lower():
                price = int(find_price(i)[1]) * 1.1
                if price > 1000:
                    mb_pro_m3_16_2023[find_price(i)[0]] = price
    message = '<b><u>ПРАЙС на новые MacBook</u></b>'
    if len(mac_mini) != 0:
        message += '\n<b>Mac Mini</b>\n\n'
        for i in mac_mini:
            message += i + converter(mac_mini[i]) + '\n'
    if len(mb_air_m1_13_2020) != 0:
        message += '\n<b>MacBook Air М1 13 (2020)</b>\n\n'
        for i in mb_air_m1_13_2020:
            message += i + converter(mb_air_m1_13_2020[i]) + '\n'
    if len(mb_air_m2_13_2022) != 0:
        message += '\n<b>MacBook Air М2 13 (2022)</b>\n\n'
        for i in mb_air_m2_13_2022:
            message += i + converter(mb_air_m2_13_2022[i]) + '\n'
    if len(mb_air_m3_13_2024) != 0:
        message += '\n<b>MacBook Air М3 13 (2024)</b>\n\n'
        for i in mb_air_m3_13_2024:
            message += i + converter(mb_air_m3_13_2024[i]) + '\n'
    if len(mb_air_m2_15_2023) != 0:
        message += '\n<b>MacBook Air М2 15 (2023)</b>\n\n'
        for i in mb_air_m2_15_2023:
            message += i + converter(mb_air_m2_15_2023[i]) + '\n'
    if len(mb_air_m3_15_2024) != 0:
        message += '\n<b>MacBook Air М3 15 (2024)</b>\n\n'
        for i in mb_air_m3_15_2024:
            message += i + converter(mb_air_m3_15_2024[i]) + '\n'
    message += '\n Продолжение в следующем сообщении>>>'
    message1 = ''
    if len(mb_pro_m2_13_2022) != 0:
        message1 += '\n<b>MacBook Pro М2 13 (2022)</b>\n\n'
        for i in mb_pro_m2_13_2022:
            message1 += i + converter(mb_pro_m2_13_2022[i]) + '\n'
    if len(mb_pro_m2_14_2022) != 0:
        message1 += '\n<b>MacBook Pro М2 14 (2022)</b>\n\n'
        for i in mb_pro_m2_14_2022:
            message1 += i + converter(mb_pro_m2_14_2022[i]) + '\n'
    if len(mb_pro_m3_14_2023) != 0:
        message1 += '\n<b>MacBook Pro М3 14 (2023)</b>\n\n'
        for i in mb_pro_m3_14_2023:
            message1 += i + converter(mb_pro_m3_14_2023[i]) + '\n'
    if len(mb_pro_m1_16_20212) != 0:
        message1 += '\n<b>MacBook Pro М1 16 (2021 - 2022)</b>\n\n'
        for i in mb_pro_m1_16_20212:
            message1 += i + converter(mb_pro_m1_16_20212[i]) + '\n'
    if len(mb_pro_m2_16_2022) != 0:
        message1 += '\n<b>MacBook Pro М2 16 (2022)</b>\n\n'
        for i in mb_pro_m2_16_2022:
            message1 += i + converter(mb_pro_m2_16_2022[i]) + '\n'
    if len(mb_pro_m3_16_2023) != 0:
        message1 += '\n<b>MacBook Pro М3 16 (2023)</b>\n\n'
        for i in mb_pro_m3_16_2023:
            message1 += i + converter(mb_pro_m3_16_2023[i]) + '\n'
    message1 += '''По вопросам и заказам пишите:

@Karloff_Devices
+7 (903) 322-00-00

@Vladejslavoi
+7 (928) 654-54-53

Пн-Сб с 10:00 до 21:00
Мы находимся по адресу: г Москва, ул. Барклая 8, 123 павильон.'''
    # print(message)
    # print(len(message))
    return [message, message1]


def android():
    response = get('https://t.me/BigSaleApple/10982')
    response1 = get('https://t.me/BigSaleApple/10983')
    html_format = str(response.text).split('месяцев  - 8.000')[1].split('\n') + str(response1.text).split('Гарантия 14 дней со дня покупки')[1].split('\n')
    google = {}
    samsung = {}
    samsung_tab = {}
    poco = {}
    xiaomi = {}
    headphones = {}
    watch = {}
    for i in html_format:
        # print(i)
        if 'watch' in i.lower() or 'amazfit' in i.lower():
            print(i)
            price = int(find_price(i)[1]) * 1.1
            if price > 1000:
                watch[find_price(i)[0]] = price
        if 'buds' in i.lower() or 'wireless' in i.lower() or 'ear' in i.lower() or 'tws' in i.lower() or 'soundcore' in i.lower() or 'sony wh' in i.lower():
            price = int(find_price(i)[1]) * 1.1
            print(find_price(i)[1], find_price(i)[0], 'z v o')
            if price > 1000:
                headphones[find_price(i)[0]] = price
        if 'pixel' in i.lower():
            price = int(find_price(i)[1]) * 1.1
            if price > 1000:
                google[find_price(i)[0]] = price
        if 'pixel' in i.lower() or 'a15' in i.lower() or 'a25' in i.lower() or 'a35' in i.lower() or 'a54' in i.lower() or 's23' in i.lower() or 'a55' in i.lower() or 's24' in i.lower() or 'flip' in i.lower():
            price = int(find_price(i)[1]) * 1.1
            if price > 1000:
                samsung[find_price(i)[0]] = price
        if 'tab' in i.lower():
            price = int(find_price(i)[1]) * 1.1
            if price > 1000:
                samsung_tab[find_price(i)[0]] = price
        if 'poco' in i.lower():
            price = int(find_price(i)[1]) * 1.1
            if price > 1000:
                poco[find_price(i)[0]] = price
        if 'note' in i.lower() or 'mi' in i.lower():
            price = int(find_price(i)[1]) * 1.1
            if price > 1000:
                xiaomi[find_price(i)[0]] = price

    message1 = '''<b><u>Представляем вам большой ассортимент техники ANDROID</u></b>

Мы не вписали все цвета и модели, по этому по конкретной модели можете уточнять:
@Karloff_Devices_manager'''
    if len(google) != 0:
        message1 += '\n<b>Google Pixel</b>\n\n'
        for i in google:
            message1 += i + converter(google[i]) + '\n'
    if len(samsung) != 0:
        message1 += '\n<b>Samsung</b>\n\n'
        for i in samsung:
            message1 += i + converter(samsung[i]) + '\n'
    if len(poco) != 0:
        message1 += '\n<b>Poco</b>\n\n'
        for i in poco:
            message1 += i + converter(poco[i]) + '\n'
    if len(xiaomi) != 0:
        message1 += '\n<b>Xiaomi</b>\n\n'
        for i in xiaomi:
            message1 += i + converter(xiaomi[i]) + '\n'
    message1 += '\nПродолжение в следующем сообщении>>>'
    message = ''
    if len(samsung_tab) != 0:
        message += '\n<b>Samsung Tab</b>\n\n'
        for i in samsung_tab:
            message += i + converter(samsung_tab[i]) + '\n'
    if len(watch) != 0:
        message += '\n<b>Часы</b>\n\n'
        for i in watch:
            message += i + converter(watch[i]) + '\n'
    if len(headphones) != 0:
        message += '\n<b>Наушники</b>\n\n'
        for i in headphones:
            message += i + converter(headphones[i]) + '\n'
    message += '''Для заказа и по вопросам пишите
@karloff_Devices_manager 
Whatsapp 
https://wa.me/79098440000

Доставка по Москве 
Регионам России и странам СНГ

Самовывоз: Москва, ул.Барклая 8, 123 павильон

#Android'''
    # print(message1, message)
    return [message1, message]


def ipad():
    response = get('https://t.me/BigSaleApple/11199')
    response1 = get('https://t.me/BigSaleApple/11200')
    html_format = str(response.text).split('Гарантия 14 дней со дня покупки')[1].split('\n') + \
                  str(response1.text).split('Гарантия 14 дней со дня покупки')[1].split('\n')
    air_11_2024 = {}
    air_13_2024 = {}
    pro_11_2024 = {}
    pro_13_2024 = {}
    ipad_9 = {}
    mini_6 = {}
    ipad_10 = {}
    air_5 = {}
    pro_11_m2 = {}
    pro_12_m2 = {}
    keyboard = {}
    pencil = {}
    for i in html_format:
        if 'rfb' not in i.lower():
            if 'air' in i.lower() and '11' in i and '2024' in i:
                price = int(find_price(i)[1]) * 1.1
                if price > 1000:
                    air_11_2024[find_price(i)[0]] = price
            if 'air' in i.lower() and '13' in i and '2024' in i:
                price = int(find_price(i)[1]) * 1.1
                if price > 1000:
                    air_13_2024[find_price(i)[0]] = price
            if 'pro' in i.lower() and '11' in i and '2024' in i:
                price = int(find_price(i)[1]) * 1.1
                if price > 1000:
                    pro_11_2024[find_price(i)[0]] = price
            if 'pro' in i.lower() and '13' in i and '2024' in i:
                price = int(find_price(i)[1]) * 1.1
                if price > 1000:
                    pro_13_2024[find_price(i)[0]] = price
            if 'ipad 9' in i.lower():
                price = int(find_price(i)[1]) * 1.1
                if price > 1000:
                    ipad_9[find_price(i)[0]] = price
            if 'mini 6' in i.lower():
                price = int(find_price(i)[1]) * 1.1
                if price > 1000:
                    mini_6[find_price(i)[0]] = price
            if 'ipad 10' in i.lower():
                price = int(find_price(i)[1]) * 1.1
                if price > 1000:
                    ipad_10[find_price(i)[0]] = price
            if 'air 5' in i.lower():
                price = int(find_price(i)[1]) * 1.1
                if price > 1000:
                    air_5[find_price(i)[0]] = price
            if 'pro' in i.lower() and '11' in i and 'm2' in i.lower():
                price = int(find_price(i)[1]) * 1.1
                if price > 1000:
                    pro_11_m2[find_price(i)[0]] = price
            if 'pro' in i.lower() and '12.9' in i and 'm2' in i.lower():
                price = int(find_price(i)[1]) * 1.1
                if price > 1000:
                    pro_12_m2[find_price(i)[0]] = price
            if 'keyboard' in i.lower():
                price = int(find_price(i)[1]) * 1.1
                if price > 1000:
                    keyboard[find_price(i)[0]] = price
            if 'pencil' in i.lower():
                price = int(find_price(i)[1]) * 1.1
                if price > 1000:
                    pencil[find_price(i)[0]] = price
    message = '<b><u>Прайс на новые iPad</u></b>\n'
    if len(pencil) != 0:
        message += '\n'
        for i in pencil:
            message += i + converter(pencil[i]) + '\n'
    if len(keyboard) != 0:
        message += '\n'
        for i in keyboard:
            message += i + converter(keyboard[i]) + '\n'
    if len(air_11_2024) != 0:
        message += '\n<b>iPad air 11" 2024</b>\n\n'
        for i in air_11_2024:
            message += i + converter(air_11_2024[i]) + '\n'
    if len(air_13_2024) != 0:
        message += '\n<b>iPad air 13" 2024</b>\n\n'
        for i in air_13_2024:
            message += i + converter(air_13_2024[i]) + '\n'
    if len(pro_11_2024) != 0:
        message += '\n<b>iPad pro 11" 2024</b>\n\n'
        for i in pro_11_2024:
            message += i + converter(pro_11_2024[i]) + '\n'
    if len(pro_13_2024) != 0:
        message += '\n<b>iPad pro 13" 2024</b>\n\n'
        for i in pro_13_2024:
            message += i + converter(pro_13_2024[i]) + '\n'
    message += 'Продолжение в следующем сообщении>>>'
    message1 = ''
    if len(ipad_9) != 0:
        message1 += '\n<b>iPad 9</b>\n\n'
        for i in ipad_9:
            message1 += i + converter(ipad_9[i]) + '\n'
    if len(ipad_10) != 0:
        message1 += '\n<b>iPad 10</b>\n\n'
        for i in ipad_10:
            message1 += i + converter(ipad_10[i]) + '\n'
    if len(mini_6) != 0:
        message1 += '\n<b>iPad mini 6</b>\n\n'
        for i in mini_6:
            message1 += i + converter(mini_6[i]) + '\n'
    if len(air_5) != 0:
        message1 += '\n<b>iPad air 5</b>\n\n'
        for i in air_5:
            message1 += i + converter(air_5[i]) + '\n'
    if len(pro_11_m2) != 0:
        message1 += '\n<b>iPad pro 11" M2</b>\n\n'
        for i in pro_11_m2:
            message1 += i + converter(pro_11_m2[i]) + '\n'
    if len(pro_12_m2) != 0:
        message1 += '\n<b>iPad pro 12.9" M2</b>\n\n'
        for i in pro_12_m2:
            message1 += i + converter(pro_12_m2[i]) + '\n'
    message1 += '''#Ipad

🧑‍💻Для связи:

@Karloff_Devices
+7(903) 322-00-00

@Vladejslavoi
+7 (928) 654-54-53'''
    return [message, message1]


def airpods():
    response = get('https://t.me/BigSaleApple/11198')
    html_format = str(response.text).split('og:description')[1].split('\n')
    gopro = {}
    airpods = {}
    airpods_max = {}
    airpods2_sep = {}
    airpods3_sep = {}
    airpodsp_sep = {}
    apltv = {}
    magic_mouse = {}
    airtag = {}
    cabels = {}
    for i in html_format:
        if 'gopro' in i.lower():
            price = int(find_price(i)[1]) * 1.1
            if price > 1000:
                gopro[find_price(i)[0]] = price
        if 'airpods' in i.lower() and 'max' in i.lower() and 'box' not in i.lower() and 'ухо' not in i.lower():
            price = int(find_price(i)[1]) * 1.1
            if price > 1000:
                airpods_max[find_price(i)[0]] = price
        if 'airpods' in i.lower() and 'pro' not in i.lower() and 'box' not in i.lower() and 'ухо' not in i.lower():
            price = int(find_price(i)[1]) * 1.1
            if price > 1000:
                airpods[find_price(i)[0]] = price
        if 'airpods 2' in i.lower() and ('box' in i.lower() or 'ухо' in i.lower()):
            price = int(find_price(i)[1]) * 1.1
            if price > 1000:
                airpods2_sep[find_price(i)[0]] = price
        if 'airpods 3' in i.lower() and ('box' in i.lower() or 'ухо' in i.lower()):
            price = int(find_price(i)[1]) * 1.1
            if price > 1000:
                airpods3_sep[find_price(i)[0]] = price
        if 'airpods pro' in i.lower() and ('box' in i.lower() or 'ухо' in i.lower()):
            price = int(find_price(i)[1]) * 1.1
            if price > 1000:
                airpodsp_sep[find_price(i)[0]] = price
        if 'apple' in i.lower() and 'tv' in i.lower():
            price = int(find_price(i)[1]) * 1.1
            if price > 1000:
                apltv[find_price(i)[0]] = price
        if ('magic' in i.lower() and 'mouse' in i.lower()) or ('trackpad' in i.lower()):
            price = int(find_price(i)[1]) * 1.1
            if price > 1000:
                magic_mouse[find_price(i)[0]] = price
        if 'airtag' in i.lower():
            price = int(find_price(i)[1]) * 1.1
            if price > 1000:
                airtag[find_price(i)[0]] = price
        if 'magsafe' in i.lower() or 'charger' in i.lower() or 'кабель' in i.lower():
            price = int(find_price(i)[1]) * 1.1
            if price > 1000:
                cabels[find_price(i)[0]] = price
    message = '''🎧 Apple Airpods  🎧
━─━─━─━─━─
'''
    if len(airpods) != 0:
        message += '\n <b>AirPods</b> \n\n'
        for i in airpods:
            message += i + converter(airpods[i]) + '\n'
    if len(airpods_max) != 0:
        message += '\n <b>AirPods Max</b> \n\n'
        for i in airpods_max:
            message += i + converter(airpods_max[i]) + '\n'
    message += '\n <b>Airpods по отдельности!</b>\n'
    if len(airpods2_sep) != 0:
        message += '\n'
        for i in airpods2_sep:
            message += i + converter(airpods2_sep[i]) + '\n'
    if len(airpods3_sep) != 0:
        message += '\n'
        for i in airpods3_sep:
            message += i + converter(airpods3_sep[i]) + '\n'
    if len(airpodsp_sep) != 0:
        message += '\n'
        for i in airpodsp_sep:
            message += i + converter(airpodsp_sep[i]) + '\n'
    # if len(apltv) != 0:
    #     message += '\n'
    #     for i in apltv:
    #         message += i + converter(apltv[i]) + '\n'
    # if len(magic_mouse) != 0:
    #     message += '\n'
    #     for i in magic_mouse:
    #         message += i + converter(magic_mouse[i]) + '\n'
    # if len(airtag) != 0:
    #     message += '\n'
    #     for i in airtag:
    #         message += i + converter(airtag[i]) + '\n'
    # if len(cabels) != 0:
    #     message += '\n'
    #     for i in cabels:
    #         message += i + converter(cabels[i]) + '\n'
    # if len(gopro) != 0:
    #     message += '\n <b>GoPro</b>\n\n'
    #     for i in gopro:
    #         message += i + converter(gopro[i]) + '\n'
    message += '''
🧑‍💻Для связи:

@Karloff_Devices
+7(903) 322-00-00

@Vladejslavoi
+7 (928) 654-54-53'''
    return message


@bot.message_handler(commands=['help', 'start'])
def start(message):
    # try:

    try:
        bot.edit_message_text(chat_id='@karloffdevices', message_id=441, parse_mode='HTML', text=i11and12())
        bot.reply_to(message, '11 r')
    except:
        bot.reply_to(message, '11 o')
    try:
        bot.edit_message_text(chat_id='@karloffdevices', message_id=440, parse_mode='HTML', text=i13())
        bot.reply_to(message, '13 r')
    except:
        bot.reply_to(message, '13 o')
    try:
        bot.edit_message_text(chat_id='@karloffdevices', message_id=439, parse_mode='HTML', text=i14())
        bot.reply_to(message, '14 r')
    except:
        bot.reply_to(message, '14 o')
    try:
        t = ipad()
        bot.edit_message_text(chat_id='@karloffdevices', message_id=100, parse_mode='HTML', text=t[0])
        bot.edit_message_text(chat_id='@karloffdevices', message_id=101, parse_mode='HTML', text=t[1])
        bot.reply_to(message, 'iPad r')
    except:
        bot.reply_to(message, 'iPad o')
    try:
        t = macBook()
        bot.edit_message_text(chat_id='@karloffdevices', message_id=625, parse_mode='HTML', text=t[0])
        bot.edit_message_text(chat_id='@karloffdevices', message_id=626, parse_mode='HTML', text=t[1])
        bot.reply_to(message, 'macBook r')
    except:
        bot.reply_to(message, 'macBook o')
    try:
        bot.edit_message_text(chat_id='@karloffdevices', message_id=944, parse_mode='HTML', text=iMac())
        bot.reply_to(message, 'iMac r')
    except:
        bot.reply_to(message, 'iMac o')
    try:
        bot.edit_message_caption(chat_id='@karloffdevices', message_id=69, parse_mode='HTML', caption=airpods())
        bot.reply_to(message, 'airpods r')
    except:
        bot.reply_to(message, 'airpods o')

    try:
        t = android()
        bot.edit_message_text(chat_id='@karloffdevices', message_id=127, parse_mode='HTML', text=t[0])
        bot.edit_message_text(chat_id='@karloffdevices', message_id=128, parse_mode='HTML', text=t[1])
        bot.reply_to(message, 'Android r')
    except:
        bot.reply_to(message, 'Android o')



    try:
        bot.reply_to(message, i15(), parse_mode='HTML')
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
