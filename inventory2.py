startingInv = {'gold coin': 2, 'map': 1, 'compass': 1, 'leather jacket': 1}
dragonLoot = {'gold coin': 30, 'dagger': 1, 'dragon eye': 1, 'ruby': 2}

print("Your inventory:")
print(startingInv)

def addToInventory(inventory, addedItems):
    newInventory = {k: inventory.get(k, 0) + addedItems.get(k, 0) for k in set(inventory) | set(addedItems)}
    print(newInventory)


def dragonFight():
    playerInput = input("Type 'fight' or 'live' to continue")
    if playerInput == 'fight':
        playerWins()
    elif playerInput == 'live':
        print('You coward. He laughs at you in a rumbling, ashy sort of chuckle.')
    else:
        print('That is not the right response. Please try again.')
        dragonFight()

def playerWins():
    print('He roars a mighty, firey roar and starts approaching')
    print('Do you swing your sword or use your magic shit? Type your response...')
    winInput = input("Type 'swing sword' or 'magic shit' to continue")
    if winInput == 'swing sword':
        print('You run toward him and swing your big, ass-sword')
        print('It does nothing. He eats you...')
        print('Game Over')
    elif winInput == 'magic shit':
        print('Nice job! The magic shit is super stanky and he dies an oiliphactorial death.')
        addToInventory(startingInv, dragonLoot)
    else:
        print('That is not the right response try again.')
        playerWins()

print('A dragon approaches with a mighty mandible. He looks hungry...')
print('Do you think you stand a chance?')
print('Fight the beast? Or Live to see another day?')
dragonFight()
