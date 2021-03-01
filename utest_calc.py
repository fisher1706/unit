import unittest
import calc


class CalcBasicTests(unittest.TestCase):
    """Calc tests"""

    @classmethod
    def setUpClass(cls):
        """Set up for class"""
        print("setUpClass")
        print("==========")

    @classmethod
    def tearDownClass(cls):
        """Tear down for class"""
        print("==========")
        print("tearDownClass")

    def setUp(self):
        """Set up for test"""
        print('Set up for [' + self.shortDescription() + ']')

    def tearDown(self):
        """Tear down for test"""
        print('Tear down for [' + self.shortDescription() + ']')

    def test_add(self):
        """Add operation test"""
        print('id: ' + self.id())
        self.assertEqual(calc.add(1, 2), 3)

    def test_sub(self):
        """Sub operation test"""
        print('id: ' + self.id())
        self.assertEqual(calc.sub(4, 2), 2)

    def test_mul(self):
        """Mul operation test"""
        print('id: ' + self.id())
        self.assertEqual(calc.mul(2, 5), 10)

    def test_div(self):
        """Div operation test"""
        print('id: ' + self.id())
        self.assertEqual(calc.div(8, 4), 2)

@unittest.skip('Skip CalcExTests')
class CalcExTests(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(calc.sqrt(4), 2)

    # @unittest.skip('Temporaly skip test_pow')
    def test_pow(self):
        self.assertEqual(calc.pow(3, 3), 27)


if __name__ == '__main__':
    unittest.main()