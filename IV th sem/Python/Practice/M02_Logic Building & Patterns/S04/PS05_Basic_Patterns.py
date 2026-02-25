'''
square star pattern
n = 4
output:
* * * * 
* * * *
* * * * 
* * * *
'''
'''
n = int(input())
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
'''

'''
right angle triangle 
n = 4
output:
*
* *
* * *
* * * *
'''
'''
n = int(input())
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()
'''

'''
inverted right 
n = 4
output:
* * * *
* * *
* *
*
'''
n = int(input())
for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    print()
