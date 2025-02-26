import sys
import os

# modules papkasini qidirish yo‘liga qo‘shish
sys.path.append(os.path.join(os.path.dirname(__file__), "modules"))

from bank_system import Bank

def main():
    bank = Bank()

    while True:
        print("\n📌 Bank menyusi")
        print("1. 🆕 Hisob yaratish")
        print("2. 🔍 Hisobni ko‘rish")
        print("3. 💰 Pul qo‘yish")
        print("4. 💸 Pul yechish")
        print("5. ❌ Chiqish")

        choice = input("Tanlovni kiriting: ")

        if choice == "1":
            name = input("👤 Ismingizni kiriting: ")
            initial_deposit = float(input("💵 Boshlang‘ich depozit summasini kiriting: "))
            bank.create_account(name, initial_deposit)

        elif choice == "2":
            acc_number = int(input("📜 Hisob raqamini kiriting: "))
            bank.view_account(acc_number)

        elif choice == "3":
            acc_number = int(input("📜 Hisob raqamini kiriting: "))
            amount = float(input("💵 Depozit summasini kiriting: "))
            bank.deposit(acc_number, amount)

        elif choice == "4":
            acc_number = int(input("📜 Hisob raqamini kiriting: "))
            amount = float(input("💵 Yechildigan summani kiriting: "))
            bank.withdraw(acc_number, amount)

        elif choice == "5":
            print("🚪 Bank dasturidan chiqildi.")
            break

        else:
            print("⚠️ Noto‘g‘ri tanlov!")

if __name__ == "__main__":
    main()