#!/usr/bin/env python
"""
    test_gen_pass.py
    ~~~~~~~~~~~~~~~~

    Tests nupass.gen_pass() to verify

    :copyright: (c) 2017 by Sean Callaway.
    :license: GNU GPL v2, see LICENSE for more details.
"""
import unittest
from nupass import gen_pass

class TestGenPass(unittest.TestCase):
    """Test for NuPass password generation."""

    def setUp(self):
        """Generate the password for testing."""
        self.password = gen_pass()

    def test_two_upper(self):
        """Verify there are exactly two uppercase characters."""
        self.assertEqual(sum(1 for c in self.password if c.isupper()), 2)

    def test_two_digits(self):
        """Verify there are exactly two digits."""
        self.assertEqual(sum(1 for c in self.password if c.isdigit()), 2)

    def test_one_symbol(self):
        """Verify there is exactly one symbol."""
        self.assertEqual(sum(1 for c in self.password if not c.isalnum()), 1)

if __name__ == '__main__':
    unittest.main()
