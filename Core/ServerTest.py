import asyncio

from Rabbit.Rendering.Texts.Text import printf
from datetime import datetime

import websockets
import json


def get_time():
    return str(datetime.now().time())[:-7]

class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.list_conection_client = {}

    async def handler(self, websocket, path):
        """Обработка нового подключения"""
        id_client = str(id(websocket))
        self.list_conection_client[id_client] = websocket
        printf(f"{get_time()} - [+] Присоеденился клиент ID: {id_client}", color="green")
        await websocket.send(str(id_client))

        # Обрабатываем сообщение от клиентов
        try:
            async for message in websocket:
                await self.manager_message(json.loads(message))
        # Обрабатываем ошибки
        except websockets.exceptions.ConnectionClosedError:
            printf(f"[-] Клиент аворино отключился ID: {id_client}", color="red")

    async def manager_message(self, message):
        """Обрабатываем сообщение"""
        id_client = message[0]
        data = message[1]
        if data == "help":
            #Это для теста
            help_menu = """
            my id - Показывает вашь id
            number conection - Показывает сколько всего подключино клиентов"""
            await self.list_conection_client[id_client].send(help_menu)
        elif data == "my id":
            await self.list_conection_client[id_client].send(f"Вашь ID: {id_client}")
        elif data == "number conection":
            await self.list_conection_client[id_client].send(f"Подключино - {len(self.list_conection_client)}")
        else:
            await self.list_conection_client[id_client].send(f"Такой команды нет !")

    async def async_start_server(self):
        """Запускаем сервер"""
        server = await websockets.serve(self.handler, self.ip, self.port)
        printf(f"{get_time()} - [+] Сервер запущен IP: {self.ip} PORT:{self.port}", color="green", style=True)

        await server.wait_closed()
