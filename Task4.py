import random

print("\n🎮 Welcome to Rock-Paper-Scissors Game 🎮")

# Score counters
user_score = 0
computer_score = 0
round_number = 1

# Choices list
choices = ["rock", "paper", "scissors"]

while True:
    print(f"\n--- Round {round_number} ---")
    print("Choose one: rock / paper / scissors")
    user = input("Your choice: ").lower()

    if user not in choices:
        print("❌ Invalid input. Please type rock, paper, or scissors.")
        continue

    computer = random.choice(choices)

    print(f"\n You 🧍 chose: {user}")
    print(f"Computer 💻 chose: {computer}")

    # Game logic
    if user == computer:
        print("🔁 It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win this round!✅")
        user_score += 1
    else:
        print("❌ Computer wins this round!")
        computer_score += 1

    # Show current score
    print(f"\n🔢 Score → You: {user_score} | Computer: {computer_score}")

    # Ask if user wants to play again
    play_more = input("\nDo you want to play another round? (yes/no): ").lower()
    if play_more != "yes":
        print("\n🎉 Final Score:")
        print(f"🧍 You: {user_score}")
        print(f"💻 Computer: {computer_score}")

        if user_score > computer_score:
            print("🏆 You won the game!")
        elif user_score < computer_score:
            print("😔 Computer won the game!")
        else:
            print("🤝 It's a draw!")

        print("\nThanks for playing! 👋")
        break

    round_number += 1
