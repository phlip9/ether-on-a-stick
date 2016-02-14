import unittest
from random import random as rand

from ethereum import tester as t
from ethereum import utils as u

def convert_hex_int(hex_str):
    return int('0x' + hex_str.encode('hex'), 16)

def to_ether(wei):
    return wei / 10L**18

def to_wei(ether):
    return ether * 10**18

class TestContract(unittest.TestCase):

    def setUp(self):
        self.s = t.state()
        self.c = self.s.abi_contract('contract.se')

    def balance(self, acct):
        return self.s.block.get_balance(acct)

    def test_create_pool(self):
        self.assertEqual(self.c.create_pool(123, t.a0, 'my contract', 'some event', 100, 50), 1)
        self.assertEqual(self.c.get_recipient(123), convert_hex_int(t.a0))
        self.assertEqual(self.c.get_name(123), 'my contract')
        self.assertEqual(self.c.get_deadline(123), self.s.block.timestamp + 100)
        self.assertEqual(self.c.get_voting_threshold(123), 50)
        self.assertEqual(self.c.get_balance(123), 0)
        self.assertEqual(self.c.get_vote_position(123), 0)

    def test_commit(self):
        self.c.create_pool(123, t.a0, 'my contract', 'some event', 100, 50)
        a1_bal = self.balance(t.a1)
        self.assertEqual(1, self.c.commit(123, sender=t.k1, value=to_wei(1000)))
        assert a1_bal - to_wei(1000) > self.balance(t.a1) # account for gas
        self.assertEqual(self.c.get_balance(123), to_wei(1000))
        self.assertEqual(self.c.get_vote_position(123), 0)

    def test_vote(self):
        self.assertEqual(1, self.c.create_pool(123, t.a0, 'my contract', 'some event', 100, 50))

        # k1 commits 1000 eth
        self.assertEqual(1, self.c.commit(123, sender=t.k1, value=to_wei(1000)))
        self.assertEqual(to_wei(1000), self.c.get_balance(123))
        # k2 commits 500 eth
        self.assertEqual(1, self.c.commit(123, sender=t.k2, value=to_wei(500)))
        self.assertEqual(to_wei(1500), self.c.get_balance(123))
        # k3 commits 250 eth
        self.assertEqual(1, self.c.commit(123, sender=t.k3, value=to_wei(250)))
        self.assertEqual(to_wei(1750), self.c.get_balance(123))
        self.assertEqual(0, self.c.get_vote_position(123))

        # k2 votes no with 500 eth
        self.assertEqual(1, self.c.vote_no(123, sender=t.k2))
        self.assertEqual(to_wei(-500), self.c.get_vote_position(123))

        # k1 votes yes with 1000 eth
        self.assertEqual(1, self.c.vote_yes(123, sender=t.k1))
        self.assertEqual(to_wei(500), self.c.get_vote_position(123))

        # k3 votes yes with 250 eth
        self.assertEqual(1, self.c.vote_yes(123, sender=t.k3))
        self.assertEqual(to_wei(750), self.c.get_vote_position(123))

        # k3 decides to abstain
        self.assertEqual(1, self.c.abstain(123, sender=t.k3))
        self.assertEqual(to_wei(1750), self.c.get_balance(123))
        self.assertEqual(to_wei(500), self.c.get_vote_position(123))


    def test_kill(self):
        self.c.create_pool(123, t.a0, 'my contract', 'some event', 100, 50)
        ret = self.c.kill()


if __name__ == '__main__':
    unittest.main()
