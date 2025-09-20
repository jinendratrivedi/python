# wap to make a func girl() and another func boy()
# call function boy() when user input 'b' and call func girl() when user inputs 'g'

def girl():
    print('it is girl')
    print('she is beautiful')
    print('she is smart')

def boy():
    print('it is boy')
    print('he is handsome')
    print('he is smart')

a=input('enter a character:').lower()

if a=='b':
    boy()

elif a=='g':
    girl()

else:
    print('invalid character')    