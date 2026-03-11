'''
print all the factors of a given number
input: 12
output: 1 2 3 4 6 12
'''
'''
num = int(input("Enter a number: "))
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")
print(num)
'''        

'''
count the number of factors of a given number
input: 12
output: 6
'''
'''
num = int(input("Enter a number: "))
count = 0   
for i in range(1, num//2 + 1):
    if num % i == 0:
        count += 1
print(count + 1) 
'''

'''
check if a given number is prime or not
input: 7
output: prime

input: 9
output: not prime
'''
'''
num = int(input("Enter a number: "))
is_prime = True
for i in range(2, num//2 + 1):
    if num % i == 0:
        is_prime = False
        break
if is_prime:
    print("prime")
else:
    print("not prime") 
'''

'''
print all the prime numbers in a given range
input: 1 10
output: 2 5 7
'''
'''
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, num//2 + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")
'''

'''
read a number from the user and display factorial of a number
input: 5
output: 120
'''
'''
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(factorial)
'''

'''
gcd
input: 12 24
output: 12
'''
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
gcd = 1
for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i
print(gcd)