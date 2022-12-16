cycle = 1
X = 1
total = 0
mark = 0
graphic = ['','','','','','']
winner = [20,60,100,140,180,220]
gwinner = [40,80,120,160,200,240]
f = open('day10.txt','r')
lines = f.readlines()
for line in lines:
    parts = line.split()

    phase = cycle-(40*mark)-1
    print(cycle,' ',phase,' ',X)
    if phase >= X-1 and phase <= X+1:
        graphic[mark] += '#'
    else:
        graphic[mark] += '.'

    if cycle in winner:
            total += X*cycle
    if cycle in gwinner:
            mark += 1

    if parts[0] == 'addx':
        cycle += 1
        phase += 1
        print(cycle,' ',phase,' ',X)
        if phase >= X-1 and phase <= X+1:
            graphic[mark] += '#'
        else:
            graphic[mark] += '.'

        if cycle in winner:
            total += X*cycle
        if cycle in gwinner:
            mark += 1

        X += int(parts[1])
        
    cycle += 1

print(total)
for line in graphic:
    print(line,'   ',len(line))
