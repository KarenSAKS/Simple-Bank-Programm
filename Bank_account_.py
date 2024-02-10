
import json

class Bank_accaunt:
    '''Program secured by SmartCode Privecy Policy'''
    def __init__(self,__acount_number,__balance):
        self.__acount_number = __acount_number
        self.__balance =__balance
        self.transaction = []
    
    def deposit(self,amount):
        '''Record  deposits.'''
        self.__balance += amount
        self.transaction.append(f"Deposit: {amount}$") 
    
    def withdraw(self,amount: int) -> None:
        '''Record  withdrawals.'''
        if self.__balance - amount >= 0:
            self.__balance -= amount
            self.transaction.append(f"Withdrawal: {amount}$") 
        else:
            self.transaction.append(f"Withdrawal Failed // Insufficient funds!")

    def transfer(self,other_acount,amount):
        '''Transfer the amount to other acount'''
        if self.__balance - amount >= 0:
            self.__balance -= amount
            self.transaction.append(f"Transfer to {other_acount}: {amount}$")
            other_acount.__balance += amount
            other_acount.transactions.append(f'Transfer from\
                                {self.__acount_number} {amount}$')

    def generate_statment(self):
        '''Ganerate the statment of transactions.'''
        for i in self.transaction:
            print(i)

    def get_balance(self):
        '''Returns the balance of bank acount.'''
        return self.__balance
    
    def clear_transaction(self):
        self.transaction.clear()


def load_data(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    


Action_menu ='''
1.New account.
2.Sign in.
'''
Main_Action_menu = '''
1.Deposit.
2.Get balance.
3.Withdraws.
4.Statments.
5.Clear transactions.
6.Sign out
7.Quit
''' 

Common_data = []
current_user = None

while True:
    if not current_user:
        load_data('Common_data.json')


# user1 = Bank_accaunt('12345',2000)
# user2 = Bank_accaunt('54321',5000)

# user1.deposit(1200)

# user1.transfer(54321,1000)
# user2.deposit(1000)

# balance1 = user1.get_balance()
# balance2 = user2.get_balance()

# print('Transaction_user1',user1.transaction,'Balance',balance1)
# print('Transaction_user2',user2.transaction,'Balance',balance2)


