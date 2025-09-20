# Find characters that are unique to each of two strings.
str1="hello"
str2="world"

s1=set(str1)
s2=set(str2)

print("unique elements in str1:",s1.symmetric_difference(s2))