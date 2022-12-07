total = 0
overlap = 0
f = open('day4.txt','r')
for line in f.readlines():
    parts = line.split(',')
    one = parts[0].split('-')
    two = parts[1].split('-')
    s1 = int(one[0])
    e1 = int(one[1])
    s2 = int(two[0])
    e2 = int(two[1])
    if((s1<=s2 and e1>=e2) or (s2<=s1 and e2>=e1)):
        total += 1
    if((s2<=e1 and s1<=e2)or(s1<=e2 and s2<=e1)):
        overlap += 1

print(total)
print(overlap)