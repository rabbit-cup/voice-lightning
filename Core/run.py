
"""
    сдесь только запуск конкретно для "Core"
"""

from ServerTest import Server
from ServerTest import get_time

from Rabbit.Rendering.Texts.Text import printf

import asyncio


server = Server("192.168.0.70", 8080)

if __name__ == "__main__":
    try:
        asyncio.run(server.async_start_server())
    except KeyboardInterrupt:
        printf(f"{get_time()} - [+] Сервер закрыт", color="green")
