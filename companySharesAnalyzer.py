from companyShareAnalyzerBean import CompanyDataBean

class DataInconsistantException(Exception):
    pass
	
class CompanyShareAnalyzer:
    ''' This is the main analysis class that does the overall analysis '''
	
    def __init__(self,path):
        self.__path__=path
        self.result_=None
    
	def readFile(self):
        '''
        The first row contains the company names so, this function reads it
        only ones.This function reads the file and yields the result, line by line.
        It returns 1) Periods(Month/Year) list and 2) Prices List
        '''
        try:
            with open(self.__path__, 'r') as f:
                for ln in f:
                    ln = ln.split(',') # Removing the last ','
                    if self.result_ == None:
                        '''
                             first time to read all company names
                             and set the share value to 0
                        '''
                        self.result_= [ CompanyDataBean(x,0,None,0) for x in ln[2:]]
                        continue
                    if len(self.result_) == len(ln[2:]):
                        yield (ln[:2],ln[2:])
                    else:
                        raise DataInconsistantException("Please check the data inside the file")
		except IOError, err:
            print "IOError : %r" %(err)
            raise IOError("File not Exist")

    def getResultSharePriceAnalysis(self):
        '''
        The main computation happens here and the final result is returned.
        '''
        for period,shareValue in self.readFile():
            for i, val in enumerate(shareValue):
               if self.result_[i] >  val:
                   self.result_[i]=CompanyDataBean(self.result_[i].name,val,period[1],period[0])
        return self.result_
    
    def printResults(self):
    	''' This is just to print the results '''
    	for i in self.result_ :
            print i
        
