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
                print("You dealt", attack, "damage")
                p_HP -= attack
                print("Phoenix HP:", p_HP)
                if p_HP <= 0:
                    print("You defeated the Phoenix!")
                    break
                print("Phoenix attacks!")
                print("Phoenix dealt", p_att, "damage")
                HP -= p_att
                if HP <= 0:
                    print("You died...")
                    break
                print(name, "HP:", HP)
            elif action == "potion":
                if potions > 0:
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
                else:
                    print("No potions")
            elif action == "defend":
                print("Incoming damage reduced by half!")
                print("Phoenix attacks!")
                print("Phoenix dealt", (p_att * 0.5), "damage")
                HP -= (p_att * 0.5)
                if HP <= 0:
                    print("You died...")
                    break
                print(name, "HP:", HP)
            else:
                print("You tried to run, but you died to the flames of the Phoenix...")
                print("Game over...")
                quit()

while True:
    print("North     East")
    print("South     West")
    direction = input("Which way do you wish to go? ").lower()

    if direction not in directions:
        print("The Warden is approaching. Better take a direction.")
        tick += 1
        if tick == 5:
            chance = random.randint(0, 1)
            w_HP = 666
            w_att = 444
            print("The Warden now stares you down")
            print("Warden HP:", w_HP)
            print("Warden attack:", w_att)
            if chance == 1:
                print("The Warden takes the initiative")
                print("The Warden dealt", w_att, "damage")
                print("You died...")
                break
            else:
                print("Attack     Potion")
                action = input("What do you wish to do? ").lower()
                if action not in options:
                    print("You panicked hard, and the Warden sents death upon you...")
                    print("Game over...")
                    break
                else:
                    if action == "attack":
                        print("You dealt", attack, "damage")
                        w_HP -= attack
                        print("Warden HP:", w_HP)
                        if w_HP <= 0:
                            print("You defeated the Warden!")
                            break
                        print("Warden attacks!")
                        print("Warden dealt", w_att, "damage")
                        HP -= w_att
                        if HP <= 0:
                            print("You died...")
                            break
                        print(name, "HP:", HP)
                    elif action == "potion":
                        if potions > 0:
                            print("You used a potion")
                            potions -= 1
                            HP += 50
                            if HP > 120:
                                HP = 120
                            healed = 50
                            print("You healed:", healed)
                            print(name, "HP:", HP)
                        else:
                            print("No potions")
                    else:
                        print("No potions")
                        continue

    elif direction == "north":
        chance = random.randint(0, 4)  # 1/5
        randoHP = random.randint(-5, 5)
        randoAtt = random.randint(-3, 2)
        if chance == 2:
            print("A monster appears!")
            m_HP = 30 + randoHP
            m_att = 2 + randoAtt
            print("Monster HP:", m_HP)
            print("Monster Attack:", m_att)
            while True:
                print("Attack     Potion")
                print("Defend     Run")
                action = input("What do you wish to do? ").lower()
                if action not in options:
                    print("You panicked hard, and the monster beat you to death.")
                    print("Game over...")
                    break
                else:
                    if action == "attack":
                        print("You dealt", attack, "damage")
                        m_HP -= attack
                        print("Monster HP:", m_HP)
                        if m_HP <= 0:
                            print("You defeated the monster!")
                            randomScore = random.uniform(0, 2)
                            gamescore += math.floor(43 * randomScore)
                            break
                        print("Monster attacks!")
                        print("Monster dealt", m_att, "damage")
                        HP -= m_att
                        if HP <= 0:
                            print("You have died.")
                            print("Game over...")
                            break
                        print(name, "HP:", HP)
                    elif action == "potion":
                        if potions > 0:
                            print("You used a potion")
                            potions -= 1
                            HP += 50
                            if HP > 120:
                                HP = 120
                            healed = 50
                            print(f"You healed: {healed}")
                            print(name, "HP:", HP)
                        else:
                            print("No potions")
                    elif action == "defend":
                        print("Incoming damage reduced by half!")
                        print("Monster attacks!")
                        print("Monster dealt", (m_att * 0.5), "damage")
                        HP -= (m_att * 0.5)
                        if HP <= 0:
                            print("You have died.")
                            print("Game over...")
                            break
                        print(name, "HP:", HP)
                    else:
                        runchance = random.randint(0, 1)  # 1/2
                        if runchance == 1:
                            print("Successfully ran away.")
                            break
                        else:
                            print("Failed!")
                            continue
    elif direction == "east":
        chance = random.randint(0, 4)  # 1/5
        randoAtt = random.randint(-3, 3)
        if chance == 1:
            print("You found a unique item")
            item = attack + randoAtt
            print("Another sword:", item, "attack")
            action = input("Do you want to take it? (yes/no) ").lower()
            if action == "yes":
                print("Equipped!")
                attack = item
                print(name + "'s attack:", attack)
            else:
                print("Left it.")
        elif chance == 2:
            print("Found 2 potions")
            potions += 2
            print("Available potions:", potions)
    elif direction == "south":
        print("You found nothing.")
        chance = random.randint(0, 4)  # 1/5
        if chance == 2:
            print("Found 2 potions")
            potions += 2
            print("Available potions:", potions)
    elif direction == "west":
        chance = random.randint(0, 4)  # 1/5
        randoAtt = random.randint(-3, 2)
        if chance == 2:
            print("A monster appears!")
            m_HP = 30
            m_att = 2 + randoAtt
            print("Monster HP:", m_HP)
            print("Monster Attack:", m_att)
            while True:
                print("Attack     Potion")
                print("Defend     Run")
                action = input("What do you wish to do? ").lower()
                if action not in options:
                    print("You panicked hard, and the monster beat you to death.")
                    print("Game over...")
                    break
                else:
                    if action == "attack":
                        print("You dealt", attack, "damage")
                        m_HP -= attack
                        print("Monster HP:", m_HP)
                        if m_HP <= 0:
                            print("You defeated the monster!")
                            randomScore = random.uniform(0, 2)
                            gamescore += math.floor(43 * randomScore)
                            break
                        print("Monster attacks!")
                        print("Monster dealt", m_att, "damage")
                        HP -= m_att
                        if HP <= 0:
                            print("You have died.")
                            print("Game over...")
                            break
                        print(name, "HP:", HP)
                    elif action == "potion":
                        if potions > 0:
                            print("You used a potion")
                            potions -= 1
                            HP += 50
                            if HP > 120:
                                HP = 120
                            healed = 50
                            print(f"You healed: {healed}")
                            print(name, "HP:", HP)
                        else:
                            print("No potions")
                    elif action == "defend":
                        print("Incoming damage reduced by half!")
                        print("Monster attacks!")
                        print("Monster dealt", (m_att * 0.5), "damage")
                        HP -= (m_att * 0.5)
                        if HP <= 0:
                            print("You have died.")
                            print("Game over...")
                            break
                        print(name, "HP:", HP)
                    else:
                        runchance = random.randint(0, 1)  # 1/2
                        if runchance == 1:
                            print("Successfully ran away.")
                            break
                        else:
                            print("Failed!")
                            continue

print("Your score is:", gamescore)
print("GG")