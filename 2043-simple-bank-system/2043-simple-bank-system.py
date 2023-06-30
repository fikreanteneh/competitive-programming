class Bank:

    def __init__(self, balance: List[int]):
        self.balanace = balance 
        self.accounts = len(balance) 

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 > self.accounts or account2 > self.accounts:
            return False
        if self.balanace[account1 - 1] < money:
            return False
        self.balanace[account1 - 1] -= money
        self.balanace[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account > self.accounts :
            return False
        self.balanace[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account > self.accounts :
            return False
        if self.balanace[account - 1] < money: 
            return False
        self.balanace[account - 1] -= money
        return True

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)