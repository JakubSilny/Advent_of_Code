
depth = 0
hor = 0
aim = 0
data = open('Datas.txt')
for i in data:
    command, move = i.split()
    move = int(move)
    if command == 'forward':
        hor = hor + move
        depth = depth + (aim * move)
    elif command == 'down':
        #depth = depth + move
        aim = aim + move
    elif command == 'up':
        #depth = depth - move
        aim = aim - move;

print('Answer: ', hor * depth)
print('forward: ', hor)
print('depth: ', depth)
