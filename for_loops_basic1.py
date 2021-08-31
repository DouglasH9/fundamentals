for i in range(0, 151):
    print(i)

for i in range(5, 1000, 5):
    print(i)

for i in range(1, 101):
    if i%10==0:
        print("Coding Dojo")
    elif i%5==0:
        print("Coding")
    else:
        print(i)

sum = 0
for i in range(0, 500001):    
    if i%2!=0:
        sum += i

print(sum)

for i in range(2018, 0, -4):
    print(i)

lowNum = 4
highNum = 93
mult = 6
for i in range(lowNum, highNum):
    if i%mult==0:
        print(i)

