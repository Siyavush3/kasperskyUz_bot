import asyncio
import logging
from mysql.connector import connect, Error
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentType
import datetime
import time 
from messages import MESSAGES
from config import BOT_TOKEN, PAYMENTS_PROVIDER_TOKEN, TIME_MACHINE_IMAGE_URL
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import re
logging.basicConfig(format=u'%(filename)+13s [ LINE:%(lineno)-4s] %(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.INFO)


loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode=types.ParseMode.MARKDOWN)
dp = Dispatcher(bot, loop=loop)

button1_ru = KeyboardButton('Купить лицензию🛒')
button2_ru = KeyboardButton('Правила и условия🔍')
button3_ru = KeyboardButton('Мои купленные лицензии🔑')
button4_ru = KeyboardButton('Сменить язык🌐')

button1_uz = KeyboardButton('Litsenziyani sotib olish🛒')
button2_uz = KeyboardButton('Qoidalar va shartlar🔍')
button3_uz = KeyboardButton('Mening sotib olingan litsenziyalarim🔑')
button4_uz = KeyboardButton('Tilni o`zgartirish🌐')


select_ru = KeyboardButton('Русский язык🇷🇺')
select_uz = KeyboardButton('O`zbek tili🇺🇿')

select_lang = ReplyKeyboardMarkup(resize_keyboard=True).add(
    select_uz).add(select_ru)

markup_ru = ReplyKeyboardMarkup(resize_keyboard=True).add(
    button1_ru).add(button2_ru).add(button3_ru).add(button4_ru)

markup_uz = ReplyKeyboardMarkup(resize_keyboard=True).add(
    button1_uz).add(button2_uz).add(button3_uz).add(button4_uz)

# Setup prices
PRICES = [
    types.LabeledPrice(label='Kaspersky Standart', amount=10350000)
    
]

def get_time():
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return timestamp

def create_user(tg_id, tg_phone):
    try:
        if isUserReg(tg_id) == False:
            with connect(host="localhost",user="kasperky_tg_bot",password='D4tas27w@',database="kaspersky_bot_db") as connection:
                print(connection)
                create_user_query = """
                INSERT INTO users
                (tg_id, phone_number)
                VALUES ( %s, %s)
                """
                
                
                with connection.cursor(buffered=True) as cursor:
                    cursor.execute(create_user_query,(tg_id,tg_phone))
                    connection.commit()
    except Error as e:
        print(e)

def getUserPhone(tg_id):

        UserPhone = ' '
        with connect(host="localhost",user="kasperky_tg_bot",password='D4tas27w@',database="kaspersky_bot_db") as connection:
            print(connection)
            get_phone_query = """
            SELECT * FROM users WHERE tg_id = %s
            """
            
            
            with connection.cursor(buffered=True) as cursor:
                cursor.execute(get_phone_query,(tg_id,))
                result = cursor.fetchone()
                UserPhone = result[3]
                connection.commit()
        return UserPhone

def isUserReg(tg_id):

        
        with connect(host="localhost",user="kasperky_tg_bot",password='D4tas27w@',database="kaspersky_bot_db") as connection:
            print(connection)
            get_phone_query = """
            SELECT * FROM users WHERE tg_id = %s
            """
            
            
            with connection.cursor(buffered=True) as cursor:
                cursor.execute(get_phone_query,(tg_id,))
                result = cursor.fetchall()
                connection.commit()
            if(result == []):
                isUserAviable = False
            else:
                isUserAviable = True

        return isUserAviable
    

def checkAviableKeys():
    try:
        with connect(host="localhost",user="kasperky_tg_bot",password='D4tas27w@',database="kaspersky_bot_db") as connection:
            print(connection)
            select_keys_query = """
            SELECT * FROM lic_keys WHERE free = 0
            """
            
            
            with connection.cursor(buffered=True) as cursor:
                cursor.execute(select_keys_query)
                result = cursor.fetchall()
                
                connection.commit()
        if (result == []):
            isAviable = False
        else:
            isAviable = True
    except Error as e:
        print(e)
    return isAviable

def update_key_status(update_lic_key):
    try:
        with connect(host="localhost",user="kasperky_tg_bot",password='D4tas27w@',database="kaspersky_bot_db") as connection:
            print(connection)
            tstmp = get_time()
            update_keys_query = """
            UPDATE lic_keys SET free = %s, key_given = %s WHERE lic_key = %s
            """
            keys = (True, tstmp, update_lic_key)
            
            with connection.cursor(buffered=True) as cursor:
                cursor.execute(update_keys_query, keys)

                connection.commit()
    except Error as e:
        print(e)


