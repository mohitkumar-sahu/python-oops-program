from p1 import p1
from p2 import p2
from p3 import p3

class child(p3,p1,p2):
    d=40
    def __init__(self, r,p,q,s):
        super().__init__(r)
        p1.__init__(self,p)
        p2.__init__(self,q)
        self.s=s
    
    def meth4(self):
        print(f"p:{self.p}\nQ:{self.q}\nr:{self.r}\ns:{self.s}")

obj_c=child(10,20,30,40)
obj_c.meth4()