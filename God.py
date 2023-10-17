
questions = [
    "Is God willing to prevent evil? (yes/no): ",
    "Is God able to prevent evil? (yes/no): ",
    "Do humans have free will? (yes/no): ",
]

responses = [
    "Then He is not omnipotent.",
    "Then He is malevolent.",
    "Why does evil exist?",
    "Why call Him God?",
]

theistic_responses = [
    "Theodicy: Evil exists because it's part of God's plan for a greater good.",
    "Soul-Building: Evil exists to test and strengthen our souls.",
    "Unknown Divine Purpose: Evil exists, but we cannot fully understand God's purpose.",
    "Free Will Defense: Evil exists because of human free will.",
]

counterarguments = [
    "Critics argue that attributing evil to God's plan raises questions about God's benevolence. They question whether a perfectly good God would intentionally create or allow suffering.",
    "Some argue that the 'soul-building' explanation does not justify extreme suffering. Critics contend that this explanation implies that God intentionally inflicts suffering on individuals for their spiritual growth.",
    "Critics contend that the 'unknown divine purpose' response is a form of theodicy with limited explanation. They argue that labeling suffering as 'beyond human understanding' may not provide a satisfactory answer.",
    "Skeptics question whether human free will can explain natural disasters and non-human suffering. They argue that events like earthquakes and diseases seem unrelated to human choices and free will.",
]

user_responses = []

for question in questions:
    user_response = input(question).lower()
    if user_response == "yes":
        user_responses.append(True)
    elif user_response == "no":
        user_responses.append(False)
    else:
        print("Please answer with 'yes' or 'no'.")

god_response = None
free_will_response = None

if user_responses[0] and user_responses[1]:
    god_response = responses[2]  # God is willing and able
elif user_responses[0] and not user_responses[1]:
    god_response = responses[1]  # God is willing but not able
elif not user_responses[0] and user_responses[1]:
    god_response = responses[0]  # God is able but not willing
else:
    god_response = responses[3]  # God is neither willing nor able

if user_responses[2]:
    free_will_response = "Humans have free will."
else:
    free_will_response = "Humans do not have free will."
print("\nChoose one of the following theistic responses to the problem of evil:")
for i, response in enumerate(theistic_responses, start=1):
    print(f"{i}. {response}")

user_choice = input("Enter the number corresponding to your choice (1-4): ")
user_choice = int(user_choice)

if 1 <= user_choice <= 4:
    chosen_response = theistic_responses[user_choice - 1]
    print(f"\nYou chose: {chosen_response}")

    print("-" * 50)
    print("\nCounterarguments:")
    print(counterarguments[user_choice - 1])
else:
    print("Invalid choice. Please enter a number between 1 and 4.")

print("\nSummary:")
print(god_response)
print(free_will_response)

print("\n" + "-" * 60)
