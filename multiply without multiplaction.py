#This is a function to multiply 2 numbers without using multiplication .
def holder(a, b, counter):
    if counter == 0:
        return 0

    return a + holder(a, b, counter - 1)
def multiply(a, b):
    if a == 0 or b == 0:
        return 0

    return holder(a, b, a)

# the recursive function will do the work of a multiplication
print (multiply(9, 6))
print (multiply(2, 0))
print (multiply(4, 6))

#this problem can also be solved like this
def method(a, b):
    if a==0 or b==0:
        return 0
    return method(a, b-1)+a
print(method(2,4))