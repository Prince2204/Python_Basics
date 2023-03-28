import unittest
import capitalize

class TestCapitalize(unittest.TestCase):

    def test_one_word(self):
        text="hello"
        result=capitalize.convert_to_capital(text)
        self.assertEqual(result,"Hello")

    def test_multi_word(self):
        text="hello prince"
        result=capitalize.convert_to_capital(text)
        self.assertEqual(result,"Hello Prince")

    def test_multi_word_using_title(self):
        text="hello prince"
        result=capitalize.convert_to_title(text)
        self.assertEqual(result,"Hello Prince")


if __name__ == '__main__' :
    unittest.main()
