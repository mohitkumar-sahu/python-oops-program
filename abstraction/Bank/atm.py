from abc import ABC,abstractmethod
class ATM(ABC):
    @abstractmethod
    def insert_card(self):
        pass

    @abstractmethod
    def enter_pin(self):
        pass

    @abstractmethod
    def cash_withdraw(self):
        pass

    @abstractmethod
    def cash_deposit(self):
        pass
    
    @abstractmethod
    def balance_enquiry(self):
        pass