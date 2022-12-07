dock = [['B','L','D','T','W','C','F','M'],['N','B','L'],['J','C','H','T','L','V'],['S','P','J','W'],['Z','S','C','F','T','L','R'],['W','D','G','B','H','N','Z'],['F','M','S','P','V','G','C','N'],['W','Q','R','J','F','V','C','Z'],['R','P','M','L','H']]
f = open('day5.txt','r')
for line in f.readlines():
    parts = line.split(' ')
    X = int(parts[1])
    A = int(parts[3])-1
    B = int(parts[5])-1
    spot = len(dock[A])-X
    for i in range(X):
        crate = dock[A].pop(spot)
        dock[B].append(crate)

for stack in dock:
    print(stack.pop())

