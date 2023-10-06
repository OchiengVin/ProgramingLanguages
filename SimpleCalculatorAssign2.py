#Vincent OChieng  SCT211-0070/2022

import datetime

yearOfBirth = int(input("Enter your year of birth: "))
birthDate = datetime.date(yearOfBirth, 1, 1)
currentDate = datetime.date.today()
ageInYears = currentDate.year - birthDate.year
ageInMonths = currentDate.month - birthDate.month
ageInDays = currentDate.day - birthDate.day

print(f"Age is: {ageInYears} years, {ageInMonths} months, and {ageInDays} days.")

