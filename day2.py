total=0

f = open('day2.txt','r')
for line in f.readlines():
    line = line.split(' ')
    if line[0] == 'A':
        if line[1] == 'X\n':
            total += 3+0
        elif line[1] == 'Y\n':
            total += 1+3
        else:
            total += 2+6
    elif line[0] == 'B':
        if line[1] == 'X\n':
            total += 1+0
        elif line[1] == 'Y\n':
            total += 2+3
        else:
            total += 3+6
    elif line[0] == 'C':
        if line[1] == 'X\n':
            total += 2+0
        elif line[1] == 'Y\n':
            total += 3+3
        else:
            total += 1+6
    print(total)

print(total)