income = int(input("What was your income this month?"))

rent = int(input("How much money you spend on your apartment rental?"))
groceries = int(input("How much money you spend on groceries?"))
transport = int(input("How much money you spend on transport?"))
entertainment = int(input("How much money you spend on entertainment?"))

total_expances = rent + groceries + transport + entertainment
balance = income - total_expances

print(f"Income: {income}")
print (f"Total expances: {total_expances}")
print(f"Balance: {balance}")

percent_rent = (rent / income) * 100
percent_groceries = (groceries / income) * 100
percent_tranasport = (transport / income) * 100
percent_entertainment = (entertainment / income) * 100

print(f"Rent: {percent_rent:.2f} % of income")
print(f"Groceries: {percent_groceries:.2f} % of income")
print(f"Transport: {percent_tranasport:.2f} % of income")
print(f"Entertainment: {percent_entertainment:.2f} % of income")
