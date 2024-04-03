import test2
import unittest

class calculator(unittest.TestCase):
    def test_summ(self):
        self.assertEqual(test2.summ(10,10),20)
        self.assertEqual(test2.summ(0,0),0)
        self.assertEqual(test2.summ(-10,10),0)
        self.assertEqual(test2.summ(10.1,10),20.1)        
        
    def test_sub(self):
        self.assertEqual(test2.sub(10,10),0)
        self.assertEqual(test2.sub(-10,10),-20)
        self.assertEqual(test2.sub(0,0),0)
        self.assertEqual(test2.sub(-10,-10),0)

    def test_mul(self):
        self.assertEqual(test2.mul(10,10),100)
        self.assertEqual(test2.mul(-10,10.1),-101)
        self.assertEqual(test2.mul(0,0),0)
        self.assertEqual(test2.mul(-10,10),-100)
        
    def test_div(self):
        self.assertEqual(test2.div(10,10),1)
        self.assertEqual(test2.div(-10,10),-1)
        self.assertEqual(test2.div(0.1,10),0.01)
        self.assertRaises(ZeroDivisionError,test2.div,-10,0)


if __name__=='__main__':
    unittest.main()