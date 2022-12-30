"""
Script: test_formatter.py
By: Martina Atkinson(L00177769)
Purpose : Unit Testing Using Unittest Module
Prerequisites: formatter.py created
Tested: 15/10/2022
"""

import unittest
import formatter

class TestFormatter(unittest.TestCase):
    def test_lower(self):
        test_text = "MARTINA ATKINSON"
        result = formatter.convert_lower(test_text)
        self.assertEqual(result, "martina atkinson")
    def test_upper(self):
        test_text = "Martina Atkinson"
        result = formatter.convert_upper(test_text)
        self.assertEqual(result, "MARTINA ATKINSON")
if __name__ =="__main":
    unittest.main()


