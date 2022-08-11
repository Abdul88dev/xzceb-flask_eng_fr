import unittest
from translator import englishToFrench,frenchToEnglish

class TestenglishTofrench(unittest.TestCase):
    def test_method(self):
        self.assertEqual(englishToFrench("Hello"),'Bonjour')
        self.assertEqual(englishToFrench("What is your name"),'Quel est votre nom?')



class Testfrenchtoenglish(unittest.TestCase):
    def test_method(self):
        self.assertEqual(frenchToEnglish("Bonjour"),'Hello')
        self.assertEqual(frenchToEnglish("Quel est votre nom?"),'What is your name?')




unittest.main()
