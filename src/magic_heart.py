import asyncio
from random import choice

from .start_client import client
from telethon.events import NewMessage


HEART = '🤍'
COLORED_HEARTS = ['💗', '💓', '💖', '💘', '❤️', '💞']
MAGIC_PHRASES = ['magic']
EDIT_DELAY = 0.02

PARADE_MAP = '''
00000000000
00111011100
01111111110
01111111110
00111111100
00011111000
00001110000
00000100000
'''


def generate_parade_colored():
    output = ''
    for c in PARADE_MAP:
        if c == '0':
            output += HEART
        elif c == '1':
            output += choice(COLORED_HEARTS)
        else:
            output += c
    return output


async def process_love_words(event: NewMessage.Event):
    sequence = 'i love you forever'.split(" ")
    result = ''

    for word in sequence:
        result += f"{word} " if word != sequence[-1] else word + '💗'

        await client.edit_message(event.peer_id.user_id, event.message.id, result)
        await asyncio.sleep(1)


async def process_build_place(event: NewMessage.Event):
    output = ''
    for i in range(8):
        output += '\n'
        for j in range(11):
            output += HEART
            await client.edit_message(event.peer_id.user_id, event.message.id, output)
            await asyncio.sleep(EDIT_DELAY / 2)


async def process_colored_parade(event: NewMessage.Event):
    for i in range(50):
        text = generate_parade_colored()
        await client.edit_message(event.peer_id.user_id, event.message.id, text)

        await asyncio.sleep(EDIT_DELAY)


async def handle_message_hearth(event: NewMessage.Event):
    await process_build_place(event)
    await process_colored_parade(event)
    await process_love_words(event)