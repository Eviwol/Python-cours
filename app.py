import random

questions = [
    {
        "question": "Quelle est la race de chat la plus populaire au monde ?",
        "choices": ["Persan", "Siamois", "Maine Coon", "Chat domestique"],
        "correct_choice": 3
    },
    {
        "question": "Combien de doigts (orteils) a généralement un chat domestique normal sur chaque patte avant ?",
        "choices": ["Quatre", "Cinq", "Six", "Deux"],
        "correct_choice": 1
    },
    {
        "question": "Quelle est la principale source d'alimentation d'un chat sauvage ?",
        "choices": ["Légumes", "Fruits", "Viande", "Herbe"],
        "correct_choice": 2
    },
    {
        "question": "Comment les chats communiquent-ils principalement entre eux ?",
        "choices": ["En aboyant", "En grognant", "En miaulant", "En chantant"],
        "correct_choice": 2
    },
    {
        "question": "Quelle race de chat est connue pour sa fourrure sans poils ?",
        "choices": ["Sphynx", "Persan", "Maine Coon", "Siamois"],
        "correct_choice": 0
    },
    {
        "question": "Quel est l'âge moyen d'un chat en bonne santé ?",
        "choices": ["5 ans", "10 ans", "15 ans", "20 ans"],
        "correct_choice": 2
    },
    {
        "question": "Comment les chats marquent-ils leur territoire ?",
        "choices": ["En urinant partout", "En griffant les meubles", "En laissant des empreintes de patte", "En frottant leur tête contre les objets"],
        "correct_choice": 3
    },
    {
        "question": "Quel est le nom du composé chimique qui fait que l'herbe à chat affecte les chats de manière euphorique ?",
        "choices": ["Catnipine", "Felinine", "Niphrine", "Catatanol"],
        "correct_choice": 1
    },
    {
        "question": "Combien de moustaches (vibrisses) en moyenne un chat a-t-il sur son museau ?",
        "choices": ["12", "18", "24", "30"],
        "correct_choice": 2
    },
    {
        "question": "Quel est le plus grand félin au monde ?",
        "choices": ["Lion", "Tigre", "Léopard", "Panthère"],
        "correct_choice": 1
    }
]

score = 0

random.shuffle(questions)

for question in questions:
    print(f"Question: {question['question']}")
    random_choices = random.sample(question['choices'], len(question['choices']))
    index = 0
    for choice in random_choices:
        index += 1
        print(f"{index}.{choice}")

    user_choice = int(input("Votre réponse (1, 2, 3 ou 4) : "))
    
    correct_choice_index = random_choices.index(question['choices'][question['correct_choice']])
    
    if user_choice - 1 == correct_choice_index:
        print("Bonne réponse!\n")
        score += 1
    else:
        print(f"Mauvaise réponse. La réponse correcte est : {question['choices'][question['correct_choice']]}\n")

print(f"Votre score final est de {score}/{len(questions)}.")

