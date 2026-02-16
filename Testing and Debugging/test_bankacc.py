"""a BankAccount class that needs to be tested. 
Class TestAccount extends the TestCase and has several test methods 
that check the BankAccount's deposit and withdrawal methods."""

import unittest

class BankAccount:
    def __init__(self, bal=0):
        self._balance = bal              # Bug

    def deposit(self, amt):
        self._balance += amt             # Bug

    def withdrawal(self, amt):
        self._balance -= amt             # Bug
        if self._balance >= 0:
            return True
        return False

    @property
    def balance(self):
        return self._balance

class TestAccount(unittest.TestCase):
    def test_default_account(self):      # pass
        acct = BankAccount()
        self.assertEqual(acct.balance, 0)

    def test_account(self):              # pass
        acct = BankAccount(100)
        self.assertEqual(acct.balance, 100)

    def test_deposit(self):              # pass
        acct = BankAccount()
        acct.deposit(100)
        self.assertEqual(acct.balance, 100)

    def test_withdrawal(self):           # pass
        acct = BankAccount(100)
        acct.withdrawal(25)
        self.assertEqual(acct.balance, 75)

    def test_insufficient_funds(self):   # fail
        acct = BankAccount(100)
        self.assertFalse(acct.withdrawal(200))
        self.assertEqual(acct.balance, 100)

    def test_negative_account(self):     # fail
        acct = BankAccount(-100)
        self.assertEqual(acct.balance, 0)

    def test_negative_deposit(self):     # fail
        acct = BankAccount()
        acct.deposit(-100)
        self.assertEqual(acct.balance, 0)

    def test_negative_withdrawal(self):  # fail
        acct = BankAccount(100)
        acct.withdrawal(-100)
        self.assertEqual(acct.balance, 100) 

unittest.main(exit=False)