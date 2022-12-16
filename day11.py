monkies = [[66, 59, 64, 51],[67, 61],[86, 93, 80, 70, 71, 81, 56],[94],[71, 92, 64],[58, 81, 92, 75, 56],[82, 98, 77, 94, 86, 81],[54, 95, 70, 93, 88, 93, 63, 50]]
total = [0,0,0,0,0,0,0,0]
for i in range(10000):
    for monkey in range(8):
        for j in range(len(monkies[monkey])):
            item = monkies[monkey].pop(0)
            item = item % 9699690
            if monkey == 0:
                total[0] += 1
                item *= 3
                test = item % 2
                if test == 0:
                    monkies[1].append(item)
                else:
                    monkies[4].append(item)
            elif monkey == 1:
                total[1] += 1
                item *= 19
                test = item % 7
                if test == 0:
                    monkies[3].append(item)
                else:
                    monkies[5].append(item)
            elif monkey == 2:
                total[2] += 1
                item += 2
                test = item % 11
                if test == 0:
                    monkies[4].append(item)
                else:
                    monkies[0].append(item)
            elif monkey == 3:
                total[3] += 1
                item *= item
                test = item % 19
                if test == 0:
                    monkies[7].append(item)
                else:
                    monkies[6].append(item)
            elif monkey == 4:
                total[4] += 1
                item += 8
                test = item % 3
                if test == 0:
                    monkies[5].append(item)
                else:
                    monkies[1].append(item)
            elif monkey == 5:
                total[5] += 1
                item += 6
                test = item % 5
                if test == 0:
                    monkies[3].append(item)
                else:
                    monkies[6].append(item)
            elif monkey == 6:
                total[6] += 1
                item += 7
                test = item % 17
                if test == 0:
                    monkies[7].append(item)
                else:
                    monkies[2].append(item)
            else:
                total[7] += 1
                item += 4
                test = item % 13
                if test == 0:
                    monkies[2].append(item)
                else:
                    monkies[0].append(item)

total.sort(reverse=True)
print(total[0]*total[1])
