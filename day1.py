
new = 0
first = 0
second = 0
third = 0
f = open('day1.txt','r')
for line in f.readlines():
    if line == '\n':
        print("New: ",new,", 1st: ",first,", 2nd: ",second,", 3rd: ",third)
        if new > first:
            third = second
            second = first
            first = new
        elif new > second:
            third = second
            second = new
        elif new > third:
            third = new
        new = 0
    else:
        new += int(line)

print(first+second+third)