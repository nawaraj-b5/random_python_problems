#Compare the length of your first name and your last name
first_name_input = input('Enter first name : ')
last_name_input = input('Enter last name : ')
length_of_first_name = len(first_name_input)
length_of_last_name = len(last_name_input)
first_name_has_more_length = length_of_first_name > length_of_last_name
last_name_has_more_length = length_of_last_name >length_of_first_name
both_have_equal_length =  length_of_first_name > length_of_last_name
print ("The length of first name is : {}".format( length_of_first_name) )
print("The length of last name is : {}".format(length_of_last_name) )
print("First name has more length : {}".format(first_name_has_more_length) )
print("Last name has more length : {}".format(last_name_has_more_length) )
print("First name and Last name have equal length :{}".format(both_have_equal_length) )