f = open('day13.txt','r')
lines = f.readlines()
indexo = 1
total = 0
first = []
second = []

def test(first, second): # this is part 1
    global total
    global indexo
    parsing = True

    while parsing:

        if first == [] or second == []:
            if len(first) < len(second):
                total += indexo
                parsing = False
            elif len(first) > len(second):
                parsing = False
            else:
                break

        else:
            X = first.pop(0)
            Y = second.pop(0)

            if type(X) == int and type(Y) == int:
                if X < Y:
                    total += indexo
                    parsing = False
                elif X > Y:
                    parsing = False
            elif type(X) == list and type(Y) == list:
                parsing = test(X, Y)
            elif type(X) == int:
                parsing = test([X],Y)
            else:
                parsing = test(X,[Y])

    return parsing

def dig(spot, level): # this is part 2
    global low
    global mid
    if spot == []:
        low += 1
    elif type(spot[0]) == list:
        dig(spot[0],level+1)
    elif spot[0] < 2 or (spot[0] == 2 and level < 2):
        low += 1
    elif spot[0] < 6 or (spot[0] == 6 and level < 2):
        mid += 1
    
flip = False
part = []
low = 0
mid = 0
for line in lines:
    if line != '\n':
        parts = line.split()
        flip = not flip
        part = eval(parts[0])
        dig(part, 1) #part 2, everything else is part 1
        if flip:
            first = part
        else:
            second = part
            test(first, second)
            indexo += 1
            
print(total) #answer p1
print((low+1)*(low+mid+2)) #answer p2
print(low,' ',mid) #debug