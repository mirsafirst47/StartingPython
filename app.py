#         Input lesson

# weight_in_pound = input("Enter your weight: ")
# weight_in_kilo = int(weight_in_pound) * 0.45
# print(weight_in_kilo)

#         If Else Statement

# is_hot = False
# is_cold = False

# if is_hot:
#     print("Drink plenty of water and stay cool.")
# elif is_cold:
#     print("Make sure to grab a jacket.")
# else:
#     print("It's sexy weather time. Wear Baccarat!!!")

# price_of_house = 1000000
# good_credit = True
#
# if good_credit:
#     down_payment = 0.1 * price_of_house
# else:
#     down_payment = 0.2 * price_of_house
# print(f"Down payment is: ${down_payment}")

#       Logical Operators (and, or, not) Example can be used for both operators
# AND: Both should be True
# Or: one has to be True

# has_high_income = True
# has_good_credit = True
#
# if has_high_income and has_good_credit:
#     print("Eligible for loan.")
# else:
#     print("Not a good candidate for loan approval.")

#       Comparison Operators (<, >, >=, <=, ==, !=)

# temperature = 30
#
# if temperature > 30:
#     print("It's a hot day.")
# elif temperature < 10:
#     print("It's a cold day.")
# else:
#     print("It's neither hot or cold today.")

# name = input("Enter name: ")
#
# if len(name) < 3:
#     print("Name must be at least 3 characters.")
# elif len(name) > 12:
#     print("Name can't be more than 12 characters.")
# else:
#     print(f"Welcome {name}!")

# weight = int(input("Enter your weight: "))
# kg_or_lbs = input("(L)bs or (k)g: ")
#
# if kg_or_lbs.upper() == "L":
#     converted_weight = weight * 0.45
#     print(f"You are {converted_weight} kilos.")
# elif kg_or_lbs.upper() == "K":
#     converted_weight = weight / 0.45
#     print(f"You are {converted_weight} pounds.")

#        While loops

# i = 1
# while i <= 5:
#     print("*" * i)
#     i += 1
# print("Done.")

#    Guessing Game
# secret_num = 9
# guess_count = 0
# guess_limit = 3
#
# while guess_count < guess_limit:
#     guess = int(input("Guess: "))
#     guess_count += 1
#     if guess == secret_num:
#         print("You won!")
#         break
# else:
#     print("Sorry, you failed.")

#         Car engine game

# command = ""
# started = False
#
# while True:
#     command = input("> ").lower()
#     if command == "help":
#         print("""
# start - to start the car
# stop - to stop the car
# quit - to quit
#         """)
#     elif command == "start":
#         if started:
#             print("car already on.")
#         else:
#             started = True
#             print("Car started...Ready to go!")
#     elif command == "stop":
#         if not started:
#             print("car is already stopped.")
#         else:
#             started = False
#             print("Car stopped.")
#     elif command == "quit":
#         break
#     else:
#         print("I don't understand that...")


#          for loops

# prices = [10, 35, 20, 75]
# total = 0
#
# for price in prices:
#     total += price
# print(f"Total: {total}")

# for i in range(1, 5):
#     print(i)
# range(5):generates 0,1,2,3,4
# range(1,5):generates 1,2,3,4
# range(1,5,2):generates 1,3. 2 is a step.

#           Nested loops

# for x in range(4):
#     for y in range(3):
#         print(f"({x}, {y})")

# numbers = [2, 2, 2, 2, 7] #shape for printing an L
#
# for number in numbers:
#     output = ""
#     for count in range(number):
#         output += "x"
#     print(output)

#         Lists

# numbers = [1, 6, 56]
# max = numbers[0]
#
# for number in numbers:
#     if number > max:
#         max = number
# print(max)

#       2D lists: list inside of a list

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# accessing an element from the inner list
# print(matrix[1][0])

# iterating over items in a 2D list
# for row in matrix:
#     for item in row:
#         print(item)

#       Removing duplicates

# numbers = [1, 2, 7, 10, 10, 0, 8, 9, 10, 2]
# uniques = []
#
# for number in numbers:
#     if number not in uniques:  # if the number is not in the unique list
#         uniques.append(number)  # add it to the unique list
#         # uniques.sort()
# print(uniques)

#        Tuples (1, 2, 3) they are immutable. Can't add or remove items form tuples.

coordinates = (1, 2, 3)  # tuple
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]

x, y, z = coordinates  # tuple unpacking. does the same as the 3 lines above. you can also unpack lists.

print(y)

