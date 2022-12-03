command = list(input('Input move command: ').split())
position = [0, 0]
command[1] = int(command[1])

if command[0] == 'UP' and command[1] >= 0:
    position[1] += command[1]
elif command[0] == 'DOWN' and command[1] >= 0:
    position[1] -= command[1]
elif command[0] == 'LEFT' and command[1] >= 0:
    position[0] -= command[1]
elif command[0] == 'RIGHT' and command[1] >= 0:
    position[0] += command[1]
else:
    print('INCORRECT COMMAND')

print('Hero position: x=%s y=%s' % (position[0], position[1]))
