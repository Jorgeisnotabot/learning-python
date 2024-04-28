import datetime
birth_year = input("Enter your birth year ")
now = datetime.datetime.now()
current_year = now.year
numeric_birth_year = int(birth_year)
age = current_year - numeric_birth_year
print(age)