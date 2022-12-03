position = [0, 0]

while True:
    command = list(input('Input move command: ').split())
    if command[0] == 'UP' and int(command[1]) >= 0:
        position[1] += int(command[1])
    elif command[0] == 'DOWN' and int(command[1]) >= 0:
        position[1] -= int(command[1])
    elif command[0] == 'LEFT' and int(command[1]) >= 0:
        position[0] -= int(command[1])
    elif command[0] == 'RIGHT' and int(command[1]) >= 0:
        position[0] += int(command[1])
    elif command[0] == 'STOP':
        break
    else:
        print('INCORRECT COMMAND')

print('Hero position: x=%s y=%s' % (position[0], position[1]))
