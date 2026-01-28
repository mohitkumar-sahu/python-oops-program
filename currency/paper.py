class Paper:
    paper_company="xyz"
    country_of_origin='India'

    def __init__(self,length,width,thikness):
        self.length=length
        self.width=width
        self.thikness=thikness

    def info1(self):
        print(f"Paper Company Name : {self.paper_company}\nCountry of Origin : {self.country_of_origin}\nLength : {self.length}\nWidth : {self.width}\nThikness : {self.thikness}")
        