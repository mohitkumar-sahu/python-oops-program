class Store:
    Store_name= "H&M"

    def __init__(self,store_type,no_of_items,no_of_staff):
        self.store_type=store_type
        self.no_of_items=no_of_items
        self.no_of_staff=no_of_staff
        
    def store_info(self):
        print(f"Store Name : {self.Store_name}\nStore Type : {self.store_type}\nNo of Staff : {self.no_of_staff}" )
        