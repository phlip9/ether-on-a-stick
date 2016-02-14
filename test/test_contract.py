import unittest
from random import random as rand

from ethereum import tester as t
from ethereum import utils as u

def convert_hex_int(hex_str):
    return int('0x' + hex_str.encode('hex'), 16)

class TestContract(unittest.TestCase):

    def setUp(self):
        self.s = t.state()
        self.c = self.s.abi_contract('contract.se')

    def test_create_pool(self):
        self.assertEqual(
            self.c.create_pool(123, t.a0, 'my contract', 'some event', 100, 1234),
            1
        )
        self.assertEqual(
            self.c.get_recipient(123),
            convert_hex_int(t.a0)
        )
        self.assertEqual(self.c.get_name(123), 'my contract')

    # def test_vote_yes(self):
        # state = tester.state()
        # contract = state.abi_contract('contract.se')

if __name__ == '__main__':
    unittest.main()
