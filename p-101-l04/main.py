'''
print(type(len))
num_letters = len("four")
print(num_letters)
return_value = print("What do I return?")
print(return_value)


def multiply(x, y):
    # Function signature
    """Return the product of two numbers x and y."""
    # # Function body
    product = x * y
    return product
    print("You can't see me!") # For instance, the print() function will never be executed in the following function !!!

print(multiply(2,2))

num = multiply(2,5)

print(num)

def greet(name):
    print(f"Hello {name}")

greet("Sebastian")

help(multiply)
'''
# Review Exercises 6.3

'''
1. Write a function called cube() with one number parameter and re-
turns the value of that number raised to the third power. Test the
function by displaying the result of calling your cube() function on
a few different numbers.

def cube(x):
    potega_3 = x ** 3
    print(f"liczba {x} podniesiona do potegi 3 wynosi: {potega_3}")

cube(2)
cube(4)
cube(25)



2. Write a function called greet() that takes one string parameter
called name and displays the text "Hello <name>!" , where <name> is
replaced with the value of the name parameter.

def greet(name):
    print(f"Hello {name} !")

greet("Sebastian")


n = 1
while n < 5:
    print(n)
    n = n + 1

for letter in "Python":
    print(letter)


word = "Python"
index = 0
while index < len(word):
    print(word[index])
    index = index + 1

for n in range(3):
    print("Python")

for n in range(10, 20):
    print(n * n)

amount = float(input("Enter an amount: "))
for num_people in range(2, 6):
    print(f"{num_people} people: ${amount / num_people:,.2f} each")
'''
for n in range(1, 4):
    for j in range(4, 7):
        print(f"n = {n} and j = {j}")
