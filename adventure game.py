import random
import math

name = input("Type your name: ")
print("Welcome", name + "!")
print("You enter the dungeon and find a half-beaten blade and 3 potions.")
getIt = input("Do you want to pick the items? (yes/no) ").lower()

options = ["attack", "potion", "defend", "run"]
directions = ["north", 'east', "south", "west"]

HP = 120
attack = 2
potions = 0
tick = 0
gamescore = 0

if getIt == "yes":
    print("You equipped the items.")
    print("Attack: 7")
    print("Available potions: 3")
    attack = 7
    potions = 3
elif getIt == "no":
    print("You ignored the items and went in.")
    print("Attack: 2")
    print("Available potions: 0")
else:
    print("You started speaking gibberish and a monster came to attack you!")
    print("A Phoenix traps you in its embers!")
    print("HP: 777")
    p_HP = 777
    p_att = 100
    while True:
        print("Attack     Potion")
        print("Defend     Run")
        action = input("What do you wish to do? ").lower()
        if action not in options:
            print("You panicked hard, and the Phoenix proceeded to burn you to death....")
            print("Game over...")
            quit()
        else:
            if action == "attack":
                print("=====================================")
                print("You dealt", attack, "damage")
                p_HP -= attack
                print("Phoenix HP:", p_HP)
                print("=====================================")
                if p_HP <= 0:
                    print("You defeated the Phoenix!")
                    break
                print("=====================================")
                print("Phoenix attacks!")
                print("Phoenix dealt", p_att, "damage")
                print("=====================================")
                HP -= p_att
                if HP <= 0:
                    print("=====================================")
                    print("You died...")
                    print("=====================================")
                    break
                print("=====================================")
                print(name, "HP:", HP)
                print("=====================================")
            elif action == "potion":
                if potions > 0:
                    print("=====================================")
                    print("You used a potion")
                    potions -= 1
                    HP += 50
                    if HP > 120:
                        HP = 120
                        healed = 50
                    else:
                        healed = 50
                    print(f"You healed: {healed}")
                    print(name, "HP:", HP)
                    print("=====================================")
                else:
                    print("=====================================")
                    print("No potions")
                    print("=====================================")
            elif action == "defend":
                print("=====================================")
                print("Incoming damage reduced by half!")
                print("Phoenix attacks!")
                print("Phoenix dealt", (p_att * 0.5), "damage")
                print("=====================================")
                HP -= (p_att * 0.5)
                if HP <= 0:
                    print("=====================================")
                    print("You died...")
                    print("=====================================")
                    break
                print("=====================================")
                print(name, "HP:", HP)
                print("=====================================")
            else:
                print("=====================================")
                print("You tried to run, but you died to the flames of the Phoenix...")
                print("Game over...")
                print("=====================================")
                quit()

