x = "There are %d types of people." % 10 #Define x, and give it a string, use special fomatter
binary = "binary" # Define binary as a string.
do_not = "don't" # Define 'do_not' and give it string "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x 
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e