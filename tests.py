from telethon.sync import TelegramClient
import io
import time


async def get_channel_messages(channel_id, message_ids):
    global texts
    for i in message_ids:
        try:
            messages = await client.get_messages(channel_id, ids=message_ids[i])
            for message in messages:
                texts[i] = str(message.text)
        except Exception as e:
            print(f"Error: {e}")

while True:
    api_id = 26300743
    api_hash = '4285078f9b776db7e538f6f0edb06662'
    client = TelegramClient('session_name', api_id, api_hash)
    texts = {'dyson': [296], 'iMac': [292], 'playstation': [295], 'iPad': [291], 'Watch': [289], 'MacBook': [290],
                   'iPhone 11_12_13': [297], 'iPhone 14': [298], 'iPhone 15': [299], 'iPhone 16': [300],
                   'airpods': [288]}  # Example message IDs
    channel_id = 'icity_store'
    message_ids = {'dyson': [296], 'iMac': [292], 'playstation': [295], 'iPad': [291], 'Watch': [289], 'MacBook': [290], 'iPhone 11_12_13': [297], 'iPhone 14': [298], 'iPhone 15': [299], 'iPhone 16': [300], 'airpods': [288]} # Example message IDs
    client.start()
    client.loop.run_until_complete(get_channel_messages(channel_id, message_ids))
    client.disconnect()


    ms = ''
    for i in texts:
        ms += i + ' +++ ' + texts[i] + ' -=-=- '

    with io.open('example.txt', 'w', encoding='utf-8') as f:
        f.write(ms)
    time.sleep(3000)