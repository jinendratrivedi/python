    # * * * * *
    # * * * *
    # * * *
    # * *
    # *

# def pattern8(n):
#     for i in range(n, 0, -1):
#         for j in range(i):
#             print("*", end=" ")
#         print()

# pattern8(5)

for i in range(5,0,-1): 
    for j in range(1,i+1):
        print("*", end=" ")
    print()

