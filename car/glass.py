class Glass:
    glass_company="ABC"

    def __init__(self,size,thikness,bullet_proof):
        self.size=size
        self.thikness=thikness
        self.bullet_proof=bullet_proof

    def info2(self):
        print(f"Glass Company : {self.glass_company}\nGlass Size : {self.size}\nThikness : {self.thikness}\nBulletProof : {self.bullet_proof}")

