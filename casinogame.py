import random
        
wager_input = int(input("Enter a wager amount: R"))
comp_num = random.randint(1, 10)

while wager_input > 0:
    user_input = int(input("Enter a number between 1 and 10: "))
    if user_input == comp_num:
        wager_input += 1
        print("Congratulations, You have won!!!")
        
    elif user_input != comp_num:
        wager_input -= 1
        print("Oops, You have lost, try again!!!")
        print("The number you have guessed was: ", user_input)
        print("The computer number was: ", comp_num)
        print("You have: R" + str(wager_input) + " funds remaining")
        
if wager_input == 0:
    print("Sorry, You have insufficient funds, Bye!")
        
