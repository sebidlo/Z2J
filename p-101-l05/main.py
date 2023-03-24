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
'''




import random
def roll():
    return random.randint(1, 6)


rolling_tally = 0
# rolin_number = roll()
# print(f"wylosowano {rolin_number}")

'''
2. Write a script that simulates 10,000 rolls of a fair die and displays
the average number rolled.
'''

for rolling in range(10_000):
    rolin_number = roll()
    rolling_tally = rolling_tally + rolin_number

print(f"po 10_000 rutow ")
print(f"suma wurzuconych oczek = {rolling_tally}")
avenge_value = rolling_tally / 10_000
print(f"średnio wyrzuconi:  {avenge_value:.0f}")
