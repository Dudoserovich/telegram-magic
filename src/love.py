import os
import asyncio
from random import choice

from .start_client import client
from telethon.events import NewMessage

COLORED_HEARTS = ['💗', '💓', '❤️‍🔥', '💘', '❤️', '🤍']
MAGIC_PHRASES = ['love']
sequence = 'Я тебя люблю, нерпёнок💙'
EDIT_DELAY = 0.2

images = []
for root, dirs, files in os.walk("img"):
    for filename in files:
        images.append(filename)


async def process_love(event: NewMessage.Event):
    chat = event.chat

    result = ''

    # Печать сообщения
    for char in sequence:
        random_hearth = choice(COLORED_HEARTS) if char != sequence[-1] else ''
        result += char + random_hearth

        await client.edit_message(event.peer_id.user_id, event.message.id, result)
        await asyncio.sleep(EDIT_DELAY)
        result = result[:-len(random_hearth)]

    await client.send_file(entity=chat, file=f"img/{choice(images)}")


async def handle_message_love(event: NewMessage.Event):
    await process_love(event)
