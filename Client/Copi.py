
"""
    Это не трогай это для меня
               ! ! !
"""

import websockets
import asyncio
import threading


class Client:
    def __init__(self, url):
        self.url = url # url Сервера
        self.websocket = None # Храним сосдавшийся websocket
        self.my_id = None # Храним свой id
        self.loop = asyncio.new_event_loop()  # Храним главный цикл клиента
        self.future_main = None # Хроним корутину подключения из к серверу из другого патока потока

        threading.Thread(target=self.run_client_loop, daemon=True).start() # Запускаем отдельный поток для старта клиента

    def run_client_loop(self):
        """Устанавливаем бесконечный цикл для клиента и запускам его"""
        asyncio.set_event_loop(self.loop) # Устанавливаем цикл
        self.loop.run_forever() # Запускаем бесконечный цикл

    def connect(self):
        """Запускаем корутину с запущиным клиентом из другого потока"""
        self.future_main = asyncio.run_coroutine_threadsafe(self.async_connect(), self.loop)

    async def async_connect(self):
        """Присоеденяемся к серверу"""
        self.websocket = await websockets.connect(self.url) # Подключаемся к серверу
        self.my_id = await self.websocket.recv() # Получаем id
        asyncio.create_task(self.recv_message()) # Запускаем функцию для синхроного приёма данных

    async def recv_message(self):
        while True:
            """Принимаем данные от сервера"""
            data = await self.websocket.recv()
            self.maneger_message(data)

    def maneger_message(self, message):
        """Обрабатываем данные от сервера тут"""
        print(message)

    def start_client(self):
        self.connect()





