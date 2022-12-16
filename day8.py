trees = []
total = 0
height = 0
f = open('day8.txt','r')
lines = f.readlines()
for line in lines:
    trees.append([])
    for tree in line:
        if tree != '\n':
            trees[height].append(int(tree))
    height += 1

length = len(trees[0])
midcolum = height/2
midrow = length/2
best = 0

for row in range(height):
    for column in range(length):
        if (column == 0 or row == 0 or column == length-1 or row == height-1):
            total += 1
        else:
            tree = trees[row][column]
            search = ['left','down','up','right']
            value = 1
            passed = False
            
            for dir in search:
                distance = 0
                testrow = row
                testcolumn = column
                searching = True
                while searching:
                    if dir == 'up':
                        testrow -= 1
                    elif dir == 'down':
                        testrow += 1
                    elif dir == 'right':
                        testcolumn += 1
                    else:
                        testcolumn -= 1
                    distance += 1
                    if tree <= trees[testrow][testcolumn]:
                        searching = False
                    elif (testcolumn == 0 or testrow == 0 or testcolumn == length-1 or testrow == height-1):
                        passed = True
                        searching = False
                if (testcolumn == 0 or testrow == 0 or testcolumn == length-1 or testrow == height-1):
                    searching=False
                value *= distance
            if value > best:
                best = value
            if passed:
                    total += 1

print(total)
print(best)