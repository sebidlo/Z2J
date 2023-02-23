# This is a block comment.
# block comment
# block comment

"""
Multilines block comment
"""
"""
print("Hello World")

text_variable = "Hellooo !!!"
print(text_variable)  # This is an in-line comment.

text_type = type(text_variable)
print("type text_variable is:")
print(text_type)
"""
'''
string1 = 'Hello, world'
string2 = "1234"
print(string1)
print(string2)
'''
"""
The quotes surrounding a string are called delimiters because they tell Python where a string begins and where it ends.
When one type of quotes is used as the delimiter, the other type of quote can be used inside of the string
"""
'''
string3 = "We're #1!"
string4 = 'I said, "Put it over by the llama."'
print(string3)
print(string4)
'''
# Determine the Length of a String
'''
letters = "abc"
num_letters = len(letters)
print(num_letters)


paragraph = "This planet has - or rather had - a problem, which was \
this: most of the people living on it were unhappy for pretty much \
of the time. Many solutions were suggested for this problem, but \
most of these were largely concerned with the movements of small \
green pieces of paper, which is odd because on the whole it wasn't \
the small green pieces of paper that were unhappy."
print(paragraph)

paragraph2 = """This planet has - or rather had - a problem, which was
this: most of the people living on it were unhappy for pretty much
of the time. Many solutions were suggested for this problem, but
most of these were largely concerned with the movements of small
green pieces of paper, which is odd because on the whole it wasn't
the small green pieces of paper that were unhappy."""
print(paragraph2)
print("""An example of a
...          string that spans across multiple lines
...                 that also preserves whitespace.""")

string1 = "abra"
string2 = "cadabra"
magic_string = string1 + string2
print(magic_string)

first_name = "Sebastian"
last_name = "Kycia"
full_name = first_name + " " + last_name
print(full_name)

flavor = "apple pie"
print(flavor[1])
print(flavor[-1])
print(len(flavor))

first_three_letters = flavor[0] + flavor[1] + flavor[2]
print(first_three_letters)
print(flavor[0:3])
print(flavor[-9:-6])
print(flavor[-9:0])
print(flavor[-9:])

word = "goal"
# word[0] = "f"
print(word)
word = "f" + word[1:]  # modify a string by creating a new string
print(word)

name = "Jean-luc Picard"
print(name)
print(name.lower())
print(name.upper())
print(len(name))
name = "Jean-luc Picard         "
print(name.rstrip())
print(name)

starship = "Enterprise"
print(starship)
print(starship.startswith("en"))
print(starship.endswith("rise"))

prompt = "Hey, what's up? "
user_input = input(prompt)
print("You said:", user_input)


1. Write a script that takes input from the user and displays that input
back.

prompt1 = "Type something "
user_input1 = input(prompt1)
print(user_input1)

2. Write a script that takes input from the user and displays the input
in lowercase.

prompt2 = "Write something and I'll make it lowercase"
user_input2 = input(prompt2)
print(user_input2.lower())


3. Write a script that takes input from the user and displays the number
of characters inputted.

prompt3 = "write something and I'll count the letters"
user_input3 = input(prompt3)
number_of_caracters = str(len(user_input3))
print("characters is " + number_of_caracters)



Write a script named first_letter.py that first prompts the user for
input by using the string "Tell me your password:" The script should
then determine the first letter of the user’s input, convert that letter
to upper-case, and display it back.

prompt = "Tell me your password: "
user_input = input(prompt)
first_caracter = user_input[0:1]
print("The first letter you entered was: " + first_caracter.upper())

num = "2"
print(num + num)
num = "12"
print(num * 3)

num = input("Enter a number to be doubled: ")
doubled_num = num * 2
print(doubled_num)
print(int(doubled_num))
print(float(doubled_num))

num = "12.0"
double_num = float(num) * 2
print(double_num)

num = input("Enter a number to be doubled: ")
doubled_num = float(num) * 2
print(doubled_num)
'''
'''
num_pancakes = 10
print("I am going to eat " + str(num_pancakes) + " pancakes.")

total_pancakes = 10
pancakes_eaten = 5
print("Only " + str(total_pancakes - pancakes_eaten) + " pancakes left.")
'''

