#Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = input('Enter hours : ')
rpr = input('Enter rate per hour : ')
weekly_earning = int(hours) * int( rpr )
print('The weekly earning is :',weekly_earning)