# Reverse a string using recursion.

def rev(s):
    if len(s)==0:
        return ""
    return rev(s[1:])+s[0]

print(rev("hello"))