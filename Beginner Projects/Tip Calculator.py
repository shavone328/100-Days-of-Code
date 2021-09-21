# Tip Calculator
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
#print(total_bill)
percentage = int(input("What percentage would you like to give? 10, 12, or 15? "))
#print(percentage)
number_of_people = int(input("How many people to split the bill? "))
#print(number_of_people)

tip = percentage/100
total_tip = total_bill*tip

bill_per_person = (total_bill+total_tip)/number_of_people
final = round(bill_per_person,2)
print(f"Each person pays ${final}")



