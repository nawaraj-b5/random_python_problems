#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume someone lives up to hundred years
years_lived = int( input('Enter number of years you have lived: ') )
seconds_lived = years_lived * 365 *24*60*60
print("You have lived {} seconds in your life.".format(seconds_lived))