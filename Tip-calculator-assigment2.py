#Vincent OChieng  SCT211-0070/2022

total_bill = float(input("Enter the total bill amount: "))
tip_percentage = int(input("Enter the tip percentage (10, 12, or 15): "))
num_people = int(input("Enter the number of people splitting the bill: "))

def calculate_tip_and_split_bill(total_bill, tip_percentage, num_people):
    tip_amount = (total_bill * tip_percentage) / 100

    total_amount = total_bill + tip_amount

    per_person_amount = total_amount / num_people

    return per_person_amount

per_person_amount = calculate_tip_and_split_bill(total_bill, tip_percentage, num_people)
print(f"Each person should pay: ${per_person_amount:.2f}")


