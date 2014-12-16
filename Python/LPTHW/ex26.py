def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words): #forget colon
    """Prints the first word after popping it off."""
    word = words.pop(0)   #miss spell pop
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1) #miss right parentheses
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 6 #math error 10 - 2 + 3 - 5 = 6
print "This should be five: %d" % five # %s stands for string so there can use %d stands for decimal

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000 #operator use mistake '/' stands for disivion instead of '\'
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point) #mistake '-' and '_' and "=="

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates) #spelling mistake in strings 'jeans'

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point) #misspelling 'point'



sentence = "All good things come to those who wait." #I thought it occurs some mis-spelling

words = break_words(sentence) #There is no necessarily to use ex25. beacuse the funciton is defined in the same file
sorted_words = sort_words(words) #Same reason 

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words) #Stop punctuation is not necessary
print_last_word(sorted_words)
sorted_words = sort_sentence(sentence) #ex25. is not necessary
print sorted_words #Misspelling print

print_first_and_last(sentence) #Misspelling function name

print_first_and_last_sorted(sentence) #No necessary indent and misspelling function name
