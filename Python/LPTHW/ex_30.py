people = 30
cars = 40
buses = 15 # some variables that contains some values

if cars > people: # if else-if statment, three branchs for decision making
    print "We should take the cars."

elif cars < people:
    print "We should not take the cars."

else:
    print "We can't decide."

if buses > cars: # if else-if statment, three branchs for decision making
    print "That's too many buses."
elif buses< cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."
