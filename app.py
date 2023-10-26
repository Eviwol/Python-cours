import random

class Question:
    def __init__(self, texte_question, options, reponse_correcte):
        self.texte_question = texte_question
        self.options = options
        self.reponse_correcte = reponse_correcte

    def est_correcte(self, reponse_utilisateur):
        return reponse_utilisateur.lower() == self.reponse_correcte.lower()

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def commencer_quiz(self):
        random.shuffle(self.questions)
        for question in self.questions:
            print(question.texte_question)
            for i, option in enumerate(question.options, 1):
                print(f"{chr(96 + i)}) {option}")

            reponse_utilisateur = self.obtenir_reponse_valide()
            if question.est_correcte(reponse_utilisateur):
                print("Correct !\n")
                self.score += 1
            else:
                print(f"Faux. La réponse correcte est {question.reponse_correcte}.\n")

    def obtenir_reponse_valide(self):
        reponse_utilisateur = input("Votre réponse (a, b ou c) : ").lower()
        while reponse_utilisateur not in ['a', 'b', 'c']:
            print("Réponse non valide. Veuillez entrer a, b ou c.")
            reponse_utilisateur = input("Votre réponse (a, b ou c) : ").lower()
        return reponse_utilisateur

    def afficher_score(self):
        print(f"Votre score final est : {self.score}/{len(self.questions)}")

if __name__ == "__main__":
    questions = [
        Question("Quel mot-clé est utilisé pour déclarer une fonction en Python?", ["func", "def", "function"], "b"),
        Question("Comment créez-vous un commentaire en Python?", ["// Commentaire", "# Commentaire", "/* Commentaire */"], "b"),
        Question("Quelle est la sortie de l'expression 2 + 3 * 4 en Python?", ["20", "14", "18"], "b"),
        Question("Quel opérateur est utilisé pour la concaténation de chaînes de caractères en Python?", ["&", "+", "%"], "b"),
        Question("Comment ouvrir un fichier en mode lecture (lecture seule) en Python?", ["open('fichier.txt', 'w')", "open('fichier.txt', 'r')", "open('fichier.txt', 'a')"], "b"),
        Question("Quelle boucle est utilisée pour itérer sur une séquence en Python?", ["for", "while", "repeat"], "a"),
        Question("Quelle méthode est utilisée pour ajouter un élément à la fin d'une liste en Python?", ["append()", "add()", "insert()"], "a"),
        Question("Quelle est la sortie de print('Hello, ' + 'World!') en Python?", ["'Hello, World!'", "'Hello, '", "'World!'"], "a"),
        Question("Comment vérifiez-vous si une clé existe dans un dictionnaire en Python?", ["contains()", "has_key()", "in"], "c"),
        Question("Quelle est la méthode pour supprimer un élément d'une liste en Python?", ["remove()", "delete()", "pop()"], "a"),
    ]

    quiz = Quiz(questions)
    quiz.commencer_quiz()
    quiz.afficher_score()