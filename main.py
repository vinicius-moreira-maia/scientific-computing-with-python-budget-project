import budget
from budget import create_spend_chart

food = budget.Category("Food")
food.deposit(100, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)

auto = budget.Category("Auto")
auto.deposit(100, "initial deposit")
auto.withdraw(15)

academia = budget.Category("Academia")
academia.deposit(200, "initial deposit")
academia.withdraw(70, "creatina")
academia.withdraw(35, "luvas")

print(food)
print(clothing)
print(auto)
print(academia)

print(create_spend_chart([food, clothing, auto, academia]))