print("Welcome to Quiz :) ")

playing = input("Do you want to play? ")
if playing.lower()!= "yes":
    quit()
score = 0
incorrect = 0

print("Okay! Let play")

answer = input("what does stands for pc? ")
if answer.lower() == "personal computer":
    print("correct")
    score += 1
else:
    print("incorrect")
    incorrect += 1

answer = input("what does stands for cpu? ")
if answer.lower() == "central processing unit":
    print("correct")
    score += 1
else:
    print("incorrect")
    incorrect += 1

answer = input("what does stands for RAM? ")
if answer.lower() == "random access memory":
    print("correct")
    score += 1
else:
    print("incorrect")
    incorrect += 1

answer = input("what does stands for ROM? ")
if answer.lower() == "read only memory":
    print("correct")
    score += 1
else:
    print("incorrect")
    incorrect += 1

print("Score: "  + str(score) + " correct answer")
print("wrong: "  + str(incorrect) + " incorrect answer")
print("percentage: "  + str((score / 4) * 100) + " %.")
