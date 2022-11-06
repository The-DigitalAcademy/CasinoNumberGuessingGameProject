import random
        
balance = int(input("Enter a wager amount: R"))
comp_num = random.randint(1, 10)

while balance > 0:
    user_input = int(input("Enter a number between 1 and 10: "))
    if user_input == comp_num:
        balance += 1
        print("Congratulations, You have won!!!")
        
        
    elif user_input != comp_num:
        balance -= 1
        print("Oops, You have lost, try again!!!")
        print("The number you have guessed was: ", user_input)
        print("The computer number was: ", comp_num)
        print("You have: R" + str(balance) + " funds remaining")
        
if balance == 0:
    print("Sorry, You have insufficient funds, Bye!")
   deposit_amount = int(input("Enter a deposit amount"))
        print("Your new balance is:",balance+deposit_amount)
