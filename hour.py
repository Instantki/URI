x = int(input())
hour = []
fact = [3600, 60, 1]
for n in fact:
    hour.append(x/n)
    x = x%n
print("%d:%d:%d" %(hour[0],hour[1],hour[2]))
