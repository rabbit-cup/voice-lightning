import customtkinter as ctk


"""Меню регистрации"""
class UIRegistr(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Registr") # заголовок окна
        self.geometry("1100x650") # геометрия окна
