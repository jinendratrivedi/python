# waf to print strings using arbitary arguments

def strings(*args):
    for i in args:
        print(i)
strings("hi","hello","bye")
strings("hi","hello","bye","good")

        