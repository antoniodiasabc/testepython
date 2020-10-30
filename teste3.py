import unittest
import teste4
import teste2

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)
        testname = teste4.print_hi("Antonio")
        self.assertEqual(testname, "Antonio")
        self.assertNotEqual(testname, "Antonios")
        result = teste4.sumtwo(8,9)
        self.assertEqual(result, 17)
        self.assertNotEqual(result, 18)
        primos = teste2.nao_entre_em_panico()
        print(primos)

def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
