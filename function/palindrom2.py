# waf to check that all elemnts of list is palindrome or not

def is_palindrome(li):
    for i in li:
        if i==i[::-1]:
            print("palindrome")
        else:
            print("not palindrome")

is_palindrome(["hii","madam","hello","nayan"])            