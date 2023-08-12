import random

print('welcome to the game of snake water gun')
print("lets play the game")

list = ["snake", "water", "gun"]
user_won=0
cpu_won=0
no_of_chance=0
chance=5
while no_of_chance<chance:
    user=input('snake,water,gun:')
    choice1 = random.choice(list)


    if user==choice1:
       print("you both choice the same ")

    elif user=="snake" and choice1=="water":
       user_won = user_won + 1
       print(f"your guess {user} and computer guess {choice1}\n")
       print("user win")
       print(f"computer_points is {cpu_won} and user point is {user_won}\n")
    elif user == "snake" and choice1=="gun":
       cpu_won = cpu_won + 1
       print(f"your guess {user} and computer guess {choice1}\n")
       print("cpu win")
       print(f"computer_points is {cpu_won} and user point is {user_won}\n")

    elif user=="water" and choice1=="snake":
       cpu_won = cpu_won + 1
       print(f"your guess {user} and computer guess {choice1}\n")
       print("cpu win")
       print(f"computer_points is {cpu_won} and user point is {user_won}\n")


    elif user == "water "and choice1=="gun":
       user_won = user_won + 1
       print(f"your guess {user} and computer guess {choice1}\n")
       print("user win")
       print(f"computer_points is {cpu_won} and user point is {user_won}\n")

    elif user == "gun" and choice1=="water":
       cpu_won = cpu_won + 1
       print(f"your guess {user} and computer guess {choice1}\n")
       print("cpu win")
       print(f"computer_points is {cpu_won} and user point is {user_won}\n")


    elif user == "gun" and choice1=="snake":
       user_won = user_won + 1
       print(f"your guess {user} and computer guess {choice1}\n")
       print("user win")
       print(f"computer_points is {cpu_won} and user point is {user_won}\n")
    else:
        print("invalid!")
    no_of_chance = no_of_chance+1
    print(f"{chance - no_of_chance} is left out of {chance}\n")


    print("game over")


    if user_won>cpu_won:
          print("user won")
    elif user_won<cpu_won:
         print("soory cpu won")
    else:
       print("user and comp both have same score ")
    print(f"your points is {user_won} and computer points is {cpu_won}")



