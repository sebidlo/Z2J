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
'''
starship = "Enterprise"
print(starship)
print(starship.startswith("en"))
print(starship.endswith("rise"))
