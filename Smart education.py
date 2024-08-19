import random
class StateCapitalQuiz:
    def __init__(self):
        self.states_and_capitals = {
            'Andhra Pradesh': 'Amaravati',
            'Arunachal Pradesh': 'Itanagar',
            'Assam': 'Dispur',
            'Bihar': 'Patna',
            'Chhattisgarh': 'Raipur',
            'Goa': 'Panaji',
            'Gujarat': 'Gandhinagar',
            'Haryana': 'Chandigarh',
            'Himachal Pradesh': 'Shimla',
            'Jharkhand': 'Ranchi',
            'Karnataka': 'Bengaluru',
            'Kerala': 'Thiruvananthapuram',
            'Madhya Pradesh': 'Bhopal',
            'Maharashtra': 'Mumbai',
            'Manipur': 'Imphal',
            'Meghalaya': 'Shillong',
            'Mizoram': 'Aizawl',
            'Nagaland': 'Kohima',
            'Odisha': 'Bhubaneswar',
            'Punjab': 'Chandigarh',
            'Rajasthan': 'Jaipur',
            'Sikkim': 'Gangtok',
            'Tamil Nadu': 'Chennai',
            'Telangana': 'Hyderabad',
            'Tripura': 'Agartala',
            'Uttar Pradesh': 'Lucknow',
            'Uttarakhand': 'Dehradun',
            'West Bengal': 'Kolkata'
        }
        self.score = 0
        self.num_questions = 5  # Default number of questions
    def ask_question(self, state):
        correct_capital = self.states_and_capitals[state]
        answer = input(f"What is the capital of {state}? ").strip()
        if answer.lower() == correct_capital.lower():
            print("Correct!")
            self.score += 1
        else:
            print(f"Wrong! The correct answer is {correct_capital}.")
    def start_quiz(self):
        states = list(self.states_and_capitals.keys())
        random.shuffle(states)
        print("Welcome to the State and Capital Quiz!")
        num_questions = min(self.num_questions, len(states))
        for i in range(num_questions):
            state = states[i]
            self.ask_question(state)
        print(f"Quiz over! Your final score is {self.score}/{num_questions}.")
        self.score = 0  
def main():
    quiz = StateCapitalQuiz()
    while True:
        print("\nQuiz Menu:")
        print("1. Start Quiz")
        print("2. Exit")
        choice = input("Choose an option (1 or 2): ").strip()
        if choice == '1':
            quiz.start_quiz()
            break  
        elif choice == '2':
            print("Thank you for playing!")
            break  
        else:
            print("Invalid choice, please enter 1 or 2.")
if __name__ == "__main__":
    main()