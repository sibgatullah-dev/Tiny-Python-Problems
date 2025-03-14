num = int(input("Enter your number: "))
a,b = 0,1
print(f'{a} {b}', end=" ")

for i in range(num -2):
    c = a + b
    print(c, end=' ')
    a,b = b,c