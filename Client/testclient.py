
"""
    сдесь сделай консольный клиент
"""

import websockets
import json

from Rabbit.Rendering.Texts.Text import printf


class Client:
    def __init__(self, url):
        self.url = url # url Сервера
        self.websocket = None # Храним сосдавшийся websocket
        self.my_id = None # Храним свой id

    async def async_connect(self):
        """Присоеденяемся к серверу"""
        self.websocket = await websockets.connect(self.url) # Подключаемся к серверу
        self.my_id = await self.websocket.recv() # Получаем id
        printf(f"[+] Вы подключены к серверу вашь ID: {self.my_id}", color="green", style=True)
        await self.geting_in_toch_server() # Запускаем функцию для взаимодействия со сервером

    async def geting_in_toch_server(self):
        """Взаимодействуем со сервером"""
        while True:
            message = str(input("--> ")) # Вводим сообщение
            await self.send_data(message) # Обробатываем и отпровляем на сервер данные
            data = await self.websocket.recv() # Получаем ответ от сервера
            self.maneger_message(data) # Обробатываем ответ

    def maneger_message(self, message):
        """Обрабатываем данные от сервера тут"""
        print(message)

    async def send_data(self, data):
        """Отпровляем оброботоеые данные серверу"""
        new_data = json.dumps([self.my_id, data])
        await self.websocket.send(new_data)

    async def start_client(self):
        """Запускаем клиента"""
        await self.async_connect()
        printf(f"[+] Клиент запущен вашь ID: {self.my_id}", color="green", style=True)







