import random


class InvalidInput(Exception):
    pass


def user_hit(monster):
    if monster == "goblin":
        return random.randint(5, 20)
    elif monster == "orc":
        return random.randint(12, 40)
    else:
        return random.randint(25, 100)


def monster_hit(monster):
    if monster == "goblin":
        return random.randint(1, 9)
    elif monster == "orc":
        return random.randint(5, 19)
    else:
        return random.randint(10, 42)


user_health = 100
monsterdict = {"goblin": 30,
               "orc": 80,
               "dragon": 200}
monsters = ["goblin", "orc", "dragon"]
moves = {"h": "Hit", "d": "Doge"}
fight = ["h", "d"]

print("You are an adventurer, who is lost in woods full of monsters.\n"
      "You hear some noises from not so far and decided to check it out.\n"
      "You saw a monster there......\n")

while True:
    try:
        choice = input("Enter your choice fight the monster or quit (f/q):")
        if choice.lower() == "f":
            mons_typ = random.choice(monsters)
            mons_health = monsterdict[mons_typ]
            print()
            print(mons_typ, mons_health)
            
            while True:
                user_fight_choice = input("hit or dodge or quit or any other key to exit this fight(h/d/q):")
                print()
                mons_choice = random.choice(fight)
                
                if user_fight_choice in fight:
                    if user_fight_choice.lower() == mons_choice == "h":
                        usr_damage = user_hit(mons_typ)
                        mons_health -= usr_damage
                        mons_damage = monster_hit(mons_typ)
                    
                        if mons_health <= 0:
                            monsters.pop(monsters.index(mons_typ))
                            print(f"You slayed the {mons_typ}.\n"
                                  f"Your health has been restored.")
                            user_health = 100
                            if monsters:
                                play_again = input("Do you want to continue fighting monsters? (y/n): ").lower()
                                if play_again == 'y':
                                    break
                                elif play_again == "n":
                                    exit()
                                else:
                                    raise InvalidInput
                            else:
                                raise IndexError
                    
                        else:
                            user_health -= mons_damage
                            print(f"monster health:{mons_health}, damage done: {usr_damage}\n"
                                  f"user health:{user_health}, damage done: {mons_damage}")
                            print()
                        
                            if user_health <= 0:
                                print("You died!!!!!!!!\n"
                                      f"The {mons_typ} was too strong for you to handle.")
                                exit()
                
                    elif user_fight_choice == "d":
                        print("You chose to doge")
                    
                    elif mons_choice == "d":
                        print(f"{mons_typ} chose to doge")
                
                elif user_fight_choice == "q":
                    print("What a loser!!!!!")
                    exit()
                
                else:
                    break
        
        elif choice.lower() == "q":
            print("\nWhat a loser!!!!!")
            exit()
        
        else:
            raise InvalidInput
    
    except InvalidInput:
        print("\nPlease enter a valid input")
    
    except IndexError:
        print("\nCongratulations!!! you have sucessfully defeated all the monsters")
        exit()
