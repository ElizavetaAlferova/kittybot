# send_random_image.py

import requests  # Импортируем библиотеку для работы с запросами

from telegram import Bot

bot = Bot(token='6309835394:AAFhK0lUXc_kMb3kmuXvF7sgASUBfrTGZfk')
# Адрес API сохраним в константе
URL = 'https://api.thecatapi.com/v1/images/search'
chat_id = 1587781686
# Сделаем GET-запрос к API
# метод json() преобразует полученный ответ JSON в тип данных, понятный Python
response = requests.get(URL).json()

# Рассмотрим структуру и содержимое переменной response
random_cat_url = response[0]['url']
bot.send_photo(chat_id, random_cat_url)