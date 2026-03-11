'''
Arithmettic series
input: 1 2 
output: 1 3 5 7 9 11 13 15 17 19
'''
'''
start = int(input("Enter the first term: "))
diff = int(input("Enter the common difference: "))
n = int(input("Enter the number of terms: "))
for i in range(n):
    term = start + i * diff
    print(term, end=" ")
'''

'''
geometric series
  
'''
n = int(input())
a = 0
b = 1
for i in range(n):
    print(a,end=" ")
    a,b = b, a+b


