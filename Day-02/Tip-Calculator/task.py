print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people=int(input("enter the number of people"))
total=(tip/100)*bill+bill
bill_per_person=round(total/people,2)
print(f"each person bill is {bill_per_person}")
