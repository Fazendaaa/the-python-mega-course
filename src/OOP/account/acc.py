"""Libary that implements the Account"""

#   -----------------------------   CLASSES   ------------------------------   #

class Account:
    """Class that handles all the accounts operations"""
    def __init__(self, filename):
        """Initlize the class with the file that has the account data"""
        self.filename = filename
        with open(self.filename, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        """Update the balance value when withdraw"""
        self.balance -= amount

    def deposit(self, amount):
        """Update the balance value when deposit"""
        self.balance += amount

    def commit(self):
        """Save all the changes in the account"""
        with open(self.filename, 'w') as file:
            file.write(str(self.balance))

#   Why pass Account as argumment to Checking one may ask? Beacuse is the Python
#   syntax to inheritance
class Checking(Account):
    """Class that handles all the checking account operations"""
    type = 'checking'

    def __init__(self, filename, fee):
        """Initlize the class with the file that has the account data"""
        Account.__init__(self, filename)
        self.fee = fee

    def transfer(self, amount):
        """Transfer the determinate amount"""
        self.balance -= amount - self.fee

#   ------------------------------   MAIN   --------------------------------   #

ACCOUNT = Account('../../input/balance_acc.txt')
print('Account balance:', ACCOUNT.balance)
ACCOUNT.withdraw(100)
print('Account balance:', ACCOUNT.balance)
ACCOUNT.deposit(300)
print('Account balance:', ACCOUNT.balance)
ACCOUNT.commit()
print('Account balance:', ACCOUNT.balance)

CHECKING = Checking('../../input/balance_che.txt', 1)
print('Checking balance:', CHECKING.balance)
CHECKING.withdraw(100)
print('Checking balance:', CHECKING.balance)
CHECKING.deposit(700)
print('Checking balance:', CHECKING.balance)
CHECKING.transfer(380)
print('Checking balance:', CHECKING.balance)
CHECKING.commit()
print('Checking balance:', CHECKING.balance)

JOE = Checking('../../input/balance_joe.txt', 1)
print('Joe\'s balance:', JOE.balance)
JOE.transfer(80)
print('Joe\'s balance:', JOE.balance)
JOE.commit()
print('Joe\'s balance:', JOE.balance)
print('Joe\'s type:', JOE.type)

WILL = Checking('../../input/balance_will.txt', 1)
print('Will\'s balance:', WILL.balance)
WILL.transfer(230)
print('Will\'s balance:', WILL.balance)
WILL.commit()
print('Will\'s balance:', WILL.balance)
print('Will\'s type:', WILL.type)

#   ------------------------------   EOF   ---------------------------------   #
