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
num_pancakes = 10
print("I am going to eat " + str(num_pancakes) + " pancakes.")

total_pancakes = 10
pancakes_eaten = 5
print("Only " + str(total_pancakes - pancakes_eaten) + " pancakes left.")
