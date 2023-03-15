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
'''
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
