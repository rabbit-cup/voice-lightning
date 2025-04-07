from abc import ABC, abstractstaticmethod

class Observer(ABC):
    @abstractstaticmethod
    def getRegistrationData(self, login, pasword):
        pass

