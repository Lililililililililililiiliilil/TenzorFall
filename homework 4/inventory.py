inventory = {}
capacity = 50
current_weight = 0

while True:
    command = list(input().split())
    if command[0] == "+" and command[2].isdigit():
        if current_weight + float(command[2]) <= capacity:
            inventory[command[1]] = float(command[2])
            current_weight += float(command[2])
            print('Inventory: %.1f/%.0f' % (current_weight, capacity))
        else:
            print('Not enough space \033[91m %.1f/%.0f \033[00m !' % (current_weight + float(command[2]), capacity))
    elif command[0] == "-":
        if current_weight - inventory[command[1]] < 0:
            current_weight = 0
        else:
            current_weight -= inventory[command[1]]
            inventory.pop(command[1])
            print('Inventory %.1f/%.0f' % (current_weight, capacity))
    elif command[0] == 'stop':
        break
    elif command[0] == 'list':
        print('item | weight')
        print('-------------')
        for w in sorted(inventory, key=inventory.get, reverse=True):
            print(' %s   |  %.1f' % (w, inventory[w]))
    else:
        print('Incorrect input!')
