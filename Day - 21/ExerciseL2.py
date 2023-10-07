# Exercises: Level 2

# Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description. The same goes for expenses.

class PersonAccount:
    def __init__(self, firstname, lastname) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []

    def total_income(self):
        total = [x["income"] for x in self.incomes]
        return sum(total)

    def total_expense(self):
        total = [x["expense"] for x in self.expenses]
        return sum(total)

    def account_info(self):
        return f'firstname : {self.firstname}\nlastname : {self.lastname}\nincomes : {self.incomes}\nexpenses : {self.expenses}'

    def add_income(self, income, description):
        self.incomes.append({"income": income, "description": description})

    def add_expense(self, expense, description):
        self.expenses.append({"expense": expense, "description": description})

    def account_balance(self):
        return self.total_income() - self.total_expense()


p = PersonAccount("Twinkle", "Patel")
p.add_income(25000, "Salary")
p.add_income(2500, "Interest")
p.add_income(1500, "Bonus")
p.add_expense(12500, "House rent")
p.add_expense(1200, "Grocery")
p.add_expense(1000, "Pay loan")
print("Account Info :", p.account_info())
print("Total income : ", p.total_income())
print("Total expense : ", p.total_expense())
print("Account balance :", p.account_balance())
