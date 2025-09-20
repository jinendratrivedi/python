# *
# * *
# * * *
# * * * *

def pattern():
    for i in range(1,6):
        print(" * " * i)

pattern()


#      *
#     * *
#    * * * 
#   * * * *
#  * * * * *  


#      *
#     **
#    ***
#   ****  

# def paternTriangle():
#     for i in range(1,6):
#         for j in range(1,i+1):
#             print("*", end='')
#         print()   
        
# paternTriangle()


def paternTriangle():

    for i in range (6):
        for j in range(6-i):
            print(" ",end="")
        for k in range(i):
            print("* ",end="")
        print()   

paternTriangle()