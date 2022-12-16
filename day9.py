snake = [[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0]]
places = {"0,0": True}
total = 1

f = open('day9.txt','r')
lines = f.readlines()
for line in lines:
    parts = line.split()
    for step in range(int(parts[1])):
        if parts[0] == 'U':
            snake[0][1] += 1
        elif parts[0] == 'D':
            snake[0][1] -= 1
        elif parts[0] == 'L':
            snake[0][0] -= 1
        else:
            snake[0][0] += 1

        for i in range(9):
            head = snake[i]
            tail = snake[i+1]
            if (head[0] == tail[0]+2 and head[1] == tail[1]+1) or (head[0] == tail[0]+1 and head[1] == tail[1]+2):
                tail[0] += 1
                tail[1] += 1
            elif (head[0] == tail[0]-2 and head[1] == tail[1]+1) or (head[0] == tail[0]-1 and head[1] == tail[1]+2):
                tail[0] -= 1
                tail[1] += 1
            elif (head[0] == tail[0]-2 and head[1] == tail[1]-1) or (head[0] == tail[0]-1 and head[1] == tail[1]-2):
                tail[0] -= 1
                tail[1] -= 1
            elif (head[0] == tail[0]+2 and head[1] == tail[1]-1) or (head[0] == tail[0]+1 and head[1] == tail[1]-2):
                tail[0] += 1
                tail[1] -= 1
            elif head[0] == tail[0]+2 and head[1] == tail[1]+2:
                tail[0] += 1
                tail[1] += 1
            elif head[0] == tail[0]-2 and head[1] == tail[1]+2:
                tail[0] -= 1
                tail[1] += 1
            elif head[0] == tail[0]-2 and head[1] == tail[1]-2:
                tail[0] -= 1
                tail[1] -= 1
            elif head[0] == tail[0]+2 and head[1] == tail[1]-2:
                tail[0] += 1
                tail[1] -= 1
            elif head[0] == tail[0]+2:
                tail[0] += 1
            elif head[0] == tail[0]-2:
                tail[0] -= 1
            elif head[1] == tail[1]+2:
                tail[1] += 1
            elif head[1] == tail[1]-2:
                tail[1] -= 1
            

        key = f"{snake[9][0]},{snake[9][1]}"
        check = places.get(key)
        if not check:
            total += 1
            places[key] = True

print(total)