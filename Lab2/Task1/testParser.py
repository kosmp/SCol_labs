import unittest
from parser import get_amount_of_declarative_sentences
from parser import get_words_and_num_of_chars


class TestSentenceAmountMethod(unittest.TestCase):
    def test_amount_of_declarative_sentences(self):
        list_of_sentences = ['Abf gr32f 4vd d4g75 32 5 ad, ba, cb etc.', 'Vcdgfd ad?',
                             'Bdf ... cvvkd 3 64 f!', 'Nvf fs?!', 'Cdgdg e.g. gf dv, Dr. Smith.',
                             'Vfgd vsd3.', 'Vsafassf vf...']
        result = get_amount_of_declarative_sentences(list_of_sentences)
        self.assertEqual(result, 4)


class TestNumOfWordsAndNumOfChars(unittest.TestCase):
    def test_num_of_words(self):
        list_of_sentences = ['Abf gr32f 4vd d4g75 32 5 ad, ba, cb etc.', 'Vcdgfd ad?']
        result = get_words_and_num_of_chars(list_of_sentences)
        self.assertEqual(len(result[0]), 10)

    def test_num_of_chars(self):
        list_of_sentences = ['Abf 5c gr32, 34 and etc.', 'Vcdgfd ad?']
        result = get_words_and_num_of_chars(list_of_sentences)
        self.assertEqual(result[1], 23)
