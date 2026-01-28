class Display:
    display_company='Samsung'

    def __init__(self,type,size,):
        self.type=type
        self.size=size

    def display_info(self):
        print('-------------Display Info--------------')
        print(f"Display Company : {self.display_company}\nDisplay Type : {self.type}\nDisplay Size : {self.size}")