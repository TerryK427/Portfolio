import json
import random

class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

class Deck:
    def __init__(self, filename="data.json"):
        self.filename = filename
        self.flashcards = []
        self.load()
    
    def load(self): # Load flashcards from json file
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                for item in data:
                    flashcard = Flashcard(item['question'], item['answer'])
                    self.flashcards.append(flashcard)
        except FileNotFoundError:
            print(f"File {self.filename} not found. Starting with an empty deck.")
    
    def save(self): # Append flashcards to json file
        with open(self.filename, 'w') as file:
            data = [{'question': fc.question, 'answer': fc.answer} for fc in self.flashcards]
            json.dump(data, file, indent=4)

    def add_flashcard(self, question, answer): # Add a new flashcard
        flashcard = Flashcard(question, answer)
        self.flashcards.append(flashcard)
        self.save()

    def get_random_flashcard(self): # Get a random flashcard
        return random.choice(self.flashcards) if self.flashcards else None