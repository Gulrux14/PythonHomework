import json
import os
from modules.account import Account

class Bank:
    def init(self):
        self.accounts = {}
        self.file_path = os.path.join("data", "accounts.json")
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        account_number = len(self.accounts) + 1001
        new_account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = new_account
        self.save_to_file()
        print(f"✅ Hisob yaratildi! {new_account}")

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(account)
        else:
            print("❌ Bunday hisob mavjud emas!")

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.deposit(amount)
            self.save_to_file()
        else:
            print("❌ Hisob topilmadi!")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.withdraw(amount)
            self.save_to_file()
        else:
            print("❌ Hisob topilmadi!")

    def save_to_file(self):
        with open(self.file_path, "w") as file:
            json.dump({acc_num: acc.dict for acc_num, acc in self.accounts.items()}, file)

    def load_from_file(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                try:
                    data = json.load(file)
                    self.accounts = {int(acc_num): Account(**acc_data) for acc_num, acc_data in data.items()}
                except json.JSONDecodeError:
                    self.accounts = {}
        else:
            self.accounts = {}