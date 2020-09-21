'''Draw following pattern
*
**
***
****
*****
****
***
**
*
'''
star = '*'
max_line = int(input("Enter the max line to display the pattern: "))
star_length=len(star)
while star_length<=max_line-1:  #run the loop until it reaches max_line-1
    print(star)                 # first star is auto printed
    star=star+'*'               #increment size of star
    star_length=star_length+1   #star length increment
while star_length > 0:          #if star is less more then 0
    star=star_length*'*'        #multiplication of string *  with star length
    print(star)                 #print star immidiately
    star_length=star_length-1   #decrement in length of star to narrow down the while loop