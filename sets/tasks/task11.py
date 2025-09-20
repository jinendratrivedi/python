# wap to remove all strings of sets which starts with "b"
s={"abc","bob","ball","hiiiii","basket"}


for i in s.copy():
    if i[0]=="b":
        s.remove(i)

print("afte removing sets:",s)        