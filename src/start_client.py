from telethon import TelegramClient

import os
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
    APP_ID = os.environ.get('APP_ID')
    API_HASH = os.environ.get('API_HASH')

    client = TelegramClient('tg-account', int(APP_ID), API_HASH)
else:
    raise Exception("Отсутствуют переменные окружения")

# APP_ID = 1252636
# API_HASH = '4037e9f957f6f17d461b0c288ffa50f1'
# client = TelegramClient('tg-account', int(APP_ID), API_HASH)

