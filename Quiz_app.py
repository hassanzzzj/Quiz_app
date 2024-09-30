import time
import random

#Questions
questions = {
    "science": [
        {"question": "which is the largest planet?" , "options":["Earth","Saturn","Jupiter","Uranus"], "answer":2 },
        {"question": "Who discovered Gravity?", "options":["Galileo","Newton","Einstein","Copernicus"], "answer":1},
        {"question": "which is the largest planet?" , "options":["Earth","Saturn","Jupiter","Uranus"], "answer":2 },
        {"question": "Who discovered Gravity?", "options":["Galileo","Newton","Einstein","Copernicus"], "answer":1},
        {"question": "What is the process by which plants make their food?", "options":["Respiration","Photosynthesis","Decomposition","Fermentation"], "answer":1},
        {"question": "Which one is the largest mammal?","options":["Blue Whale","Fin Whale","Humpback Whale","Sperm Whale"],"answer":0},
        {"question": "which is the smallest bone in  the human body?", "options":["Femur","Tibia "<"Sternum","Stapes"],"answer":3},
        {"question": "WHo is the father of Genetics?","optons":["Gregor Mendel","Charles Darwin","Albert Einstein","louiss Pasteur"],"answer":0},
        {"question": "What is the scientific study of Earth's crust is called?", "options":["Geology","Geography","Topology","Ophthalmology"],"answer":0},
        {"question": "What is the largest living species of lizard?","opyions":["Komodo Dragon","Saltwater Crocodile","Black Mamba","Agamid"],"answer":0}
    ],
    "History":[
        {"question": "Who wasa the first president of United States?","options":["George Washington","Thomas Jefferson","Abraham Lincoin","Andrew Jackson"], "answer":0},
        {"question": "In which Year World War II started?","options":["1935","1939","1941","1945"],"answer":1},
        {"question": "Who wasa the first president of United States?","options":["George Washington","Thomas Jefferson","Abraham Lincoin","Andrew Jackson"], "answer":0},
        {"question": "In which Year World War II started?","options":["1935","1939","1941","1945"],"answer":1},
        {"question": "Who was the ancient pharaoh who built the great Pyramid?", "options":["Ramses II","Khufu","Tutankhamun","khafre"],"answer":1},
        {"question": "Who was the Roman General who crossed the Rubicon River?","options":["Julius Caeser", "Pompey","Hannibal","Nero"],"answer":0},
        {"question": "The Great Depression began with the stock market crash of which year?","options":["1925","1929","1931","1935"],"answer":1},
        {"question": "Who was the leader of Nazi Germany during World War II?","options":["Adolf Hitler","Benito Mussolini","Joseph Stalin","Hirochito"],"answer":0},
        {"question": "The Treaty of Westphalia ended which conflict?","options":["Thirty years war","Hundred Years War","War of the Roses","American Revolution"],"answer":0},
        {"question": "Which ancient civilization built the Great Library of Alexandria?","options":["Egyptians","Greeks","Romans","Babylonians"],"answer":0}
    ],
    "General Knowledge":[
        {"question": "Which planet in our solar system is known as the Red Planet?","options":["Earth","Mars","Jupiter","Saturn"],"answer":1},
        {"question": "Who painted the famous artwork The Starry Night?","options":["Leonardo da Vinci","Vincet van Gogh","Pablo Picasso","Claude Monet"],"answer":1},
        {"question": "What is the chemical symbol for gold?","options":["Ag","Au","Hg","Pb"],"answer":1},
        {"question": "In Greek mythology, who was the god of the underworld?","options":["Zeus","Poseidon","Hades","Hermes"],"answer":2}
    ],
}
# Track user score
user_score = {}

def display_categories():
    print("select a category:")
    for i, category in enumerate(questions.keys()):
        print(f"{i+1}.{category}")

def display_questions(category):
    questions_list = questions[category]
    random.shuffle(questions_list)
    return questions_list

def take_quiz(category, duration):
    questions_list = display_questions(category)
    score = 0
    start_time = time.time()
    for question in questions_list:
        print(f"\nQuestion: {question['question']}")
        for i, option in enumerate(question['options']):
            print(f"{i+1}.{option}")
        answer = int(input("Enter your answer(1-4): ")) -1
        if answer == question['answer']:
            score += 1
            print("Correct")
        else:
            print(f"Incorrect. The correct answer is {question['options'] [question['answer']]}")
        elapsed_time = time.time() - start_time
        remaining_time = duration - int (elapsed_time)
        print(f"\nTime remaining: {remaining_time} seconds")
        if remaining_time <= 0:
            break
    return score
def view_scores():
    print("\nYour Passt score: ")
    for category,  score in user_score.items():
        print(f"{category}: {score}")

def main():
    while True:
        print("\n*******Quiz Application******")
        print("1. Start New Quiz ")
        print("2. Previous Scores")
        print("3. Exit ")
        choice = input("Enter Your choice: ")
        if  choice == "1":
            display_categories()
            category_choice = int(input("Enter the Category Number: "))
            category = list(questions.keys())[category_choice-1]
            duration = int(input("Enter the quiz dration (in seconds): "))
            score = take_quiz(category, duration)
            user_score[category] = score
            print(f"\nYour score: {score} out of {len(questions[category])}")
        elif choice == "2":
            view_scores()
        elif choice =="3":
            break
        else:
            print("Invalid choice. Please Try again.")

if __name__ == "__main__":
    main()            
