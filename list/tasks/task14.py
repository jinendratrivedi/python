#wap to print only those values from list whose len is greater than 3 and 
# first and last character starts with "a"

li=["aba","ab","abba","caac","abc","mnom"]
for i in li:
 if len(i)>3 and i[0]=="a" and i[-1]=="a":
  print(i)