#Write a function that takes a list of integers as a parameter and returns the sum of the list without using sum().

def item_list(list_of_integer):
    result = 0
    i= 0
    length =len(list_of_integer)
    while i < length:
        result+=list_of_integer[i]
        i+=1
    print('The sum of the {} number in the list is {}'.format(length,result))

item_list([2,3,5,7,8,4,8,5])
item_list([2,3,0,7,8,4,5])
