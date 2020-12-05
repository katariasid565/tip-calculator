#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill (In American $)? $ "))

tip = int(input("How much tip would you like to give(in %)? 5 , 10 , 12? "))

people = int(input("How many people to split the bill? "))

tip_as_percent = tip / 100

total_tip_amount = bill * tip_as_percent 

total_bill = bill + total_tip_amount

bill_per_person = total_bill / people

final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")

print(f"The total amount to be paid is = ${total_bill}")

print("Thank you for using it!")