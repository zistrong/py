import unittest
import sys
sys.path.append(r'./')
import ch10.ch10_2 as ch
class PrimeTest(unittest.TestCase):
    def testPrime(self):
        self.assertTrue(ch.isPrime(5))
    def testGcd(self):
        self.assertEqual(ch.gcd(3,6),3)
        
if __name__ == '__main__':
    unittest.main()