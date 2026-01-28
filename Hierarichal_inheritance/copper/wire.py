from p1 import Copper

class Wire(Copper):
    Company_name='ABC'
    GST_No='abc8723792487'

    def __init__(self, grade,type,length,width):
        super().__init__(grade)
        self.type=type
        self.length=length
        self.width=width

    def wire_info(self):
        print('--------wire Info----------')
        print(f"Company Name : {self.Company_name}\nGST No : {self.GST_No}\nType : {self.type}\nLength : {self.length}\nWidht : {self.width}")
        self.copper_info

obj_w=Wire('A','pvc Wire','50m','20mm')
obj_w.wire_info()