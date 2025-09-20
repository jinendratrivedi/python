# take list from user append all element in list and print longest word in list  
#         input : ["java", "python", "php","cpp","flutter"]
#         output :  flutter

li=["java", "python", "php","cpp","flutter"]

max = li[0]

for i in li:
    if len(i) > len(max):
        max = i

print("longest word is:",max)        