terrain = []
f = open('day12.txt','r')
lines = f.readlines()
y = 0
start = [0,0]
end = [0,0]
for line in lines:
    terrain.append([])
    x = 0
    for char in line:
        if char == 'S':
            start = [y,x]
            terrain[y].append('a')
        elif char == 'E':
            end = [y,x]
            terrain[y].append('z')
        elif char != '\n':
            terrain[y].append(char)
        x += 1
    y += 1

length = x
height = y
total = 0
que = [end]
master = []
dirs = ['up','down','left','right']
abcd = 'abcdefghijklmnopqrstuvwxyz'
searching = True

while searching:
    mark = len(que)
    for i in range(mark):

        if not searching:
                break

        spot = que.pop(0)
        master.append(spot)
        here = terrain[spot[0]][spot[1]]

        for dir in dirs:
            if dir == 'up':
                new = [spot[0]-1,spot[1]]
            elif dir == 'down':
                new = [spot[0]+1,spot[1]]
            elif dir == 'left':
                new = [spot[0],spot[1]-1]
            else:
                new = [spot[0],spot[1]+1]

            if not (new[0] < 0 or new[0] >= height or new[1] < 0 or new[1] >= length):
                there = terrain[new[0]][new[1]]
                if new not in master and new not in que:
                    if abcd.find(there) >= abcd.find(here)-1:
                        if there == 'a':
                            searching = False
                            break
                        que.append(new)
    total += 1
    if total > 500:
        print('ERROR: too big...')
        searching = False

print(total)


#for row in terrain:
#    line = ''
#    for char in row:
#        line += char
#    print(line)