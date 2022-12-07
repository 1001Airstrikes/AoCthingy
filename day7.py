grandtotal = 0
f = open('day7.txt','r')
mark = 10216456
storage = 999999999

def traverse():
    total = 0
    global grandtotal
    global storage
    while True:
        line = f.readline()
        parts = line.split()
        if parts[0] == '$':
            if parts[1] == 'cd':
                if parts[2] == '..':
                    if total <= 100000:
                        grandtotal += total
                    if total >= mark and total < storage:
                        storage = total
                    return total
                else:
                    total += traverse()
        elif parts[0] != 'dir':
            total += int(parts[0])
            
traverse()
print(grandtotal)
print(storage)