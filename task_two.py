# Basic Banking System Challenge

#  Define a class called Account with the following attributes and methods:
#  - Attributes: account_number, account_holder, balance
#  - Methods: display_account_info() - prints information about the account

#  Create two subclasses, SavingsAccount and CheckingAccount, that inherit from Account.
#  Each subclass should have its own unique method, for example, earn_interest() for SavingsAccount
#  and deduct_fees() for CheckingAccount.


class Account:
    def __init__(
        self, account_number: int, account_holder: str, balance: float
    ) -> None:
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def display_account_info(self) -> str:
        return f"Account number: {self.account_number}\nAccount holder: {self.account_holder}\nBalance: {self.balance}"


class SavingsAccount(Account):
    def __init__(
        self, account_number: int, account_holder: str, balance: float, interest: float
    ) -> None:
        super().__init__(account_number, account_holder, balance)
        self.interest = interest

    def earn_interest(self, interest_rate: float) -> float:
        return self.balance * interest_rate / 100


class CheckingAccount(Account):
    def __init__(
        self, account_number: int, account_holder: str, balance: float, deduct_fee: float, interest: float
    ) -> None:
        super().__init__(account_number, account_holder, balance)
        self.deduct_fee = deduct_fee
        self.saving_account = SavingsAccount(account_number=account_number, account_holder=account_holder, balance=balance, interest=interest )

    def deduct_fees(self) -> float:
        return self.balance - self.deduct_fee


account_jonas = SavingsAccount(account_number=1241, account_holder="Jonas Jonaitis", balance=50, interest=50)


print(f"Jonas earn interest: {account_jonas.earn_interest(interest_rate=10)}")

account_matas = CheckingAccount(account_number=1941, account_holder="Matas Mataitis", balance=70, deduct_fee=35)

print(f"Matas deduct fee: {account_matas.deduct_fees()}")

