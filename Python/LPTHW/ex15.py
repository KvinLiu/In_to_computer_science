from sys import argv #Import module from labriary

script, filename = argv #To make varible to argument varibles

txt = open(filename) #Give the txt varible the file contents

print "Here's your file %r:" % filename #Give a prompt in English
print txt.read() #Use .read() method to read file contents

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()