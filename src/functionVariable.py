# encoding: utf-8

# this one is like your scripts with argv
def print_two(*args):
    # using _ to avoid too many vlaues to unpack
    arg1, arg2,_,_ = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothin'."


#print_two("one","two","three")
print_two("one","two","three","four")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