''' 4.6 Review Exercises
1. Create a string containing an integer, then convert that string into
an actual integer object using int(). Test that your new object is
a number by multiplying it by another number and displaying the result.

number = 20
int_numer = int(number)
print(int_numer * 2)


2. Repeat the previous exercise, but use a floating-point number and
float().

number_2 = 20.0
float_number = float(number_2)
print(float_number * 2)


3. Create a string object and an integer object, then display them sideby-
side with a single print statement by using the str() function.

string_object = "I drink today"
string_object_2 = "coffe"
number_3 = 3
print(string_object, str(number_3), string_object_2)


4. Write a script that gets two numbers from the user using the
input() function twice, multiplies the numbers together, and
displays the result. If the user enters 2 and 4, your program should
print the following text: The product of 2 and 4 is 8.0.

num = input("Enter a number: ")
num_2 = input("Enter a second number:")
print("The product of number and second number is ", str(int(num) * int(num_2)))

n = 30
m = 34
print(f"{n * m}")

1. Create a float object named weight with the value 0.2, and create
a string object named animal with the value "newt". Then use these
objects to print the following string using only string concatenation:
0.2 kg is the weight of the newt.

wight = 0.2
animal = "newt"
print(str(wight) + " kg is the weight of the " + str(animal) + ".")


2. Display the same string by using the .format() method and empty
{} place-holders.

print("{} kg is the weight of the {}.".format(wight, animal))


3. Display the same string using an f-string.


print(f"{wight} kg is the weight of the {animal}.")

phrase = "the surprise is in here somewhere"
print(phrase.find("surprise"))  # find - return index 4
print(phrase.find("eyjafjallajökull"))  # dosen't find substring return -1

my_story = "I'm telling you the truth; nothing but the truth!"
print(my_story)
print(my_story.replace("the truth", "lies"))
print(my_story)

my_story = my_story.replace("the truth", "lies")
print(my_story)

1. In one line of code, display the result of trying to .find() the substring
"a" in the string "AAA". The result should be -1.

text = "AAA"
print(text.find("a"))


2. Replace every occurrence of the character "s" with "x" in the string
"Somebody said something to Samantha.".

my_text = "Somebody said something to Samantha."
print(my_text)
my_text = my_text.replace("s", "x")
print(my_text)


3. Write and test a script that accepts user input using the input()
function and displays the result of trying to .find() a particular
letter in that input.

my_input = input(
    "Type in some text and I'll check to see if there's an 'a' in there. ")
print(my_input)
print(my_input.find("a"))

# translate 4.9 Challenge

my_input = input("Type in some text:")
print(my_input)
my_input = my_input.replace("a", "4")
my_input = my_input.replace("b", "8")
my_input = my_input.replace("e", "3")
my_input = my_input.replace("l", "1")
my_input = my_input.replace("o", "0")
my_input = my_input.replace("s", "5")
my_input = my_input.replace("t", "7")
print(my_input)

print(type(1))
print(int("25"))
print(10000000000000000000000000000000000000000000000000000)
print(1_000_000)

print(type(1.0))
print(float("1.25"))
print(1000000.0)
print(1_000_000.0)
print(1e6)
print(200000000000000000.0)
print(1e-4)
print(2e400)
n = 2e400
print(n)
print(type(n))

1. Write a script that creates the two variables, num1 and num2. Both
num1 and num2 should be assigned the integer literal 25,000,000,
one written with underscored and one without. Print num1 and num2
on two separate lines.

num1 = 25000000
num2 = 25_000_000
print(num1)
print(num2)

2. Write a script that assigns the floating-point literal 175000.0 to the
variable num using exponential notation, and then prints num in the
interactive window.

num = 175000.0
print(num)


3. In IDLE’s interactive window, try and find the smallest exponent N
so that 2e<N>, where <N> is replaced with your number, returns inf.

print(2e300)
print(2e307)
print(2e308)
'''
print(2 + 3)  # Addition +
print(1.0 + 2)  # Result int + float = float

print(5 - 3)  # Subtraction
print(5 - 2.0)  # result float - int = float
print(1 - -3)

print(3 * 3)  # Multiplication
print(2 * 8.0)

print(9 / 3)  # Division
print(5.0 / 2)
print(5 / 2.0)

print(int(8.0 / 2))
print(5.0 // 2)  # Integer Division
print(-3 // 2)