def get_lic_key_id(get_lic_key):
    
    with connect(host="localhost",user="kasperky_tg_bot",password='D4tas27w@',database="kaspersky_bot_db") as connection:
        print(connection)
        order_keys_query = """
        SELECT * FROM lic_keys WHERE lic_key = %s
        """
        lic_key_toGet_id = get_lic_key
        id = 0
        with connection.cursor(buffered=True) as cursor:
            cursor.execute(order_keys_query,(lic_key_toGet_id,))
            result = cursor.fetchone()
            id = result[0]
            connection.commit()
    return id


def set_lang(tg_id,languague):
    try:
        with connect(host="localhost",user="kasperky_tg_bot",password='D4tas27w@',database="kaspersky_bot_db") as connection:
            print(connection)
            order_keys_query = """
            UPDATE users SET lang = %s WHERE tg_id = %s
            """
            
            
            with connection.cursor(buffered=True) as cursor:
                cursor.execute(order_keys_query,(languague, tg_id))
                
                
                connection.commit()
    except Error as e:
        print(e)
    

def get_lang(tg_id):
    try:
        with connect(host="localhost",user="kasperky_tg_bot",password='D4tas27w@',database="kaspersky_bot_db") as connection:
            print(connection)
            order_keys_query = """
            SELECT * FROM users WHERE tg_id = %s
            """
            
            
            with connection.cursor(buffered=True) as cursor:
                cursor.execute(order_keys_query,(tg_id,))
                result = cursor.fetchone()
                print(result)
                if result != None:
                    lang = result[2]
                else:
                    lang = 'None'
                connection.commit()
    except Error as e:
        print(e)
    return lang

def get_license_key():
    try:
        with connect(host="localhost",user="kasperky_tg_bot",password='D4tas27w@',database="kaspersky_bot_db") as connection:
            print(connection)
            order_keys_query = """
            SELECT * FROM lic_keys WHERE free = 0
            """
            
            
            with connection.cursor(buffered=True) as cursor:
                cursor.execute(order_keys_query)
                result = cursor.fetchall()
                License_key = result[0][2]
                connection.commit()
    except Error as e:
        print(e)
    return License_key

def list_of_bought_keys(tg_id):
    with connect(host="localhost",user="kasperky_tg_bot",password='D4tas27w@',database="kaspersky_bot_db") as connection:
        print(connection)
        order_keys_query = """
        SELECT `lic_key`, `pay_time` FROM `sold_keys` WHERE `customer_tid` = %s
        """

        with connection.cursor(buffered=True) as cursor:
            cursor.execute(order_keys_query,(tg_id,))
            result = cursor.fetchall()

            connection.commit()
    return result

