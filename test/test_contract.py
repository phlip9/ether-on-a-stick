from ethereum import tester

import unittest

class TestContract(unittest.TestCase):

    def test_vote_yes(self):
        state = tester.state()
        contract = state.abi_contract('contract.se')

if __name__ == '__main__':
    unittest.main()
