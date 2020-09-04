#The radius of a circle is 30 meters.
radius=30
area_of_circle = 3.14 * radius ** 2     #Calculate the area of a circle and assign the value to a variable area_of_circle
circum_of_circle = 2* 3.14 * radius     #Calculate the circumference of a circle and assign the value to a variable circum_of_circle
print(area_of_circle)
print(circum_of_circle)

#Take radius as user input and calculate the area.
radius_from_user_input = int( input('Enter the radius of the circle: ') )
area_of_circle_by_user = 3.14 *radius_from_user_input**2
print( 'The area of the user defined radius is {}'.format( area_of_circle_by_user ) )