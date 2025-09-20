#wap to print only those values from list whose len is greater than 3 and 
# first and last character is same

li=["aba","ab","abba","caac","abc","mnom"]


for i in li:
 if len(i)>3 and i[0]==i[-1]:
  print(i)
     
