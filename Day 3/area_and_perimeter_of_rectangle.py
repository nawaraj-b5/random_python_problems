#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

length = input( 'Enter the length of rectangle : ' )
width = input( 'Enter the width of rectangle : ' )
area = int( length ) * int ( width )
perimeter = 2 * ( int( length ) + int( width ) )
print( 'Area is : ',area )
print( 'Perimeter is : ',perimeter )