from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from mysql.connector import connect, Error
import asyncio

from aiogram import Bot, Dispatcher, executor, types


bot = Bot(token='5213212941:AAHz33k1F8fdPJ-sLcxviZUn7yVJUkjK198')
dp = Dispatcher(bot)

def read_var():
    with open("num.txt",'r+') as file:

        num = int(file.readlines()[0])
        
        file.close()


    return num

def change_var():
    with open("num.txt",'r+') as file:
        write_num = read_var() + 1
        file.truncate(0)
        
        file.write(str(write_num))
        file.close()

def check_keys():
    UserPhone = ' '
    with connect(host="localhost",user="kasperky_tg_bot",password='D4tas27w@',database="kaspersky_bot_db") as connection:
        
        get_phone_query = """
        SELECT COUNT(*) FROM lic_keys WHERE free = 0
        """
 
 
        with connection.cursor(buffered=True) as cursor:
            cursor.execute(get_phone_query)
            result = cursor.fetchone()
            kCount = result[0]
            connection.commit()
    return kCount

def sold_keys():
    UserPhone = ' '
    with connect(host="localhost",user="kasperky_tg_bot",password='D4tas27w@',database="kaspersky_bot_db") as connection:
        
        get_phone_query = """
        SELECT COUNT(*) FROM sold_keys;
        """
 
 
        with connection.cursor(buffered=True) as cursor:
            cursor.execute(get_phone_query)
            result = cursor.fetchone()
            soldCount = result[0]
            connection.commit()
    return soldCount

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):

    

    while True:
        sKeys = sold_keys()
        s_keys = read_var()
        keys_count = check_keys()
        
        if sKeys > s_keys:
            await bot.send_message(str(1733672501),'Через вашего бота произвели новую покупку!' )
            change_var()

        if keys_count < 4:
            await bot.send_message(str(1733672501),'Ключей осталось менее 4 штук, пополните!' )
            await asyncio.sleep(60)

if __name__ == "__main__":
    executor.start_polling(dp)
