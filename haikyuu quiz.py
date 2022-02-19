print("Welcome to Haikyuu quiz!!")
b = input("Enter your name: ")

a = input(f"Do you want to participate in the quiz {b}? \n yes or no? \n")

if a.lower() == "no":
    print("Sad to see you go ;(")
    quit()

print(f"Okay, lets begin the quiz {b}!!")
print("You have to give the correct answer to gain points!")
print("Choose only one option")
score = 0


answer = int(input("Who is the captain of Karasuno's team? \n 1. Hinata shoyo \n 2. Toru Oikawa \n 3. Daichi Sawamura \n Answer: "))
if answer == 3:
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer!")

answer = int(input("Which team is Karasuno's destined rival? \n 1. Date Tech \n 2. Nekoma \n 3. Itachiyama \n Answer: "))
if answer == 3:
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer!")

answer = int(input("Who is the captain of Aoba Johsai's team? \n 1. Kageyama \n 2. Toru Oikawa \n 3. Miya Atsumu \n Answer: "))
if answer == 2:
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer!")

answer = int(input("Who is the twin of Miya Osamu ? \n 1. Hinata shoyo \n 2. Kageyama \n 3. Miya Atsumu \n Answer: "))
if answer == 3:
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer!")

answer = int(input("Who is the captain of Inarizaki's team? \n 1. Shinsuke Kita \n 2. Keiji Akaashi \n 3. Kozume Kenma \n Answer: "))
if answer == 1:
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer!")

print(f"Thankyou {b} for participating in this quiz!")
print(f"You have gained {score} points {b}!!")



