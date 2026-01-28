from p2 import B
class C(B):
    c=30
    def __init__(self,p,q,r):
        B.__init__(self,p,q)
        self.r=r

    def meth3(self):
        self.meth2()
        print(f"R : {self.r}")

c1=C(10,20,30)
c1.meth3()
