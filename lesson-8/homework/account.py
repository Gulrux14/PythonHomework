class Account:
    def init(self, account_number, name, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"💰 {amount} so'm qo'shildi. Yangi balans: {self.balance} so'm")
        else:
            print("⚠️ Noto‘g‘ri summa!")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"💸 {amount} so'm yechildi. Yangi balans: {self.balance} so'm")
        else:
            print("⚠️ Yetarli mablag' yo‘q yoki noto‘g‘ri summa!")

    def str(self):
        return f"🔹 {self.name} (Hisob raqami: {self.account_number}) – Balans: {self.balance} so'm"