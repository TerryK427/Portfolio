from Flashcard import Deck

def main():
    deck = Deck()

    while True:
        print("1. Add Flashcard | 2. Take Quiz | 3. View All Flashcards | 4. Exit")
        user_input = input("--------------------------------\nOption (Write Number): ")
        if (user_input.isdigit() and int(user_input) == 1) or user_input.lower() == "add flashcard":
            question = input("Enter question: ")
            answer = input("Enter answer: ")
            deck.add_flashcard(question, answer)
            print("Flashcard added!\n")
        elif choice == '2':
            flashcard = deck.get_random_flashcard()
            if flashcard:
                user_answer = input(f"Question: {flashcard.question}\nYour Answer: ")
                if user_answer.strip().lower() == flashcard.answer.strip().lower():
                    print("Correct!\n")
                else:
                    print(f"Wrong! The correct answer is: {flashcard.answer}\n")
            else:
                print("No flashcards available. Please add some first.\n")
        elif choice == '3':
            if deck.flashcards:
                for idx, fc in enumerate(deck.flashcards, 1):
                    print(f"{idx}. Q: {fc.question} | A: {fc.answer}")
                print()
            else:
                print("No flashcards available.\n")
        elif choice == '4':
            exit()
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()