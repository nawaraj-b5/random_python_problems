#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = input("Enter base : ")
height = input("Enter height : ")
area = 0.5 * int( base ) * int( height )
print("The area of the triangle is :", area )