#Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = input("Enter side a : ")
side_b = input("Enter side b : ")
side_c = input("Enter side c : ")
perimeter = int( side_a ) + int( side_b ) + int( side_c )
print ('The perimeter of the triangle is ',perimeter)