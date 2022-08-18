print("---------------------------------------------------------")
print("Welcome to \"Who wants to be a millionaire!\" Let's play.")
print("---------------------------------------------------------")
print("Ok. First Question.\n")
print("Q.1) Meaning the act of \"lying with a person,\" what word appears on a T-shirt that warns that it often \"leads to forking\"?")
print("\n", "A. Chopsticking\n", "B. Paring knifing\n", "C. Salad tonging\n", "D. Spooning\n")

life_count = 1
winning_prize = 0

def on_exit(count, prize):
    if count == 1:
        message = "Congratulations, you win $" + str(prize) + "!"
        print(message)
        exit()
    else:
        print("Game Over!")
        exit()

answer = input("Answer: ")
if answer == "D":
    print("That is correct!")
    winning_prize = 500
    print("You have $", str(winning_prize), "!\n")
elif (answer != "D"):
    print("Oh no, that is incorrect.")
    life_count -= 1
    on_exit(life_count, winning_prize)
else:
    print("Please choose A, B, C or D only.")

print("Q.2) Journey's \"Don't Stop Believin\" and Bon Jovi's \"Wanted Dead or Alive\" are just two of many songs often referred to as what?")
print("\n", "A. Mini melodies\n", "B. Power ballads\n", "C. Turbo ditties\n", "D. Extreme waltzes\n")

answer = input("Answer: ")
if answer == "B":
    print("That is correct!")
    winning_prize = 1000
    print("You have $", str(winning_prize), "!\n")
elif (answer != "B"):
    print("Oh no, that is incorrect.")
    life_count -= 1
    on_exit(life_count, winning_prize)
else:
    print("Please choose A, B, C or D only.")

print("Q.3) A play on the title of an infamous 1936 propaganda film, Kevin Sabet's book arguing against marijuana legalization is called what?")
print("\n", "A. Crack isn't whack\n", "B. Reefer Sanity\n", "C. Oxy Morons\n", "D. There's Something About Molly\n")

answer = input("Answer: ")
if answer == "B":
    print("That is correct!")
    winning_prize = 2000
    print("You have $", str(winning_prize), "!\n")
elif (answer != "B"):
    print("Oh no, that is incorrect.")
    life_count -= 1
    on_exit(life_count, winning_prize)
else:
    print("Please choose A, B, C or D only.")

print("Q.4) For the sake of historical accuracy, what's the only building in Central London that's been allowed to have a thatched roof since a major fire struck the city in 1212?")
print("\n", "A. British Museum\n", "B. Tower of London\n", "C. Globe Theater\n", "D. Buckingham Palace\n")

answer = input("Answer: ")
if answer == "C":
    print("That is correct!")
    winning_prize = 3000
    print("You have $", str(winning_prize), "!\n")
elif (answer != "C"):
    print("Oh no, that is incorrect.")
    life_count -= 1
    on_exit(life_count, winning_prize)
else:
    print("Please choose A, B, C or D only.")

print("Q.5) Hoping to avoid mispronounciations, when it was established in 1949 what French company dropped the 'h' from the end of its founder's last name?")
print("\n", "A. Renault\n", "B. Nestle\n", "C. Bic\n", "D. Evian\n")

answer = input("Answer: ")
if answer == "C":
    print("That is correct!")
    winning_prize = 5000
    print("You have $", str(winning_prize), "!\n")
elif (answer != "C"):
    print("Oh no, that is incorrect.")
    life_count -= 1
    on_exit(life_count, winning_prize)
else:
    print("Please choose A, B, C or D only.")

print("Q.6) Two inches taller than his wife Michelle, how tall is Barack Obama?")
print("\n", "A. 5'7\"\n", "B. 5'10\"\n", "C. 6'1\"\n", "D. 6'4\"\n")

answer = input("Answer: ")
if answer == "C":
    print("That is correct!")
    winning_prize = 7000
    print("You have $", str(winning_prize), "!\n")
elif (answer != "C"):
    print("Oh no, that is incorrect.")
    life_count -= 1
    on_exit(life_count, winning_prize)
else:
    print("Please choose A, B, C or D only.")

print("Q.7) Translating to mean \"I have found it,\" what is the only U.S. state to have an official motto in Greek?")
print("\n", "A. California\n", "B. Florida\n", "C. Texas\n", "D. Montana\n")

answer = input("Answer: ")
if answer == "A":
    print("That is correct!")
    winning_prize = 10000
    print("You have $", str(winning_prize), "!\n")
elif (answer != "A"):
    print("Oh no, that is incorrect.")
    life_count -= 1
    on_exit(life_count, winning_prize)
else:
    print("Please choose A, B, C or D only.")

