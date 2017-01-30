#!python

from string_search import in_string
import unittest

class StringSearchTest(unittest.TestCase):
    def test_in_string_with_clean_lowercase_strings(self):
        assert in_string('', '') is True
        assert in_string('a', 'a') is True
        assert in_string('cat', 'at') is True #end of string
        assert in_string('crate','rat') is True #middle of string
        assert in_string('watermelon','water') is True #beginning of string
        assert in_string('gastronomy','astronomy') is True

    def test_in_string_with_mixed_casing(self):
        assert in_string('Cat', 'AT') is True #casing off in the end
        assert in_string('Crate','RAT') is True #casing off in the middle
        assert in_string('Watermelon','MElon') is True #casing off in the beginning
        assert in_string('CatASTROphe','cAt') is True #truly mixed casing
        assert in_string('GaStRoNoMy','AsTrOnOmY') is True #opposite casing

    def test_in_string_with_whitespace(self):
        assert in_string('back in', 'kin') is True
        assert in_string('store stack','rest') is True
        assert in_string('how are you', 'war') is True

    def test_in_string_with_whitespace_and_mixed_casing(self):
        assert in_string('bacK iN', 'kin') is True
        assert in_string('StorE STack','rest') is True
        assert in_string('How Are You', 'war') is True

    def test_in_string_with_whitespace_and_punctuation(self):
        assert in_string('back in!!', 'kin') is True
        assert in_string("store' stack",'rest') is True
        assert in_string('"how." are, you?', 'war') is True

    def test_in_string_with_whitespace_mixed_casing_and_punctuation(self):
        assert in_string('Back in!!', 'kin') is True
        assert in_string("Store' Stack",'rest') is True
        assert in_string('"How." Are, You?', 'war') is True

    def test_not_in_string(self):
        assert in_string('a','b') is False
        assert in_string('bb','c') is False
        assert in_string('cat','car') is False
        assert in_string('crate','create') is False #len(sub_str) > len(super_str)
        assert in_string('watermelon','lemon') is False #anagram of sub_str exists but not sub_str itself
        assert in_string('gastronomy','groom') is False

if __name__ == '__main__':
    unittest.main()
