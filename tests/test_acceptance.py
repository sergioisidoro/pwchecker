
from pwcheck.utils.Entropy import checklist

import pytest


class TestCharacterSetDetection:
    ## Strings used with edge cases: 0 and 9, a and z etc
    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    def test_lower(self):
        lower_password = "abcdefgz"
        check = checklist(lower_password)
        assert check["lower"] is True and check["capital"] is False and check["numbers"] is False and check["special"] is False

    def test_upper(self):
        upper_password = "ABCDEFGZ"
        check = checklist(upper_password)
        assert check["lower"] is False and check["capital"] is True and check["numbers"] is False and check["special"] is False

    def test_lower_upper(self):
        lower_upper_password = "aABcDeFgzZ"
        check = checklist(lower_upper_password)
        assert check["lower"] is True and check["capital"] is True and check["numbers"] is False and check["special"] is False

    def test_numbers(self):
        numbers_password = "0123459"
        check = checklist(numbers_password)
        assert check["lower"] is False and check["capital"] is False and check["numbers"] is True and check["special"] is False

    def test_numbers_lower(self):
        numbers_lower_password = "a1b2c3d4e5z"
        check = checklist(numbers_lower_password)
        assert check["lower"] is True and check["capital"] is False and check["numbers"] is True and check["special"] is False

    def test_numbers_upper(self):
        numbers_upper_password = "A1B2C3D4E5"
        check = checklist(numbers_upper_password)
        assert check["lower"] is False and check["capital"] is True and check["numbers"] is True and check["special"] is False

    def test_numbers_lower_upper(self):
        numbers_lower_upper_password = "a1B2c3D4e5"
        check = checklist(numbers_lower_upper_password)
        assert check["lower"] is True and check["capital"] is True and check["numbers"] is True and check["special"] is False


    ## TO DO - CHECK FOR SPECIAL CHARACTERS
