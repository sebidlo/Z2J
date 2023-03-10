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

for n in range(1, 4):
    for j in range(4, 7):
        print(f"n = {n} and j = {j}")
Review Exercises 6.4
'''
'''
1. Write a for loop that prints out the integers 2 through 10, each on
a new line, by using the range() function.

for n in range(1,11):
    print(n)


2. Use a while loop that prints out the integers 2 through 10 (Hint:
You’ll need to create a new integer first.)

m = 2
while m <= 10:
    print(m)
    m = m + 1

3. Write a function called doubles() that takes one number as its input
and doubles that number. Then use the doubles() function in a
loop to double the number 2 three times, displaying each result on
a separate line. Here is some sample output:
4
8
16
'''
def doubles(x):
    x = x * 2
    return x
    #print(x)

x = 2

for j in range(0, 3):
    x = doubles(x)
    print(x)

    

