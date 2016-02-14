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
        self.assertEqual(self.c.create_pool(123, t.a0, 'my contract', 'some event', 100, 1234), 1)
        self.assertEqual(self.c.get_recipient(123), convert_hex_int(t.a0))
        self.assertEqual(self.c.get_name(123), 'my contract')
        self.assertEqual(self.c.get_deadline(123), self.s.block.timestamp + 100)
        self.assertEqual(self.c.get_voting_threshold(123), 1234)
        self.assertEqual(self.c.get_balance(123), 0)
        self.assertEqual(self.c.get_vote_position(123), 0)

    def test_commit(self):
        self.c.create_pool(123, t.a0, 'my contract', 'some event', 100, 1234)
        # self.s.send(t.a0, t.a1, 100000000)
        self.s.send(t.k0, self.c.address, 1000000000000)
        # self.c.commit(123)

    def test_kill(self):
        self.c.create_pool(123, t.a0, 'my contract', 'some event', 100, 1234)
        ret = self.c.kill()

    def test_vote_yes(self):
        ret = self.c.create_pool(123, t.a0, 'my contract', 'some event', 100, 1234)

if __name__ == '__main__':
    unittest.main()
