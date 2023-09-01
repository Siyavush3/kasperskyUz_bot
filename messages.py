help_message = '''
Через этого бота можно купить официальную лицензию Kaspersky Standart.
Нажмите на кнопку Купить лицензию, чтобы перейти к покупке.
Узнать правила и положения можно воспользовавшись кнопкой Правила и условия.
'''
help_message_uz = '''
Ushbu bot orqali siz rasmiy Kasperskiy Standart litsenziyasini sotib olishingiz mumkin.
Sotib olishga o'tish uchun litsenziyani sotib olish tugmasini bosing.
Qoidalar va shartlar tugmachasi yordamida qoidalarni bilib olishingiz mumkin.
'''
start_message = 'Добро пожаловать в официальный телеграм бот Kaspersky.com.uz, по всем интересующим вопросам обращаться к администратору бота  @dm1n1strat0r\n' + help_message
start_message_uz = 'Rasmiy Kaspersky.com.uz Telegram botga xush kelibsiz. barcha savollar uchun  bot administratoriga  @dm1n1strat0r  murojaat qiling\n' + help_message_uz
pre_buy_demo_alert = '''\
Бот в тестовом режиме
Все ключи и платежи не действительны
'''

terms = '''\
*Спасибо, что выбрали нашего бота. По всем интересующим вопросам обращаться к администратору бота @dm1n1strat0r *
Ссылка на скачивание Kaspersky Standart - https://www.kaspersky.ru/downloads/standard
Техническая поддержка Kaspersky -  https://support.kaspersky.ru/
Регистрация на едином  портале Kaspersky - https://my.kaspersky.com/#/auth/layout/main 
Инструкция по установке Kaspersky Standart - https://support.kaspersky.ru/kis21/install/15410
Партнерские сертификаты и лицензии - https://bit.ly/47j6Vv3
📋Лицензия №AN03UZ00 до 31.01.2024г.🗒️АО «INNOVATION AND TECHNOLOGY TRANSFERT CENTRE ".
'''

terms_uz = '''\
*Botimizni tanlaganingiz uchun tashakkur. Barcha savollar uchun @dm1n1strat0r bot administratoriga murojaat qiling*

Kaspersky Standart o'rnatish bo'yicha ko'rsatmalar - https://support.kaspersky.ru/kis21/install/15410
Kaspersky Internet xavfsizligini yuklab olish havolasi - https://www.kaspersky.ru/downloads/standard
Kaspersky texnik yordami - https://support.kaspersky.ru/
Kaspersky yagona portalida ro'yxatdan o'tish - https://my.kaspersky.com/#/auth/layout/main
Hamkorlik sertifikatlari va litsenziyalari - https://bit.ly/47j6Vv3
📋 AN03UZ00-sonli litsenziya 31.01.2024 yilgacha 🗒️ "INNOVATION AND TECHNOLOGY transfer Center "AJ.

'''

tm_title = 'Kaspersy Standart'
tm_title_uz = 'Kaspersy Standart'

tm_description = '''\
Больше, чем просто антивирус

🔘Защита от хакеров и вредоносного ПО
🔘Защита онлайн-платежей
🔘Защита файловой системы
🔘Блокировка рекламы и сбора данных
🔘Маскировка  IP-адреса до 300 МБ трафика в день

Для Windows|macOS|Android

'''

tm_description_uz = '''\
Faqat antivirusdan ko'proq narsa

🔘Xakerlar va zararli dasturlardan himoya
🔘Onlayn to'lovlarni himoya qilish
🔘Fayl tizimini himoya qilish
🔘Reklama va ma'lumotlarni yig'ishni blokirovka qilish
🔘Kuniga 300 MB trafikka qadar IP-manzilni yashirish

Windows / macOS / Android uchun

'''


AU_error = '''\
Лицензии Kaspersky Standart активируются только с устройств находящихся на территории Республики Узбекистан,
'''



successful_payment = '''
Ура! Платеж на сумму `{total_amount} {currency}` совершен успешно! Приятного пользования!
Все правила и инструкции можете посмотреть нажав на Правила и условия
Чтобы купить еще одину лицензию Kaspersky Standart нажмите на Кнопку Купить лицензию повторно
'''

successful_payment_uz = '''
Hurray! "{total_amount} {currency} " miqdorida to'lov muvaffaqiyatli amalga oshirildi! Yoqimli foydalanish!
Siz barcha qoidalar va ko'rsatmalarni qoidalar va shartlarni bosish orqali ko'rishingiz mumkin
Boshqa Kasperskiy Standart litsenziyasini sotib olish uchun Litsenziyani sotib olish tugmani bosing
'''



MESSAGES = {
    'start': start_message,
    'start_uz': start_message_uz,
    'help': help_message,
    'help_uz': help_message_uz,
    'pre_buy_demo_alert': pre_buy_demo_alert,
    'terms': terms,
    'terms_uz': terms_uz,
    'tm_title': tm_title,
    'tm_title_uz': tm_title_uz,
    'tm_description': tm_description,
    'tm_description_uz': tm_description_uz,
    'AU_error': AU_error,
    'successful_payment': successful_payment,
    'successful_payment_uz': successful_payment_uz,
}
