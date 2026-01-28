from atm import ATM
class Bank(ATM):
    def __init__(self,name,acc_no,pin,balance):
        self.name=name
        self.acc_no=acc_no
        self.pin=pin
        self.blance=balance

    def insert_card(self):
        print('Card inserted Sucessfully')

    def enter_pin(self):
        self.insert_card()
        x=int(input("Enter the pin : "))
        if x==self.pin:
            return True
        else:
            return False
        
    def balance_enquiry(self):
        if self.enter_pin():
            print(f'Remaining balance is {self.blance}')

    def cash_withdraw(self):
        if self.enter_pin():
            x=int(input("Enter the amount "))
            if x >= self.blance:
                print('Insufficent Balance')
            else:
                self.blance-=x
                print(f'Accept the money {x}')
                print(f'Remaining Amount is {self.blance}')
        else:
            print('Incorrect Password')

    def cash_deposit(self):
        x=int(input('Enter the deposite amount : '))
        if x>0:
            self.blance+=x
            print(f'{x} Cash is sucessfully deposit.')
            print(f'Total Amount is {self.blance}')

    
