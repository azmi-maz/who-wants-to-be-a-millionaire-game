print("---------------------------------------------------------")
print("Welcome to \"Who wants to be a millionaire!\" Let's play.")
print("---------------------------------------------------------")
print("Ok. First Question.\n")
print("Q.1) Meaning the act of \"lying with a person,\" what word appears on a T-shirt that warns that it often \"leads to forking\"?")
print("\n", "A. Chopsticking\n", "B. Paring knifing\n", "C. Salad tonging\n", "D. Spooning\n")

life_count = 1

answer1 = input("Answer: ")
if answer1 == "D":
    print("That is correct!")
elif (answer1 == "A" or answer1 == "B" or answer1 == "C"):
    print("Oh no, that is incorrect.")
    life_count -= 1
else:
    print("Please choose A, B, C or D only.")


while life_count == 1:
    life_count = 1
else:
    print("Game Over!")