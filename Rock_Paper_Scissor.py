import random
import time


class ChoiceError(Exception):
    pass


print("Welcome to the Rock Paper Scissors Game")
while True:
    rps = ["R", "P", "S"]
    comp = random.choice(rps)
    print()
    time.sleep(0.8)
    print("Press 'R' to select Rock \n"
          "Press 'S' to select Scissors \n"
          "Press 'P' to select Paper \n"
          "Press 'E' to Exit")
    
    try:
        human = input("Enter Your Choice: ")
        human = human.upper()
        print()
        
        if human == "E":
            time.sleep(0.8)
            print("GOODBYE.........")
            exit()
        
        time.sleep(0.8)
        print("Computer is choosing.......")
        print()
        time.sleep(2)
        dic = {"R": "ROCK", "S": "SCISSORS", "P": "PAPER"}
        if human == comp:
            print(f"You and computer both chose {dic[human]} \n"
                  f"It's a TIE!!!!")
            time.sleep(2)
            print()
            print("Press 'Y' to play again or \n"
                  "Press 'Enter' to exit")
            play_more = input("Enter your choice:")
            play_more = play_more.upper()
            if play_more == "Y":
                continue
            else:
                exit()
        elif (human == "R" and comp == "S") or (human == "S" and comp == "P") or (human == "P" and comp == "R"):
            print(f"You chose {dic[human]} \n"
                  f"Computer chose {dic[comp]} \n"
                  f"You WON!!!!")
            time.sleep(2)
            print()
            print("Press 'Y' to play again \n"
                  "Press 'Enter' to exit")
            play_more = input("Enter your choice:")
            play_more = play_more.upper()
            if play_more == "Y":
                continue
            else:
                exit()
        elif (comp == "R" and human == "S") or (comp == "S" and human == "P") or (comp == "P" and human == "R"):
            print(f"You chose {dic[human]} \n"
                  f"Computer chose {dic[comp]} \n"
                  f"You LOST!!!!")
            time.sleep(2)
            print()
            print("Press 'Y' to play again \n"
                  "Press 'Enter' to exit")
            play_more = input("Enter your choice:")
            play_more = play_more.upper()
            if play_more == "Y":
                continue
            else:
                exit()
        else:
            raise ChoiceError
    
    except ChoiceError:
        print("Please enter a valid choice")
        continue
