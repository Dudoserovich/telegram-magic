from src import handle_message_love
from src.start_client import client
from src.magic_heart import handle_message_hearth
from telethon.events import NewMessage


if __name__ == '__main__':
    print('[*] Connect to client...')
    client.start()
    client.add_event_handler(handle_message_hearth,
                             NewMessage(outgoing=True, pattern='magic'))
    client.add_event_handler(handle_message_love,
                             NewMessage(outgoing=True, pattern='love'))
    client.run_until_disconnected()
