# Conditional Logic and Control Flow

'''
1. The if keyword
2. A test condition, followed by a colon
3. An indented block of code that is executed if the test condition is True

if 2 + 2 == 4:
    print("2 and 2 is 4")

grade = 40

if grade >= 70:
    print("You passed the class!")

print("Thank you for attending.")


grade = 40
if grade >= 70:
    print("You passed the class!")
else:
    print("You did not pass the class :(")

print("Thank you for attending.")

grade = 85 # 1

if grade >= 90: # 2
    print("You passed the class with a A.")
elif grade >= 80: # 3
    print("You passed the class with a B.")
elif grade >= 70: # 4
    print("You passed the class with a C.")
else: # 5
    print("You did not pass the class :(")
print("Thanks for attending.") # 6



sport = input("Enter a sport: ")
p1_score = int(input("Enter player 1 score: "))
p2_score = int(input("Enter player 2 score: "))
# 1
if sport.lower() == "basketball":
    if p1_score == p2_score:
        print("The game is a draw.")
    elif p1_score > p2_score:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")
# 2
elif sport.lower() == "golf":
    if p1_score == p2_score:
        print("The game is a draw.")
    elif p1_score < p2_score:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")
# 3
else:
    print("Unknown sport")


# refaktoring z uzyciem operatorów logicznych
sport = input("Enter a sport: ")
p1_score = int(input("Enter player 1 score: "))
p2_score = int(input("Enter player 2 score: "))

if p1_score == p2_score:
    print("The game is a draw.")
elif (sport.lower() == "basketball") or (sport.lower() == "golf"):
    sport = sport.lower()
    p1_wins_basketball = (sport == "basketball") and (p1_score > p2_score)
    p1_wins_golf = (sport == "golf") and (p1_score < p2_score)
    p1_wins = p1_wins_basketball or p1_wins_golf
    if p1_wins:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")
else:
    print("Unknown sport")

'''
# Review Exercises 8.3
'''
Write a script that prompts the user to enter a word using the
input() function, stores that input in a variable, and then displays
whether the length of that string is less than 5 characters, greater
than 5 characters, or equal to 5 characters by using a set of if , elif and else statements.

word = input("wpisz jakies slowo: ")
if len(word) == 5:
    print(" słowo ma 5 znaków")
elif len(word) < 5:
    print("słowo ma mniej niz 5 znakow ")
else:
    print("slowo ma wiecej niz 5 znakow")


8.4. Challenge: Find the Factors of a Number

8.4. Challenge: Find the Factors of a Number


sum_of_evens = 0
for n in range(1, 100):
    if n % 2 == 0:
        sum_of_evens = sum_of_evens + n
print(sum_of_evens)


for n in range(0, 4):
    if n == 2:
        break
    print(n)

print(f"Finished with n = {n}")

for i in range(0, 4):
    if i == 2:
        continue
    print(i)

print(f"Finished with i = {i}")


# phrase = "it marks the spot"

phrase = "X marks the spot"
for character in phrase:
    if character == "X":
        break
    else:
        print("There was no 'X' in the phrase")

for n in range(3):
    password = input("Password: ")
    if password == "I<3Bieber":
        break
    print("Password is incorrect.")
else:
    print("Suspicious activity. The authorities have been alerted.")

Review Exercises 8.6

1. Using break , write a program that repeatedly asks the user for some
input and only quits if the user enters "q" or "Q" .

for n in range(100):
    znak = input("Wpisz jakis znak z klawiatury: ")
    if znak == 'q':
        break


2. Using continue , write a program that loops over the numbers 1 to
50 and prints all numbers that are not multiples of 3 .


for i in range(1, 50):
    if i % 3 == 0:
        continue
    print(i)
'''
'''
ValueError

A ValueError occurs when an operation encounters an invalid value.
For example, trying to convert the string "not a number" to an integer
results in a ValueError :

>>> int("not a number")

Traceback (most recent call last):
File "<pyshell#1>", line 1, in <module>
int("not a number")
ValueError: invalid literal for int() with base 10: 'not a number'

'''

