# print(dir(list))
# dunder : double underscore methods

def add():
    print()
    print("Inside add")
    print("i m exporting...")
    print()


def getData():
    print()
    print("INside getData ")
    print("Get Data Exporing")
    print()

# add()
# getData()

print("######--> ",__name__)

if (__name__ == '__main__'):
    add()
    getData()


