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
'''