def make_db_order(purchased_key, customer_name,customer_phone, customer_nickname,customer_tid,pay_summ):
    try:
        with connect(host="localhost",user="kasperky_tg_bot",password='D4tas27w@',database="kaspersky_bot_db") as connection:
            print(connection)
            insert_keys_query = """
            INSERT INTO sold_keys
            (lic_keys_id,customer_name,customer_phone, customer_nikname, customer_tid, order_id, order_type, pay_id,pay_metod ,pay_time, pay_summ,pay_success, lic_key)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            lic_key_id = get_lic_key_id(purchased_key)
            order_id = lic_key_id
            pay_id = order_id
            order_type = 'KIS'
            pay_succes = True
            pay_time = get_time()
            pay_metod = 'ClickUz'
            print(type(customer_name))
            
            
            with connection.cursor(buffered=True) as cursor:
                cursor.execute(insert_keys_query,(lic_key_id,customer_name, customer_phone,customer_nickname, customer_tid,order_id, order_type, pay_id,pay_metod,pay_time,pay_summ, pay_succes,purchased_key))
                connection.commit()
    except Error as e:
        print(e)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    UserReg = isUserReg(message.from_user.id)
    markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton('Регистрация ☎️ / Ro`yxat', request_contact=True)
        )
    if UserReg == False:
        await message.reply('Пройдите регистрацию/ Ro`yxatdan o`ting :', reply_markup=markup_request)
    else:
        userLang = get_lang(message.from_user.id)
        
        if userLang == 'RU':
            await message.reply(MESSAGES['start'], reply_markup=markup_ru)
        else:
            await message.reply(MESSAGES['start_uz'], reply_markup=markup_uz)



@dp.message_handler(commands=['send_news'])
async def process_start_command(message: types.Message):
    if str(message.chat.id) == '1733672501':
        Id = GET_ID()

        for i in range(len(Id)):
            print(str(Id[i][1]))
            print('\n' + str(type(Id[i][2])))
            if Id[i][2] == 'UZ':
                await bot.send_message(str(Id[i][1]), Uz_msg)
            else:
                await bot.send_message(str(Id[i][1]), Ru_msg)






@dp.message_handler(text = 'Tilni o`zgartirish🌐')
async def process_start_command(message: types.Message):
        await message.reply('Выберите язык / Tilni tanlang :', reply_markup=select_lang)

@dp.message_handler(text = 'Сменить язык🌐')
async def process_start_command(message: types.Message):
        await message.reply('Выберите язык / Tilni tanlang :', reply_markup=select_lang) 



@dp.message_handler(text = 'Русский язык🇷🇺')
async def process_start_command(message: types.Message):
    markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Пройти верификацию номера телефона ☎️', request_contact=True)
)
    
    set_lang(message.chat.id,'RU')
    userReg = isUserReg(message.from_user.id)
    if userReg == False:
        await message.reply(MESSAGES['start'], reply_markup=markup_request)
    else:
        await message.reply(MESSAGES['start'], reply_markup=markup_ru)

@dp.message_handler(text = 'O`zbek tili🇺🇿')
async def process_start_command(message: types.Message):
    markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Telefon raqamini tasdiqlang ☎️', request_contact=True)
)
    
    set_lang(message.chat.id,'UZ')
    userReg = isUserReg(message.from_user.id)
    if userReg == False:
        await message.reply(MESSAGES['start_uz'], reply_markup=markup_request)
    else:
        await message.reply(MESSAGES['start_uz'], reply_markup=markup_uz)


@dp.message_handler(text = 'Мои купленные лицензии🔑')
async def process_start_command(message: types.Message):
    
    bought_keys = list_of_bought_keys(message.chat.id)
    if bought_keys == []:
        await bot.send_message(message.chat.id,'У вас нет купленных лицензий, для оформления покупки нажмите на кнопку *Купить лицензию*')
    else:
        await message.reply("Список купленных вами лицензионных ключей Kaspersky Standart", reply_markup=markup_ru)
        for k in bought_keys:

            await bot.send_message(message.chat.id,'Дата покупки ключа: ' + str(k[1]) + '\nКлюч: ' +k[0] )



@dp.message_handler(text = 'Mening sotib olingan litsenziyalarim🔑')
async def process_start_command(message: types.Message):
    
    bought_keys = list_of_bought_keys(message.chat.id)
    print(bought_keys)
    if bought_keys == []:
        await bot.send_message(message.chat.id,'Sizda sotib olingan litsenziyalar yoq, sotib olish uchun *Litsenziyani sotib olish* tugmani bosing')
    else:
        await message.reply("Siz sotib olgan Kasperskiy Standart litsenziya kalitlari ro'yxati", reply_markup=markup_uz)
        for k in bought_keys:

            await bot.send_message(message.chat.id,'Kalitni sotib olish sanasi: ' + str(k[1]) + '\nLitsenziya kaliti: ' +k[0] )




 

    
@dp.message_handler(content_types=['contact'])
async def contact(message):
    markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton('Регистрация ☎️ / Ro`yxat', request_contact=True)
        )
    if message.contact is not None and (message.contact.user_id == message.from_user.id):
        await bot.send_message(message.chat.id, 'Вы успешно отправили свой номер / Siz raqamingizni muvaffaqiyatli yubordingiz')
        await bot.send_message(message.chat.id, 'Выберете язык / Tilni tanlang', reply_markup=select_lang)
            
        phonenumber= str(message.contact.phone_number)
            
        create_user(message.contact.user_id,phonenumber)
    else:
        await message.reply("Это не ваш номер телефона! / Bu sizning telefon raqamingiz emas!",reply_markup=markup_request)
    



@dp.message_handler(text = 'Правила и условия🔍')
async def process_terms_command(message: types.Message):
    await message.reply(MESSAGES['terms'], reply_markup=markup_ru)

@dp.message_handler(text = 'Qoidalar va shartlar🔍')
async def process_terms_command(message: types.Message):
    await message.reply(MESSAGES['terms_uz'], reply_markup=markup_uz)


@dp.message_handler(text = 'Купить лицензию🛒')
async def process_buy_command(message: types.Message):

    if PAYMENTS_PROVIDER_TOKEN.split(':')[1] == 'TEST':
        await bot.send_message(message.chat.id, MESSAGES['pre_buy_demo_alert'])
    AviableKeys = checkAviableKeys()
    UserAviable = isUserReg(message.from_user.id)
    if AviableKeys == True and UserAviable == True:
        await bot.send_invoice(message.chat.id,
                            title=MESSAGES['tm_title'],
                            description=MESSAGES['tm_description'],
                            provider_token=PAYMENTS_PROVIDER_TOKEN,
                            currency='UZS',
                            photo_url=TIME_MACHINE_IMAGE_URL,
                            photo_height=768,  # !=0/None or picture won't be shown
                            photo_width=1221,
                            
                            need_email=False,
                            need_phone_number=False,
                            need_shipping_address=False,
                            is_flexible= False,  # True If you need to set up Shipping Fee
                            prices=PRICES,
                            start_parameter='time-machine-example',
                            payload='some-invoice-payload-for-our-internal-use')
    elif UserAviable == False:
        await bot.send_message(message.chat.id, 'Перед покупкой пройдите регистрацию!')

    elif AviableKeys == False:
        await bot.send_message(message.chat.id, 'Приносим извинения, товар закончился')


@dp.message_handler(text = 'Litsenziyani sotib olish🛒')
async def process_buy_command(message: types.Message):

    if PAYMENTS_PROVIDER_TOKEN.split(':')[1] == 'TEST':
        await bot.send_message(message.chat.id, MESSAGES['pre_buy_demo_alert'])
    AviableKeys = checkAviableKeys()
    UserAviable = isUserReg(message.from_user.id)
    if AviableKeys == True and UserAviable == True:
        await bot.send_invoice(message.chat.id,
                            title=MESSAGES['tm_title_uz'],
                            description=MESSAGES['tm_description_uz'],
                            provider_token=PAYMENTS_PROVIDER_TOKEN,
                            currency='UZS',
                            photo_url=TIME_MACHINE_IMAGE_URL,
                            photo_height=768,  # !=0/None or picture won't be shown
                            photo_width=1221,
                            
                            need_email=False,
                            need_phone_number=True,
                            need_shipping_address=True,
                            is_flexible= False,  # True If you need to set up Shipping Fee
                            prices=PRICES,
                            start_parameter='time-machine-example',
                            payload='some-invoice-payload-for-our-internal-use')
    elif UserAviable == False:
        await bot.send_message(message.chat.id, 'Sotib olishdan oldin ro`yxatdan o`ting!')

    elif AviableKeys == False:
        await bot.send_message(message.chat.id, 'Kechirasiz, mahsulot tugadi')



@dp.shipping_query_handler(lambda query: True)
async def process_shipping_query(shipping_query: types.ShippingQuery):
    print('shipping_query.shipping_address')
    print(shipping_query.shipping_address)



    await bot.answer_shipping_query(
        shipping_query.id,
        ok=True,
        shipping_options=shipping_options
    )


@dp.pre_checkout_query_handler(lambda query: True)
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    print('order_info')
    print(pre_checkout_query.order_info)



    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def process_successful_payment(message: types.Message):

    UserLicKey = get_license_key()
    
    update_key_status(UserLicKey)
    customer_name = message.from_user.first_name
    customer_phone = getUserPhone(message.from_user.id)
    customer_nickname = message.from_user.username
    customer_tid = message.from_user.id
    pay_summ = message.successful_payment.total_amount
    
    make_db_order(UserLicKey,customer_name,customer_phone,customer_nickname,customer_tid, pay_summ)
    UserLang = get_lang(message.from_user.id)
    if UserLang == 'RU':
        await message.reply(MESSAGES['terms'], reply_markup=markup_ru)
        await bot.send_message(
            message.chat.id,
            MESSAGES['successful_payment'].format(
                total_amount=message.successful_payment.total_amount // 100,
                currency=message.successful_payment.currency
            )
        )
        await bot.send_message(message.chat.id ,'Спасибо за покупку! Ваша лицензия Kaspersky Satndart: \n' + str(UserLicKey) + "\n Вам следует активировать его не позже 31.12.2023.")


    else:
        await message.reply(MESSAGES['terms_uz'], reply_markup=markup_ru)
        await bot.send_message(
            message.chat.id,
            MESSAGES['successful_payment_uz'].format(
                total_amount=message.successful_payment.total_amount // 100,
                currency=message.successful_payment.currency
            )
        )
        await bot.send_message(message.chat.id ,'Sotib olganingiz uchun tashakkur! Sizning Kasperskiy Standart litsenziyangiz: \n' + str(UserLicKey) + "\n Siz uni 31.12.2023 dan kechiktirmasdan faollashtirishingiz kerak.")

if __name__ == '__main__':
    executor.start_polling(dp, loop=loop)
