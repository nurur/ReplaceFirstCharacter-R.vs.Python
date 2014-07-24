# R script to change the case (lower or upper) of the first letter of a string 


# String 
a='circulating'
cat('The string is:', a, '\n')
cat('\n')



# Method 1: Perl type regular expression
cat('Changing the first letter by using regular expression', '\n')

b = gsub('\\b([a-z])', '\\U\\1', a, perl=T)  #using anchor token \\b
cat(b, '\n')

b = gsub('^([a-z])', '\\U\\1', a, perl=T)    #using anchor token ^
cat(b, '\n')


