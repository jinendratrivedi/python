import random

number = random.randint(1, 100)
print("Guess the number between 1 and 100")
count = 11
for i in range(11):
    count = count-1
    if count==0:
     print("Game over. The number was:", number)
     break
    guess = int(input(f"Attempt {count}/10 - Your guess: "))
    
    if guess == number:
        print("Correct! You guessed it!")
        break

    if guess < number:
        print("Too low!")
    else:
        print("Too high!")
    
   

