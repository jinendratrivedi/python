#wap to input a string and find the longest length of string

str=input("enter the string:")
words=str.split(" ")
print(words)
maxlen=len(words[0])

for i in words:
    if len(i)>maxlen:
        maxlen=len(i)

print(maxlen)        