print("Q.8) Thanks to its high capsaicin content, what common spice is commonly used medicinally to improve circulation, and rubbed on the skin to relieve pain?")
print("\n", "A. Cinnamon\n", "B. Coriander\n", "C. Cumin\n", "D. Cayenne\n")

answer = input("Answer: ")
if answer == "D":
    print("That is correct!")
    winning_prize = 20000
    print("You have $", str(winning_prize), "!\n")
elif (answer != "D"):
    print("Oh no, that is incorrect.")
    life_count -= 1
    on_exit(life_count, winning_prize)
else:
    print("Please choose A, B, C or D only.")

print("Q.9) If you drank the proverbial 8 glasses of water a day and lived to be 100, you'd consume 18,250 gallons, closest to the amount in which amount of the following?")
print("\n", "A. 1,000 beer kegs\n", "B. 10 Olympic-sized swimming pools\n", "C. 2 Boston Harbors\n", "D. 1 Lake Tahoe\n")

answer = input("Answer: ")
if answer == "A":
    print("That is correct!")
    winning_prize = 30000
    print("You have $", str(winning_prize), "!\n")
elif (answer != "A"):
    print("Oh no, that is incorrect.")
    life_count -= 1
    on_exit(life_count, winning_prize)
else:
    print("Please choose A, B, C or D only.")

print("Q.10) Founded in Colorado, what candy company specifically chose its name so as \"to suggest a hospitable, western company\"?")
print("\n", "A. Bazooka Bubble Gum\n", "B. Jolly Rancher\n", "C. Tootsie Roll\n", "D. Jelly Belly\n")

answer = input("Answer: ")
if answer == "B":
    print("That is correct!")
    winning_prize = 30000
    print("You have $", str(winning_prize), "!\n")
elif (answer != "B"):
    print("Oh no, that is incorrect.")
    life_count -= 1
    on_exit(life_count, winning_prize)
else:
    print("Please choose A, B, C or D only.")

print("Q.11) Which insect shorted out an early supercomputer and inspired the term \"computer bug\"?")
print("\n", "A. Moth\n", "B. Roach\n", "C. Fly\n", "D. Japanese beetle\n")

answer = input("Answer: ")
if answer == "A":
    print("That is correct!")
    winning_prize = 50000
    print("You have $", str(winning_prize), "!\n")
elif (answer != "A"):
    print("Oh no, that is incorrect.")
    life_count -= 1
    on_exit(life_count, winning_prize)
else:
    print("Please choose A, B, C or D only.")

print("Q.12) During WWII, U.S. soldiers used the first commercial aerosol cans to hold what?")
print("\n", "A. Cleaning fluid\n", "B. Antiseptic\n", "C. Insecticide\n", "D. Shaving cream\n")

answer = input("Answer: ")
if answer == "C":
    print("That is correct!")
    winning_prize = 100000
    print("You have $", str(winning_prize), "!\n")
elif (answer != "C"):
    print("Oh no, that is incorrect.")
    life_count -= 1
    on_exit(life_count, winning_prize)
else:
    print("Please choose A, B, C or D only.")

print("Q.13) Which scientific unit is named after an Italian nobleman?")
print("\n", "A. Pascal\n", "B. Ohm\n", "C. Volt\n", "D. Hertz\n")

answer = input("Answer: ")
if answer == "C":
    print("That is correct!")
    winning_prize = 250000
    print("You have $", str(winning_prize), "!\n")
elif (answer != "C"):
    print("Oh no, that is incorrect.")
    life_count -= 1
    on_exit(life_count, winning_prize)
else:
    print("Please choose A, B, C or D only.")

print("Q.14) Now used to refer to a cat, the word \"tabby\" is derived from the name of a district of what world capital?")
print("\n", "A. Baghdad\n", "B. New Delphi\n", "C. Cairo\n", "D. Moscow\n")

answer = input("Answer: ")
if answer == "A":
    print("That is correct!")
    winning_prize = 500000
    print("You have $", str(winning_prize), "!\n")
elif (answer != "A"):
    print("Oh no, that is incorrect.")
    life_count -= 1
    on_exit(life_count, winning_prize)
else:
    print("Please choose A, B, C or D only.")

print("Q.15) Which of the following landlocked countries is entirely contained within another country?")
print("\n", "A. Lesotho\n", "B. Burkina Faso\n", "C. Mongolia\n", "D. Luxembourg\n")

answer = input("Answer: ")
if answer == "A":
    print("That is correct!")
    winning_prize = 1000000
    print("You have $", str(winning_prize), "!\n")
elif (answer != "A"):
    print("Oh no, that is incorrect.")
    life_count -= 1
    on_exit(life_count, winning_prize)
else:
    print("Please choose A, B, C or D only.")

on_exit(life_count, winning_prize)

"""
Future updates will include using lifelines
50:50
Ask the expert
Ask the audience

"""