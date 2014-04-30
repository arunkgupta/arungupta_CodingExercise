from companySharesAnalyzer import CompanyShareAnalyzer, DataInconsistantException
import unittest
class TestCompanyShareAnalyzer(unittest.TestCase):
    '''
    This is a test class to test CompanyShareAnalyzer class
    '''
    def test_for_inconsistant_data_in_file(self): 
        ''' This raises an exception for inconsistent data in file '''
		
        shareAnalyzer = CompanyShareAnalyzer("shareData_inconsistant.csv")
        #print "HELLO %r"% (shareAnalyzer.getResultSharePriceAnalysis().getName())
        self.assertRaises(DataInconsistantException,  lambda: shareAnalyzer.getResultSharePriceAnalysis())
		
    def test_for_inexistant_file(self):
        ''' This raises an exception for non-existing file '''
		
        shareAnalyzer = CompanyShareAnalyzer("some_non_existant_file.csv")
        self.assertRaises(IOError, lambda: shareAnalyzer.getResultSharePriceAnalysis())
		
    def test_share_value(self):
        shareAnalyzer = CompanyShareAnalyzer("shareData.csv")
        self.result=shareAnalyzer.getResultSharePriceAnalysis()
        '''   Company 9 maximum price is 100    '''
		self.assertEquals(100, self.result[8].value)
		
    def test_share_month(self):
        shareAnalyzer = CompanyShareAnalyzer("shareData.csv")
        self.result=shareAnalyzer.getResultSharePriceAnalysis()
        '''   Company 1 max price month july  '''
        self.assertEquals('jul', self.result[0].month)
    
	def test_share_year(self):
        shareAnalyzer = CompanyShareAnalyzer("shareData.csv")
        self.result=shareAnalyzer.getResultSharePriceAnalysis()
        '''   Company 7 max price year is 1990  '''
        self.assertEquals(1990, self.result[6].year)
        '''Just to print the results in one sample '''
        print '\nHere are the results for the final test case \n'
        shareAnalyzer.printResults()

		
if __name__ == '__main__':
    unittest.main()
