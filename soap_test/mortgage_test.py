# Some comment
import logging
import unittest
from suds.client import Client

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.DEBUG, filename='mortgage_test.log')
logger = logging.getLogger(__name__)

class MortgageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        url = 'http://www.webservicex.net/mortgage.asmx?WSDL'
        cls._client = Client(url)

    def testMonthlyPrincipalAndInterest(self):
        soap = self._client.service.GetMortgagePayment(30, 4.2, 250000.0, 0.0, 0.0)
        self.assertEquals(round(soap.MonthlyPrincipalAndInterest, 2), 1222.54)

    def testMonthlyTax(self):
        soap = self._client.service.GetMortgagePayment(30, 4.2, 250000.0, 2.5, 0.0)
        self.assertEquals(round(soap.MonthlyTax, 2), 0.21)

    def testMonthlyInsurance(self):
        soap = self._client.service.GetMortgagePayment(30, 4.2, 250000.0, 0.0, 3.0)
        self.assertEquals(round(soap.MonthlyInsurance, 2), 0.25)

    def testTotalPayment(self):
        soap = self._client.service.GetMortgagePayment(50, 5.0, 200000.0, 1.0, 3.0)
        self.assertEquals(round(soap.TotalPayment, 2), 908.61)


if __name__ == '__main__':
    unittest.main()