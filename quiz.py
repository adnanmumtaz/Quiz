print("Welcome to Quiz App")
score = 0
answer1 = input("What does CPU stands for: ")
if answer1 == "Central Processing Unit":
    score += 1
    print("Corrent")
else:
    print("Incorrect")

answer2 = input("What does ALU stands for: ")
if answer2 == "Arthematic and Logic Unit":
    score += 1
    print("Corrent")
else:
    print("Incorrect")

answer3 = input("What does CU stands for: ")
if answer3 == "Control Unit":
    score += 1
    print("Corrent")
else:
    print("Incorrect")

answer4 = input("What does RAM stands for: ")
if answer4 == "Random Access Memory":
    score += 1
    print("Corrent")
else:
    print("Incorrect")

print("You scored", str(score), "out of 4")
print("Your percentage is " + str(score / 4 * 100) + "%")