'''
TypeError

A TypeError occurs when an operation is performed on a value of the
wrong type. For example, trying to add a string and an integer will
result in a TypeError :

>>> "1" + 2

Traceback (most recent call last):
File "<pyshell#1>", line 1, in <module>
"1" + 2
TypeError: can only concatenate str (not "int") to str
'''
'''
NameError

A NameError occurs when you try to use a variable name that hasn’t
been defined yet:

>>> print(does_not_exist)

Traceback (most recent call last):
File "<pyshell#3>", line 1, in <module>
print(does_not_exist)
NameError: name 'does_not_exist' is not defined
'''
'''
ZeroDivisionError

A ZeroDivisionError occurs when the divisor in a division operation is 0 :

>>> 1 / 0

Traceback (most recent call last):
File "<pyshell#4>", line 1, in <module>
1 / 0
ZeroDivisionError: division by zero
'''
'''
OverflowError

An OverflowError occurs when the result of an arithmetic operation is
too large. For example, trying to raise the value 2.0 to the power 1_-000_000 results in an OverflowError :

>>> pow(2.0, 1_000_000)

Traceback (most recent call last):
File "<pyshell#6>", line 1, in <module>
pow(2.0, 1_000_000)
OverflowError: (34, 'Result too large')
'''

'''
The try and except Keywords

try:
    number = int(input("Enter an integer: "))
except ValueError:
    print("That was not an integer")




def divide(num1, num2):
    try:
        print(num1 / num2)
    except TypeError:
        print("Both arguments must be numbers")
    except ZeroDivisionError:
        print("num2 must not be 0")

8.7 Review Exercises

1. Write a script that repeatedly asks the user to input an integer,
displaying a message to “try again” by catching the ValueError that
is raised if the user did not enter an integer.
Once the user enters an integer, the program should display
the number back to the user and end without crashing.

ok = False
while ok is False:
    try:
        number = int(input("Enter an integer: "))
        print(f" Your integer = {number} BAY")
        ok = True
    except ValueError:
        print("That was not an integer")

2. Write a program that asks the user to input a string and an integer
n. Then display the character at index n in the string.
Use error handling to make sure the program doesn’t crash
if the user does not enter an integer or the index is out of bounds.
The program should display a different message depending on
what error occurs.

ok = False
words = input("Enter a string: ")

while ok is False:
    try:
        number = int(input("Enter an integer as index the word: "))
        zakres = range(0, len(words)-1)
        print(f"zakres to {zakres}")
        # number in zakres
        print(f"word number {number} is  {words[number]}")
        ok = True

    except ValueError:
        print("That index is not an integer")
    except OverflowError:
        print("That index is out of bounds ")
    except IndexError:
        print("Index error")

        randpom module


# import random
print(random.randint(1, 10))

# import random
def coin_flip():
    """Randomly return 'heads' or 'tails'."""
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"


# First initialize the tallies to 0
heads_tally = 0
tails_tally = 0
for trial in range(50_000):
    if coin_flip() == "heads":
        heads_tally = heads_tally + 1
    else:
        tails_tally = tails_tally + 1

ratio = heads_tally / tails_tally
print(f"The ratio of heads to tails is {ratio}")






# import random
def unfair_coin_flip(probability_of_tails):
    if random.random() < probability_of_tails:
        return "tails"
    else:
        return "heads"


heads_tally = 0
tails_tally = 0
for trial in range(10_000):
    if unfair_coin_flip(.7) == "heads":
        heads_tally = heads_tally + 1
    else:
        tails_tally = tails_tally + 1

ratio = heads_tally / tails_tally
print(f"The ratio of heads to tails is {ratio}")

#8.7 Review Exercises
1. Write a function called roll() that uses the randint() function to
simulate rolling a fair die by returning a random integer between
1 and 6.





# import random
def roll():
    return random.randint(1, 6)


rolling_tally = 0
# rolin_number = roll()
# print(f"wylosowano {rolin_number}")


2. Write a script that simulates 10,000 rolls of a fair die and displays
the average number rolled.


for rolling in range(10_000):
    rolin_number = roll()
    rolling_tally = rolling_tally + rolin_number

print(f"po 10_000 rutow ")
print(f"suma wurzuconych oczek = {rolling_tally}")
avenge_value = rolling_tally / 10_000
print(f"średnio wyrzuconi:  {avenge_value:.0f}")
'''

