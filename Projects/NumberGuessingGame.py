import random
import math
print("Please Enter the range of numbers you want to play in!")
upper,lower=map(int,input().split())
print("Your chosen range is:",lower,upper)
num=random.randint(lower,upper)
min_guesses=math.ceil(math.log2(upper-lower+1))
print(f"You have {min_guesses} number of total guesses.Use wisely!")
guesses=0
while guesses<min_guesses:
    print("Guess the number:")
    guessed_num=int(input())
    
    if guessed_num<num:
        print("Try Again!You guessed too small")
        guesses+=1
    if guessed_num>num:
        print("Try Again! You guessed too high")
        guesses+=1
    if guessed_num==num:
        print("Congratulations!The number is",num)
        break
    
if guessed_num!=num and guesses==min_guesses:
    print(f"Better Luck next time.The number was {num}")