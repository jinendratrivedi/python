#wap to input a string and find the longest word of string

str=input("enter the string:")
words=str.split(" ")
longest_word = max(words,key=len)
print(longest_word)
