# waf to check string is palindrome

def is_palindrome(s):
    if s==s[::-1]:
        print("palindrome")
    else:
        print("not palindrome")

is_palindrome("madam")
is_palindrome("hello")        

