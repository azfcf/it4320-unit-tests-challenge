import unittest
import datetime

class Project3Test(unittest.TestCase):
    def test1(self): # symbol 
        self.assertRegexpMatches("VWAO-CF2", "^[A-Z]{1,7}$")
    def test2(self): # chart type
        self.assertRegexpMatches("1", "^[1-2]$")
    def test3(self): # time series
        self.assertRegexpMatches("f82", "^[1-4]$")
    def test4(self): # start date (regex method) 
        self.assertTrue(isinstance(datetime.datetime.strptime("2023-02-28", "%Y-%m-%d"), datetime.date))
    def test5(self): # end date (strptime)
        self.assertGreaterEqual(datetime.datetime.strptime("2023-02-29", "%Y-%m-%d"), datetime.datetime.strptime("2023-02-11", "%Y-%m-%d"))

if __name__ == "__main__":
    unittest.main()