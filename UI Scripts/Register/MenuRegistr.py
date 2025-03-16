import customtkinter as ctk
from PIL import Image

from os import chdir


"""Меню регистрации"""
class UIRegistr(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Registr") # заголовок окна
        self.geometry("1100x650") # геометрия окна
        self.resizable(False, False) # Запрет на маштобирования окна

        """Настройка колонок"""
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

        """Фрейм для входа"""
        self.frame_entrance = ctk.CTkFrame(self)
        self.frame_entrance.grid(row=1, column=1, columnspan=1, pady=(0, 150))


        """-----Виджеты входа-----"""
        self.text_user_name = ctk.CTkLabel(self.frame_entrance, text='Почта:')
        self.text_user_name.grid(row=0, column=0, padx=(20, 10), pady=(15, 5))

        self.text_pasword = ctk.CTkLabel(self.frame_entrance, text='Пороль:')
        self.text_pasword.grid(row=1, column=0, padx=(20, 10), pady=10)

        self.input_user_name = ctk.CTkTextbox(self.frame_entrance, width=200, height=10, activate_scrollbars=False)
        self.input_user_name.grid(row=0, column=1, padx=(0, 20), pady=(15, 5))

        self.input_pasword = ctk.CTkTextbox(self.frame_entrance, width=200, height=10, activate_scrollbars=False)
        self.input_pasword.grid(row=1, column=1, padx=(0, 20))

        # custom_font = ctk.CTkFont(family="Open San", size=15, weight="bold")
        self.button_entrance = ctk.CTkButton(self.frame_entrance, text="Вход")
        self.button_entrance.grid(row=2, column=0, sticky='ew', columnspan=2, padx=20, pady=(10, 0))

        self.button_register = ctk.CTkButton(self.frame_entrance, text="Регистрация", hover=False,
                                             text_color="white", width=0, fg_color='transparent')
        self.button_register.grid(row=3, column=0, columnspan=2, pady=5)

        # Смена цвета шрифта на кнопке регистрация при наведение
        self.button_register.bind("<Enter>", lambda event: self.button_register.configure(text_color='#4B38FF'))
        self.button_register.bind("<Leave>", lambda event: self.button_register.configure(text_color="white"))

        #Картинка лого
        self.image_logo_pil = Image.open("../../UI/MenuRegister/LogoMOLNNEW.png")
        self.image_logo = ctk.CTkImage(self.image_logo_pil, size=(450, 100))

        self.labe_image = ctk.CTkLabel(self, image=self.image_logo, text='')
        self.labe_image.grid(row=0, column=1, columnspan=1, pady=(130, 0))


