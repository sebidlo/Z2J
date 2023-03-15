number = int(input("enter a int number: "))

for i in range(1, number):
    if number % i == 0:
        print(f"{i} is a factor of {number}")
