import unittest
class TestStringMethod(unittest.TestCase):
    def test_upper(self):
        self.assertequal('Xio'.upper(), 'XIAO')
        
    def test_isUpper(self):
        self.assertTrue('Xiao'.upper(), 'XIAO')
        
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
    
    import unittest

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')
        
if __name__=='_main__':
    unittest.main()    
