class Cement:
    cement_company='Dalmia'

    def __init__(self,mfg_date,exp_date):
        self.mfg_date=mfg_date
        self.exp_date=exp_date

    def cement_info(self):
        print('-------------Cement Info--------------')
        print(f"Cement Company : {self.cement_company}\nMFG Date : {self.mfg_date}\nEXP Date : {self.exp_date}")
    