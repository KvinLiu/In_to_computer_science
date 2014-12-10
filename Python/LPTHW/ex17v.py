from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how

print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

open(to_file, 'w').write(open(from_file).read())

print "Alright, all done."

