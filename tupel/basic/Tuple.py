# datatype :tuple
# data : list

tpl = (110,220,33,330,'royal',True,11,22,33,55,33,66,33)
lst = [11,22,33]
# print(tpl)
# print(lst)
# print(tpl[1])
# x = list(tpl)
# convert into list
# print(x)
# x.append(22)
# x.insert(2,4444)
# print(x)
# tpl = tuple(x)
# print(tpl)
nested_tpl2 = ((11,22),(33,44))
# # nesting of tuple 
print(nested_tpl2)
# print(nested_tpl2[1])
# print(nested_tpl2[0][0])
# print(nested_tpl2[0][1])
# print(nested_tpl2[1][0])
# print(nested_tpl2[1][1])

# empty = ()
# print(empty)

# single val
# single = (43)
single = (43,)

print(single)

# tp2 = tuple(x)
# print("===> ",tp2)

print(tpl)
val = tpl.index(220)
print("Index number : ",val)

count = tpl.count(33)
print(count)

print("len : ",len(tpl))
print("3 : 7" ,tpl[3:7])
print("2 : " ,tpl[3:])
print("2 : " ,tpl[:4])
print("2 : " ,tpl[:])
print("2 : " ,tpl[-4:-1])


tplNew = tpl *2
print(tplNew)
print(len(tplNew))







