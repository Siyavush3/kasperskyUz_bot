from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_TOKEN
from mysql.connector import connect, Error

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


Ru_msg = '''Кибербезопасность в бизнесе. Все нюансы, а так же способы себя обезопасить в этом видео:

https://youtu.be/8BqGmAiecdU

 '''




Uz_msg = '''Biznesdagi kiberxavfsizlik. Ushbu videoda barcha nuanslar, shuningdek o'zingizni himoya qilish usullari:

https://youtu.be/8BqGmAiecdU'''



def GET_ID():

        Users = ' '
        with connect(host="localhost",user="kasperky_tg_bot",password='D4tas27w@',database="kaspersky_bot_db") as connection:
            print(connection)
            get_id_query = """
            SELECT * FROM users 
            """
            
            
            with connection.cursor(buffered=True) as cursor:
                cursor.execute(get_id_query)
                result = cursor.fetchall()
                Users = result
                connection.commit()
        return Users


@dp.message_handler(commands=['send_news'])
async def process_start_command(message: types.Message):

    if str(message.chat.id) == '1733672501':
        Id = GET_ID()
        for i in range(len(Id)):
            print(str(Id[i][1]))
            print('\n' + str(type(Id[i][2])))
            try:
                if Id[i][2] == 'UZ':
                    await bot.send_message(str(Id[i][1]), Uz_msg)
                else:
                    await bot.send_message(str(Id[i][1]), Ru_msg)
            except:
                i = i + 1



if __name__ == '__main__':
    executor.start_polling(dp)
