#do the addition(+) subtraction(-) multiplication(*) modulus(%) division(/) exponential(**) floor division operator(//) operations by the help of user input
a = input('Enter first number:') #gets first number from user
b = input('Enter second number:') #gets second number from user
sum = int(a)+int(b)
difference = int(a)-int(b)
multiplication = int(a)*int(b)
modulus = int(a)%int(b)
division = int(a)/int(b)
exponential = int(a)**int(b)
floor_division = int(a)//int(b)
print('The sum of {} and {} is {}'.format(a,b,sum))
print('The difference between {} and {} is {}'.format(a,b,difference))
print('The multiplication of {} and {} is {}'.format(a,b,multiplication))
print('The modulus of {} and {} is {}'.format(a,b,modulus))
print('The division of {} and {} is {}'.format(a,b,division))
print('The exponential  of {} and {} is {}'.format(a,b,exponential))
print('The floor_division  of {} and {} is {}'.format(a,b,floor_division))
