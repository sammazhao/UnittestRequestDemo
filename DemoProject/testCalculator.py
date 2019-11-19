import unittest
from DemoProject import mathFunction
import sys
# current_working_directory = "C:\\Users\\mxzhao\\PycharmProjects\\UnittestRequestDemo\\DemoProject"
# sys.path.append(current_working_directory)
print("system path is:", sys.path)

class TestCalculatorFunction(unittest.TestCase):
    def testAdd(self):
        self.assertEqual(3, mathFunction.add(1,2))
        self.assertNotEqual(5, mathFunction.add(1,2))
    def testMinus(self):
        self.assertEqual(2, mathFunction.minus(5,3))

    def testMultiple(self):
        self.assertEqual(0, mathFunction.multi(2,0))

    # def testDivid(self):
        self.assertEqual(3, mathFunction.divid(6,2))

suite=unittest.TestLoader().loadTestsFromTestCase(TestCalculatorFunction)
unittest.TextTestRunner(verbosity=2).run(suite)


