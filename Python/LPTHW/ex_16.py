from sys import argv # Import a libary from sys

script, filename = argv # Assign two parameter

print "We're going to erase %r." % filename # Screen out what computer gonna do
print "If you don't want that, hit CTRL-C(^C)." # ^C is for terminal bash Or zsh to stop processing
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
#target = open(filename, 'w')
target = open(filename, 'a')

print "Truncating the file. Goodbye!"
#target.truncate() #Commit out the line, make truncate() function don't work

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
