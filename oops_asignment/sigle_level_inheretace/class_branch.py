from class_bank import Bank
class Branch(Bank):
    ifsc="ABC01234"
    branch="Bengaluru"

    def __init__(self, account_holders_name, gender, contact_no,account_no,account_type):
        super().__init__(account_holders_name, gender, contact_no)
        self.account_no=account_no
        self.account_type=account_type

    def info2(self):
        print(f"Branch : {self.branch}")
        print(f"IFSC : {self.ifsc}")
        self.info()
        print(f"Account No : {self.account_no}")
        print(f"Account Type : {self.account_type}")

b1=Branch("Mohit Sahu",'Male',9128137610,12345678,"saving")
b1.info2()