from customtkinter import CTkFrame, CTkTextbox, CTkButton

class Frame(CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.registrationObservers = set()

        self.login = CTkTextbox(self, 200, 35)
        self.login.grid(row=0, column=0, padx=10, pady=10)
        
        self.pasword = CTkTextbox(self, 200, 35)
        self.pasword.grid(row=1, column=0, padx=10, pady=10)

        self.button = CTkButton(self, text="register", command=self.register_event)
        self.button.grid(row=2, column=0, padx=10, pady=10)
    
    def attachRegistrationObserver(self, observer):
        self.registrationObservers.add(observer)
    
    def register_event(self):
        for i in self.registrationObservers:
            i.getRegistrationData(self.login.get("0.0", "end"), self.pasword.get("0.0", "end"))
