class Milk:
    def __init__(self,milk_type,mfg_date):
        self.milk_type=milk_type
        self.mfg_date=mfg_date

    def milk_info(self):
        print('--------Milk Info---------')
        print(f"Milk used : {self.milk_type}\nMFG Date : {self.mfg_date}\n")
        