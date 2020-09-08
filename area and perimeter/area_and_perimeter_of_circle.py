#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

pi = 3.14
r = input( 'Enter the value of radius : ' )
area = pi * float(r) * float(r)
circumference = 2 * pi * float(r)
print(' The area of the circle is :',area )
print(' The circumference  of the circle is :',circumference )