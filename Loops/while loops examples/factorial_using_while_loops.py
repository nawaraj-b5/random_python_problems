#while loops
'''Syntax:
        while conditions:
            statement(s)'''

#find the factorial of the user provided number using while loop

result=1
i=1
user_input = int(input('Enter the number to find out the factorial: '))
while i<= user_input:
    result*=i
    i+=1
print('The factorial of {} is {}'.format(user_input,result))
