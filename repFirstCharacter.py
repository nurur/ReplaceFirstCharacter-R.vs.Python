# Python script to change the case (lower or upper) of the first letter of a string 


# String 
a='circulating'
print 'The string is:', a
print ''


#Method 1: splitting string into letters 
print 'Changing the first letter by splitting the string into letters'
b=list(a)
b[0] = b[0].upper()
b=''.join(b)
print b
print ' '


# Method 2: using regular expression   
print  'Changing the first letter by using regular expression'
import re

rep = lambda f: f.group(1).upper()
b   = re.sub('\A([a-z])', rep, a)     #using anchor token \A
print b

b   = re.sub('^([a-z])', rep, a)      #using anchor token ^
print b
