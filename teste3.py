import unittest
import teste4


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)
        name = teste4.print_hi("Antonio")
        self.assertEqual(name, "Antonio")
        self.assertNotEqual(name, "Antoniu")


if __name__ == '__main__':
    unittest.main()
