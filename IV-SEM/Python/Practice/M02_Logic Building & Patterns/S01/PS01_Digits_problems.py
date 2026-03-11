'''
sample input : 1234
sample output : 4

sample input : 12236
sample output : 5
'''
num = int(input("Enter a number: "))
count = 0
while num > 0:
    num = num // 10
    count += 1
print(count)

'''
input : 1234
output : 4321
'''
num = int(input("Enter a number: "))
rev = 0
while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10
print(rev)



