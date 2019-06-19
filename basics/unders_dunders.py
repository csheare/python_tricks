'''
This is mostly just notes about underscores and dunders for myself
'''

# 1.  Single Leading Underscores
# underscores are basically just a hint to the programmer for internal used
# convention is not enforced by the interpretor
# no public or private in python
# usually a leading underscore doesnt matter unless you define a module with an _function and then try to import it with from module import *, the _ will not come

# 2. Single Trailing Underscores
#  generally used as a postfix for naming things that conflict with keywords in python

# 3. Double Leading Underscore: __var
# this prefix cause the Python Interpretor to rewrite the attribute name in order ti avoid naming conflict in subclasses
# this is called name mangling - the interpretor changes the name of the variable in a way that makes it harder to create collisons when the class is extended later

class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 50

class ExtendedTest(Test):
    def __init__(self):
        super().__init__()
        self.foo = 'overridden'
        self._bar = 'overridden'
        self.__baz = 'overridden'

#t = Test()
#dir(t)

#t2 = ExtendedTest()
#print(t2.foo)
#print(t2._bar)
#print(t2.__baz)
#print(t2._ExtendedTest__baz)
