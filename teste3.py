import unittest
import teste4


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)
        teste4.print_hi("Antonio")


if __name__ == '__main__':
    unittest.main()
