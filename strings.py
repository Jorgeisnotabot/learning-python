# EXAMPLES OF STRING FUNCTIONS
course = 'Working with strings in Python'

# Uppercase, lowercase, capitalize
name = input('Enter your name ')
email = input('Enter your email ')
country = input('Enter your country ')
countryAcronym = country.replace('mexico', 'mx')
print(f'Welcome {name.capitalize()} and your email is {email.lower()} and your country is {country.upper()} ({countryAcronym})')
print(email.find('@'))

# in operator

print('Working' in course)

