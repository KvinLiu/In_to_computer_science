# Implicit Inheritance
"""
class Parent(object):
    def implicit(self):
        print "PARENT implicit()"

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
"""
# Override Explicity
"""
class Parent(object):
    def override(self):
        print "PARENT override()"

class Child(Parent):
    def override(self):
        print "CHILD override()"

dad = Parent()
son = Child()

dad.override()
son.override()
"""
# Alter Before or After

class Parent(object):
    def altered(self):
        print "PARNET altered()"

class Child(Parent):
   # def __init__(self):
       # super(Child,self).__init__()

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.altered()
son.altered()