while True:
    print("=====================================")
    print("North     East")
    print("South     West")
    print("=====================================")
    direction = input("Which way do you wish to go? ").lower()
    print("=====================================")

    if direction not in directions:
        print("=====================================")
        print("The Warden is approaching. Better take a direction.")
        print("=====================================")
        tick += 1
        if tick == 5:
            chance = random.randint(0, 1)
            w_HP = 666
            w_att = 444
            print("=====================================")
            print("The Warden now stares you down")
            print("Warden HP:", w_HP)
            print("Warden attack:", w_att)
            print("=====================================")
            if chance == 1:
                print("=====================================")
                print("The Warden takes the initiative")
                print("The Warden dealt", w_att, "damage")
                print("You died...")
                print("=====================================")
                break
            else:
                print("=====================================")
                print("Attack     Potion")
                print("=====================================")
                action = input("What do you wish to do? ").lower()
                print("=====================================")
                if action not in options:
                    print("=====================================")
                    print("You panicked hard, and the Warden sents death upon you...")
                    print("Game over...")
                    print("=====================================")
                    break
                else:
                    if action == "attack":
                        print("=====================================")
                        print("You dealt", attack, "damage")
                        w_HP -= attack
                        print("Warden HP:", w_HP)
                        print("=====================================")
                        if w_HP <= 0:
                            print("=====================================")
                            print("You defeated the Warden!")
                            print("=====================================")
                            break
                        print("=====================================")
                        print("Warden attacks!")
                        print("Warden dealt", w_att, "damage")
                        print("=====================================")
                        HP -= w_att
                        if HP <= 0:
                            print("=====================================")
                            print("You died...")
                            print("=====================================")
                            break
                        print("=====================================")
                        print(name, "HP:", HP)
                        print("=====================================")
                    elif action == "potion":
                        if potions > 0:
                            print("=====================================")
                            print("You used a potion")
                            potions -= 1
                            HP += 50
                            if HP > 120:
                                HP = 120
                            healed = 50
                            print("You healed:", healed)
                            print(name, "HP:", HP)
                            print("=====================================")
                        else:
                            print("=====================================")
                            print("No potions")
                            print("=====================================")
                    else:
                        print("=====================================")
                        print("No potions")
                        print("=====================================")
                        continue

    elif direction == "north":
        chance = random.randint(0, 4)  # 1/5
        randoHP = random.randint(-5, 5)
        randoAtt = random.randint(-3, 2)
        if chance == 2:
            print("=====================================")
            print("A monster appears!")
            m_HP = 30 + randoHP
            m_att = 2 + randoAtt
            print("Monster HP:", m_HP)
            print("Monster Attack:", m_att)
            print("=====================================")
            while True:
                print("=====================================")
                print("Attack     Potion")
                print("Defend     Run")
                print("=====================================")
                action = input("What do you wish to do? ").lower()
                print("=====================================")
                if action not in options:
                    print("=====================================")
                    print("You panicked hard, and the monster beat you to death.")
                    print("Game over...")
                    print("=====================================")
                    break
                else:
                    if action == "attack":
                        print("=====================================")
                        print("You dealt", attack, "damage")
                        m_HP -= attack
                        print("Monster HP:", m_HP)
                        print("=====================================")
                        if m_HP <= 0:
                            print("=====================================")
                            print("You defeated the monster!")
                            print("=====================================")
                            randomScore = random.uniform(0, 2)
                            gamescore += math.floor(43 * randomScore)
                            break
                        print("=====================================")
                        print("Monster attacks!")
                        print("Monster dealt", m_att, "damage")
                        print("=====================================")
                        HP -= m_att
                        if HP <= 0:
                            print("=====================================")
                            print("You have died.")
                            print("Game over...")
                            print("=====================================")
                            break
                        print("=====================================")
                        print(name, "HP:", HP)
                        print("=====================================")
                    elif action == "potion":
                        if potions > 0:
                            print("=====================================")
                            print("You used a potion")
                            print("=====================================")
                            potions -= 1
                            HP += 50
                            if HP > 120:
                                HP = 120
                            healed = 50
                            print("=====================================")
                            print(f"You healed: {healed}")
                            print(name, "HP:", HP)
                            print("=====================================")
                        else:
                            print("=====================================")
                            print("No potions")
                            print("=====================================")
                    elif action == "defend":
                        print("=====================================")
                        print("Incoming damage reduced by half!")
                        print("Monster attacks!")
                        print("Monster dealt", (m_att * 0.5), "damage")
                        print("=====================================")
                        HP -= (m_att * 0.5)
                        if HP <= 0:
                            print("=====================================")
                            print("You have died.")
                            print("Game over...")
                            print("=====================================")
                            break
                        print(name, "HP:", HP)
                    else:
                        runchance = random.randint(0, 1)  # 1/2
                        if runchance == 1:
                            print("=====================================")
                            print("Successfully ran away.")
                            print("=====================================")
                            break
                        else:
                            print("=====================================")
                            print("Failed!")
                            print("=====================================")
                            continue
    elif direction == "east":
        chance = random.randint(0, 4)  # 1/5
        randoAtt = random.randint(-3, 3)
        if chance == 1:
            print("=====================================")
            print("You found a unique item")
            item = attack + randoAtt
            print("Another sword:", item, "attack")
            print("=====================================")
            action = input("Do you want to take it? (yes/no) ").lower()
            print("=====================================")
            if action == "yes":
                print("=====================================")
                print("Equipped!")
                attack = item
                print(name + "'s attack:", attack)
                print("=====================================")
            else:
                print("=====================================")
                print("Left it.")
                print("=====================================")
        elif chance == 2:
            print("=====================================")
            print("Found 1 potion")
            potions += 1
            print("Available potions:", potions)
            print("=====================================")
    elif direction == "south":
        chance = random.randint(0, 1)  # 1/2
        if chance == 1:
            print("=====================================")
            print("Found 2 potions")
            potions += 2
            print("Available potions:", potions)
            print("=====================================")
        else:
            ask = str(input("Do you wish to exit? (yes/no) ")).lower()
            print("=====================================")
            if input == "yes":
                break
            else:
                print("=====================================")
                print("The Warden is approaching. Better take a direction.")
                print("=====================================")
                tick += 1
    elif direction == "west":
        chance = random.randint(0, 4)  # 1/5
        randoAtt = random.randint(-3, 2)
        if chance == 2:
            print("=====================================")
            print("A monster appears!")
            m_HP = 30
            m_att = 2 + randoAtt
            print("Monster HP:", m_HP)
            print("Monster Attack:", m_att)
            print("=====================================")
            while True:
                print("=====================================")
                print("Attack     Potion")
                print("Defend     Run")
                print("=====================================")
                action = input("What do you wish to do? ").lower()
                print("=====================================")
                if action not in options:
                    print("=====================================")
                    print("You panicked hard, and the monster beat you to death.")
                    print("Game over...")
                    print("=====================================")
                    break
                else:
                    if action == "attack":
                        print("=====================================")
                        print("You dealt", attack, "damage")
                        m_HP -= attack
                        print("Monster HP:", m_HP)
                        print("=====================================")
                        if m_HP <= 0:
                            print("=====================================")
                            print("You defeated the monster!")
                            print("=====================================")
                            randomScore = random.uniform(0, 2)
                            gamescore += math.floor(43 * randomScore)
                            break
                        print("=====================================")
                        print("Monster attacks!")
                        print("Monster dealt", m_att, "damage")
                        print("=====================================")
                        HP -= m_att
                        if HP <= 0:
                            print("=====================================")
                            print("You have died.")
                            print("Game over...")
                            print("=====================================")
                            break
                        print("=====================================")
                        print(name, "HP:", HP)
                        print("=====================================")
                    elif action == "potion":
                        if potions > 0:
                            print("=====================================")
                            print("You used a potion")
                            potions -= 1
                            HP += 50
                            if HP > 120:
                                HP = 120
                            healed = 50
                            print(f"You healed: {healed}")
                            print(name, "HP:", HP)
                            print("=====================================")
                        else:
                            print("=====================================")
                            print("No potions")
                            print("=====================================")
                    elif action == "defend":
                        print("=====================================")
                        print("Incoming damage reduced by half!")
                        print("Monster attacks!")
                        print("Monster dealt", (m_att * 0.5), "damage")
                        print("=====================================")
                        HP -= (m_att * 0.5)
                        if HP <= 0:
                            print("=====================================")
                            print("You have died.")
                            print("Game over...")
                            print("=====================================")
                            break
                        print("=====================================")
                        print(name, "HP:", HP)
                        print("=====================================")
                    else:
                        runchance = random.randint(0, 1)  # 1/2
                        if runchance == 1:
                            print("=====================================")
                            print("Successfully ran away.")
                            print("=====================================")
                            break
                        else:
                            print("=====================================")
                            print("Failed!")
                            print("=====================================")
                            continue

print("Your score is:", gamescore)
print("GG")