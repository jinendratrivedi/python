#  Given a string, count the frequency of each character using a dictionary.
 
str="programming"
#output-> {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}

f={}

for i in str:
  f[i]=f.get(i,0)+1

print("charcter frequency",f)        
