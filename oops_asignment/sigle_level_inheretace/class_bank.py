class Bank:
    bank_name="HDFC"
    currency_type="Indian rupee"

    def __init__(self,account_holders_name,gender,contact_no):
        self.account_holders_name=account_holders_name
        self.gender=gender
        self.contact_no=contact_no

    def info(self):
        print(f"----------Bank Details----------")
        print(f"Bank Name : {self.bank_name}")
        print(f"Currency Type : {self.currency_type}")
        print(f"Account Holder's Name : {self.account_holders_name}")
        print(f'Gender : {self.gender}')
        print(f"Contact Number {self.contact_no}")


        