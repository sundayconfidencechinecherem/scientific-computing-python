#Simple quiz app

print("\n Simple Nigeria current affairs quiz")
questions = {
    "\n what is the name of current president of nigeria? ": "tinubu",
    "\n What is the capital city of Nigeria? ": "abuja",
    "\n What is the color of nigeria flag? ": "green and white"
}
score = 0

for i, answer in questions.items():
    user_answer = input(i + " ").lower()
    if user_answer == answer:
        print(f"\n correct!")
        score +=1
    else:
        print(f"\n Wrong! The correct answer is {answer.title()}. ")
print(f"\n You got {score} / {len(questions)} correct!")