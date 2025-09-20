#wap print only those string which starts and ends with "a" in the list
li = ['abc', 'xyz',"acca",'aba', '1221',"a","moon","mom"]


for i in li:
    if i[0]=='a' and i[-1]=='a' :
        print(i)


