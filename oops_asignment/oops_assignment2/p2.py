from p1 import A
class B(A):
    b=20
    def __init__(self,p,q):
        A.__init__(self,p)
        self.q=q

    def meth2(self):
        self.meth1()
        print(f"Q : {self.q}")