# 8.8 Challenge: Simulate a Coin Toss Experiment
'''

Suppose you flip a fair coin repeatedly until it lands on both heads and tails at least once each.
In other words, after the first flip, you continue to flip the coin until it lands on something different.
Doing this generates a sequence of heads and tails. For example,
the first time you do this experiment, the sequence might be heads, heads, then tails.
On average, how many flips are needed for the sequence to contain
both heads and tails?
Write a simulation that runs 10,000 trials of the experiment and
prints the average number of flips per trial.

Załóżmy, że wielokrotnie rzucasz uczciwą monetą
dopóki nie wyląduje na 2x orzel  i 1x reszka co najmniej raz.
Innymi słowy, po pierwszym odwróceniu,
kontynuujesz rzucanie monetą, aż wyląduje na czymś innym.
Spowoduje to wygenerowanie sekwencji orłów i reszek. Na przykład
gdy przeprowadzasz ten eksperyment po raz pierwszy, sekwencja może wyglądać orzeł, orzeł, a następnie reszka.
Średnio, ile przewrotów jest potrzebnych, aby sekwencja się zawierała
2x orzeł  i 1x reszka?
Napisz symulację, która przeprowadzi 10 000 prób eksperymentu i
drukuje średnią liczbę rzutów na próbę.






import random
def coin_flip():
    """Randomly return 'heads' or 'tails'."""
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"


# First initialize the tallies to 0
heads_tally = 0  # liczba orlow
tails_tally = 0  # lizcba reszek
sequence_sum = 0  # ile razy wypadla sekwencja: orzel, orzel, reszka
sequence = 0
for trial in range(10_000):
    if coin_flip() == "heads":
        heads_tally = heads_tally + 1
        sequence = sequence + 1
    else:
        tails_tally = tails_tally + 1
        if sequence >= 2:
            sequence_sum = sequence_sum + 1
            sequence = 0

ratio = sequence_sum / 10_000
print(f"sequences (heads, heads, tails) were drawn {sequence_sum}")
print(f"The ratio of seqence (heads, heads, tails) to trials is {ratio:.0%}")


# Chapter 9 Tuples, Lists, and Dictionaries

my_first_tuple = (1, 2, 3)
print(my_first_tuple)
print(type(my_first_tuple))

print(tuple("Python"))

numbers = (1, 2, 3)
print(len(numbers))

name = "David"
print(name)
print(name[1])
print(name[2:4])


vowels = ("a", "e", "i", "o", "u")
for vowel in vowels:
    print(vowel.upper())


coordinates = 4.21, 9.29
print(type(coordinates))

x, y = coordinates
print(x)
print(y)

name, age, occupation = "David", 34, "programmer"
print(name)
print(age)
print(occupation)


vowels = ("a", "e", "i", "o", "u")
print("o" in vowels)
print("x" in vowels)

def adder_subtractor(num1, num2):
    return (num1 + num2, num1 - num2)
...
print(adder_subtractor(3, 2))



#9.2. Review Exercises

1. Create a tuple literal named cardinal_numbers that holds the strings
"first" , "second" and "third" , in that order.

cardinal_numbers = "first", "second", "third"


2. Using index notation and print() , display the string at index 1 in
cardinal_numbers .

print(cardinal_numbers[1])


3. Unpack the values in cardinal_numbers into three new strings
named position1 , position2 and position3 in a single line of code,
then print each value on a separate line.

position1, position2, position3 = cardinal_numbers

print(position1)
print(position2)
print(position3)

4. Create a tuple called my_name that contains the letters of your name
by using tuple() and a string literal.


my_name = tuple("Sebastian")


5. Check whether or not the character keyword. "x" is in my_name using the in

print("x" in my_name)


6. Create a new tuple containing all but the first letter in my_name using
slicing notation.

my_name_2 = my_name[1:]

print(my_name_2)


# create list literal
colors = ["red", "yellow", "green", "blue"]
print(colors)
print(type(colors))

# create list[] function list()
print(list((1, 2, 3)))
text = list("Python")
print(text)
# ['P', 'y', 't', 'h', 'o', 'n']

# create list[] method .split()
groceries = "eggs, milk, cheese"
grocery_list = groceries.split(", ")
print(grocery_list)
# ['eggs', 'milk', 'cheese']


numbers = [1, 2, 3, 4, 5, 6]

for numer in numbers:
    if numer % 2 == 0:
        print(numer)


# Changing Elements in a List
colors = ["red", "yellow", "green", "blue"]
colors[0] = "burgundy"
print(colors)

colors[1:3] = ["orange", "magenta"]
print(colors)
# ['burgundy', 'orange', 'magenta', 'blue']

colors = ["red", "yellow", "green", "blue"]
colors[1:3] = ["orange", "magenta", "aqua"]
print(colors)
# ['red', 'orange', 'magenta', 'aqua', 'blue']

colors[1:4] = ["yellow", "green"]
print(colors)


colors = ["red", "yellow", "green", "blue"]
colors.insert(1, "orange")
print(colors)
colors.insert(10, "violet")
print(colors)
# ['red', 'orange', 'yellow', 'green', 'blue', 'violet']

colors.insert(-1, "indigo")
print(colors)
# ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

colors.insert(-1, "indigo")
print("-1")
print(colors)
# ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'indigo', 'violet']


# remove elements
colors.pop(3)
print(colors)
# ['red', 'orange', 'yellow', 'blue', 'indigo', 'indigo', 'violet']
# colors.pop(-10) IndexError: OUT OF RENGE
colors.pop(-1)
print(colors)
# ['red', 'orange', 'yellow', 'blue', 'indigo', 'indigo']
colors.pop()
print(colors)
# ['red', 'orange', 'yellow', 'blue', 'indigo']

# add elements

colors.append("violet")
print(colors)

colors.extend(["violet", "ultraviolet"])
print(colors)


# Lists of Numbers

nums = [1, 2, 3, 4, 5]
total = 0
for number in nums:
    total = total + number

print(total)

print( sum([1, 2, 3, 4, 5]))
print( max([1, 2, 3, 4, 5]))
print( min([1, 2, 3, 4, 5]))



squares = []
for num in nums:
    squares.append(num**2)
print(squares)

numbers = (1, 2, 3, 4, 5)
squares = [num**2 for num in numbers]
print(squares)
# [1, 4, 9, 16, 25]

# pull ...

str_numbers = ["1.5", "2.3", "5.25"]
float_numbers = [float(value) for value in str_numbers]
print(float_numbers)
'''
'''
1. Create a tuple literal named cardinal_numbers that holds the strings
"first", "second" and "third", in that order.

cardinal_numbers = "first", "second", "third" 
print(cardinal_numbers)
print(type(cardinal_numbers))

2. Using index notation and print(), display the string at index 1 in
cardinal_numbers.

print(cardinal_numbers[1])


3. Unpack the values in cardinal_numbers into three new strings
named position1, position2 and position3 in a single line of code,
then print each value on a separate line.

position1, position2, position3 = cardinal_numbers
print(position1)
print(position2)
print(position3)

4. Create a tuple called my_name that contains the letters of your name
by using tuple() and a string literal.

my_name = tuple("sebastian")
print(my_name)


6. Create a new tuple containing all but the first letter in my_name using
slicing notation.


my_name_2 = my_name[1:]
print(my_name_2)

'''

