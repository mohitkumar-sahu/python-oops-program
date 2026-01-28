from p1 import Calculator

class My_Calculator(Calculator):

    def addition(self,a,b):
        print(f'Sum : {a+b}')

    def substraction(self,a,b):
        print(f'Substraction : {a-b}')

    def multiplication(self,a,b):
        print(f'Product : {a*b}')
        
    def division(self,a,b):
        print(f'Division : {a/b}')