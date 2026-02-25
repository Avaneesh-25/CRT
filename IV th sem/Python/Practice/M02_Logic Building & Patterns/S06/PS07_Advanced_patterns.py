'''
1. pascal triangle
n: 5
output:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
'''
'''
def pascal_triangle(n):
    for i in range(n):
        c = 1
        for j in range(i+1):
            print(c, end=' ')
            c = c * (i-j) // (j+1)
        print()
n = 5
pascal_triangle(n)
'''

'''
2. butterfly pattern
n: 4
output:
*      *
**    **
***  ***
********
'''
def butterfly_pattern(n):
    for i in range(1, n+1):
        print('*' * i + ' ' * (2*(n-i)) + '*' * i)
    for i in range(n, 0, -1):
        print('*' * i + ' ' * (2*(n-i)) + '*' * i)
n = 4
butterfly_pattern(n)           