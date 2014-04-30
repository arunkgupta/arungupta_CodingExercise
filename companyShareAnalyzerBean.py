class CompanyDataBean:
    ''' Bean class of Company, holds company name, Company Share price, month & year'''
    def __init__(self,name,value=0,month=None,year=0):
        self.name=name
        self.value=int(value)
        self.month=month
        self.year=int(year)
    def __gt__(self,value):
        ''' The greater than(>) operator is overloaded here'''
        return (int(value) > self.value) 
    def __str__(self):
        ''' The string representation of this class object'''
        return "Company Name : %10s ShareValue : %6s  Month/Year : %4s/%4d" % (str(self.name).strip(), self.value, self.month,self.year)
