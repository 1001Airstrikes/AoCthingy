total = 0
badges = 0
i = 0
group = [0,0,0]
scale = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
f = open('day3.txt','r')
for line in f.readlines():
    group[i]=line
    i += 1

    if (i==3):
        one = group[0]
        two = group[1]
        three = group[2]
        for l in one:
            test1 = two.find(l)
            test2 = three.find(l)
            if (test1 != -1 and test2 != -1):
                badges += 1+scale.find(l)
                i = 0
                group = [0,0,0]
                break

    mid = int(len(line)/2)
    one = line[:mid]
    two = line[mid:]
    print(one," ",two)
    for l in one:
        test = two.find(l)
        if (test != -1):
            total += 1+scale.find(l)
            break

print(total)
print(badges)