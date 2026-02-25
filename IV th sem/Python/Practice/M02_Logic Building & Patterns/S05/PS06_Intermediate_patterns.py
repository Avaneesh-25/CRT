'''
li = [1,2,3,4,5]
output:[1,4,9,16,25]
'''
'''
li = [1,2,3,4,5]
for i in range(len(li)):
    li[i] = li[i]**2
print(li)
'''

'''
li = ['a','b','c']
output: ['a1','b2','c3']
'''

'''
pyramid pattern
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
    for j in range(n-i-1):
        print(" ", end="")
    for k in range(i+1):
        print("*", end=" ")
    print()
'''

'''
number pyramid
n = 4
output:
   1
  1 2
 1 2 3
'''
'''
n = int(input())
for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for k in range(i+1):
        print(k+1, end=" ")
    print()
'''

'''
hallow pyramid
n = 4
output:
   *
  * *
 *   *
* * * *
'''
n = int(input())
for i in range(n):
    





























    for j in range(n-i-1):
        print(" ", end="")
    for k in range(i+1):
        if k == 0 or k == i or i == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()