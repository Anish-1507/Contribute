class Playerchoice:
    class1 = {'Item': 'Arrows', 'Weapon': 'Bow', 'Damage': 5, 'Health_Loss': 2}
    class2 = {'Item': 'Magic Arrow', 'Weapon': 'Staff', 'Damage': 15, 'Health_loss': 7}
    class3 = {'Item': 'Shield', 'Weapon': 'Sword', 'Damage': 8, 'Health_Loss': 3}
    print("There are three main types of classes. Archer, Magician, Knight ")
    print("These are the attributes for the different classes : ")
    print(f'Archer : {class1}')
    print(f'Magician: {class2}')
    print(f'Knight : {class3}')
    choice = input("Enter your choice. ")
    choice = choice.upper()


p = Playerchoice()


def fight():
    health = 100
    enemy_health = 100
    damage = 0
    loss = 0
    status = "Alive"
    player_chance = True
    if p.choice == "ARCHER":
        damage = 5
        loss = 2
    elif p.choice == "MAGICIAN":
        damage = 15
        loss = 7
    else:
        damage = 8
        loss = 3
    while health and enemy_health > 0:
        if player_chance:
            print("Your turn to attack.")
            enemy_health -= damage
            print(f"Enemy's health is {enemy_health}")
            player_chance = False
            continue
        else:
            print("Enemy's turn to attack")
            print(f"Your health is {health}")
            health -= loss
            player_chance = True
            continue
    if health > 0 >= enemy_health:
        status = "Alive"
        print("You win!! You may proceed!")
    elif enemy_health > 0 >= health:
        status = "Dead"
        print("      Y O U  D I E D      ")


fight()
