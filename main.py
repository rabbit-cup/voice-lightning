import customtkinter as ctk
import Registration.Frame
import Registration.Observer

"""
я плохо знаю python но вот тебе пример того как правильной архетектуры приложения
    т.е. то как правильно создавать классы не зависимо от языка
"""

"""
    в кратце как этим пользоваться

    создаешь в новом файле класс ответственный за добавление пользователя
        и наследуешь его от класса Observer который находится по пути: 
            ./Registration/Observer.py/Observer
"""

class SendUserToServer(Registration.Observer.Observer):
    
    """переписываешь метод getRegistrationData"""
    def getRegistrationData(self, login, pasword):
        """для примера просто выведу в консоль но ты должен отправить их на сервер"""
        print(login, pasword)



class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("800x600")
        self.title("voice-lighting")
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.frameRegistration = Registration.Frame.Frame(self)
        self.frameRegistration.grid(row=0, column=0, padx=10, pady=10)

        self.sendlerUsers = SendUserToServer()

        self.frameRegistration.attachRegistrationObserver(self.sendlerUsers)

        """
            как это работает:
                функция attachRegistrationObserver добавляет наш observer в список
                и когда что то в нашем классе происходит (в нашем случае нажатие на кнопку "")
                то тогда frameRegistration проходит по всему списку и у каждого
                объекта списка вызывает функцию getRegistrationData и передает туда логин и пароль
                а уже ТВОЙ класс отправляет их на сервер

            PS:
                судя по твоему коду ты я думаю что ты этого всего не знал и по этому 
                    я для тебя все это расписываю

                и не надо сувать все в один класс это не профисианально
        """



if __name__ == "__main__":
    app = App()
    app.mainloop()