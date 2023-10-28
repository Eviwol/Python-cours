import random
import string
import math

class TesteurMDP:
    def __init__(self, mdp):
        self.mdp = mdp

    def complexite(self):
        jeu_de_caracteres = string.ascii_letters + string.digits + string.punctuation
        ensemble_mdp = set(self.mdp)
        longueur_mdp = len(self.mdp)
        longueur_jeu_de_caracteres = len(jeu_de_caracteres)
        entropie = longueur_mdp * math.log2(longueur_jeu_de_caracteres)
        return entropie

    def evaluer_mdp(self):
        entropie = self.complexite()
        if entropie < 64:
            return "Faible"
        elif entropie < 128:
            return "Moyenne"
        else:
            return "Forte"

class GenerateurMDP:
    def __init__(self, nb_minuscules, nb_majuscules, nb_chiffres, nb_caracteres_speciaux):
        self.nb_minuscules = nb_minuscules
        self.nb_majuscules = nb_majuscules
        self.nb_chiffres = nb_chiffres
        self.nb_caracteres_speciaux = nb_caracteres_speciaux

    def generer_mdp(self):
        minuscules = ''.join(random.choice(string.ascii_lowercase) for _ in range(self.nb_minuscules))
        majuscules = ''.join(random.choice(string.ascii_uppercase) for _ in range(self.nb_majuscules))
        chiffres = ''.join(random.choice(string.digits) for _ in range(self.nb_chiffres))
        caracteres_speciaux = ''.join(random.choice(string.punctuation) for _ in range(self.nb_caracteres_speciaux)
)
        mdp = minuscules + majuscules + chiffres + caracteres_speciaux
        return ''.join(random.sample(mdp, len(mdp)))

    def complexite(self, mdp):
        jeu_de_caracteres = string.ascii_letters + string.digits + string.punctuation
        ensemble_mdp = set(mdp)
        longueur_mdp = len(mdp)
        longueur_jeu_de_caracteres = len(jeu_de_caracteres)
        entropie = longueur_mdp * math.log2(longueur_jeu_de_caracteres)
        return entropie

class GenerateurPassPhrase:
    def __init__(self, nb_mots):
        self.nb_mots = nb_mots
        self.liste_mots = ["aspirateur", "serviette", "banane", "porte", "jardin"]
        self.mots_utilises = []

    def generer_phrase_secrete(self):
        if self.nb_mots <= len(self.liste_mots):
            phrase_secrete = []
            for _ in range(self.nb_mots):
                mot_disponible = [mot for mot in self.liste_mots if mot not in self.mots_utilises]
                if not mot_disponible:
                    return "Plus de mots disponibles."
                mot_choisi = random.choice(mot_disponible)
                self.mots_utilises.append(mot_choisi)
                phrase_secrete.append(mot_choisi)
            return ' '.join(phrase_secrete)
        else:
            return "Nombre de mots demandé supérieur à la liste disponible."

    def complexite(self, phrase_secrete):
        longueur_liste_mots = len(self.liste_mots)
        entropie = self.nb_mots * math.log2(longueur_liste_mots)
        return entropie
    


def main():
    print("1. Évaluation de la complexité d'un mot de passe")
    print("2. Génération d'un mot de passe")
    print("3. Génération d'une phrase secrète")
    choix = input("Choisissez une option (1/2/3) : ")

    if choix == "1":
        mdp = input("Entrez le mot de passe à évaluer : ")
        testeur = TesteurMDP(mdp)
        resultat = testeur.evaluer_mdp()
        print(f"Complexité du mot de passe : {resultat}")

    elif choix == "2":
        nb_minuscules = int(input("Nombre de minuscules : "))
        nb_majuscules = int(input("Nombre de majuscules : "))
        nb_chiffres = int(input("Nombre de chiffres : "))
        nb_caracteres_speciaux = int(input("Nombre de caractères spéciaux : "))
        generateur = GenerateurMDP(nb_minuscules, nb_majuscules, nb_chiffres, nb_caracteres_speciaux)
        mdp_genere = generateur.generer_mdp()
        entropie = generateur.complexite(mdp_genere)
        print(f"Mot de passe généré : {mdp_genere}")
        print(f"Complexité du mot de passe : {entropie}")

    elif choix == "3":
        nb_mots = int(input("Nombre de mots dans la phrase secrète : "))
        generateur = GenerateurPassPhrase(nb_mots)
        phrase_secrete_generee = generateur.generer_phrase_secrete()

        if phrase_secrete_generee != "Nombre de mots demandé supérieur à la liste disponible.":
            entropie = generateur.complexite(phrase_secrete_generee)
            print(f"Phrase secrète générée : {phrase_secrete_generee}")
            print(f"Complexité de la phrase secrète : {entropie}")
        else:
            print(phrase_secrete_generee)

if __name__ == "__main__":
    main()