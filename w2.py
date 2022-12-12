# Calculate sum of digits(1256) - 1+2+5+6

total=0
num=input()
for i in range(0,len(num)):
    total += int(num[i])
print(total)