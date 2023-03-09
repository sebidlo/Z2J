'''
print(type(len))
num_letters = len("four")
print(num_letters)
return_value = print("What do I return?")
print(return_value)
'''

def multiply(x, y):
    # Function signature
    # # Function body
    product = x * y
    return product
    print("You can't see me!") # For instance, the print() function will never be executed in the following function !!!

print(multiply(2,2))

num = multiply(2,5)

print(num)