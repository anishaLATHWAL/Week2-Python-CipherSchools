# Ask user name and count each character....

name= input('Enter your name: ')
temp= ""
for i in range(0,len(name)):
    if name[i] not in temp:
