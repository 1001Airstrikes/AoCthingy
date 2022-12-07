segments = []
length = 0
total = 0
switch = 4
f = open('day6.txt','r')
line = f.readline()
for l in line:
    total += 1
    if (length>=switch):
        segments.pop(0)
    segments.append(l)
    length = len(segments)

    sorted = segments.copy()
    sorted.sort()

    if (length>=switch):
        last = 0
        passes = True
        for i in range(switch):
            if (last == sorted[i]):
                passes = False
                break
            else:
                last = sorted[i]
        if passes:
            print(total)
            if (switch==4):
                switch = 14
            else:
                break