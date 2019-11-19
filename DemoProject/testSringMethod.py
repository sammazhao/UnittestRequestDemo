import unittest
class TestStringMethod(unittest.TestCase):
    def test_upper(self):
        self.assertTrue('Xiaoming'.upper(), 'XIAOMING')

    def test_isupper(self):
        self.assertTrue('LOO'.isupper())
        self.assertFalse('Loo'.isupper())

    def test_split(self):
        s='samma zhao'
        with self.assertRaises(TypeError):
            s.split(2)

# if __name__=='__main__':
#     unittest.main()

#或者使用如下代码执行用例
suite=unittest.TestLoader().loadTestsFromTestCase(TestStringMethod)    #传testCase Class
unittest.TextTestRunner(verbosity=2).run(suite)