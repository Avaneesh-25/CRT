for i in range(1, 11):
    if i == 5:
        continue  # Skip the rest of the loop when i is 5
    print(i,end = " ")
else:
    print("Loop completed")
'''
password retry system (max 3 attempts)
if password is correct show login successful
else ask for password 3 times
once attempts exceed show account locked
'''
p1 = "abc12345"
for i in range(3):
    p2 = input()
    if p1 == p2:
        print("Login successful")
        break
    else:
        print("Account locked")

