from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Initialisation de l'API
app = FastAPI()

# Configuration du CORS (pour autoriser ton futur frontend HTML à appeler cette API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # En production, on mettra l'URL de ton portfolio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# On définit le format de la donnée que le frontend va envoyer
class PasswordRequest(BaseModel):
    mot_de_passe: str

# --- TES 4 FONCTIONS (analyser, calculer, choix, Mesurer) VONT ICI ---

# Création de la route web (l'URL de ton API)
@app.post("/api/tester-mdp")
def tester_mot_de_passe(requete: PasswordRequest):
    # On envoie le mot de passe reçu à ta fonction principale
    resultat = Mesurer_mot_de_passe(requete.mot_de_passe)
    return resultat

def analyser_mot_de_passe(mot_de_passe_recu):
    majuscule = minuscule = nombres = Speciaux = MaxLettreConsecutive = 0
    compteur =1
    CharC = ""
    for i, char in enumerate(mot_de_passe_recu):

        if i > 0:
            if char == mot_de_passe_recu[i - 1]:
                compteur += 1
            else:
                compteur = 1

        if compteur > MaxLettreConsecutive:
            MaxLettreConsecutive = compteur
            CharC = char

        if char.isalpha():
            if char.isupper():
                majuscule += 1
            else:
                minuscule += 1
        elif char.isdigit():
            nombres += 1
        else:
            Speciaux += 1
        

    return {
        "longueur": len(mot_de_passe_recu),
        "nbMajuscule": majuscule,
        "nbMinuscule": minuscule,
        "nbNombres": nombres,
        "nbCaractereSpeciaux": Speciaux,
        "nbMaxLettreConsecutive": [MaxLettreConsecutive, CharC]
    }

def calculer_score(mot_de_passe):
    score = 0

    # 1. Longueur : Facteur de sécurité principal (Max : 16 points)
    score += min(mot_de_passe["longueur"], 16)

    # 2. Diversité (Max : 2 points)
    score += 1 if 1 <= mot_de_passe["nbMajuscule"] <= 2 else (2 if mot_de_passe["nbMajuscule"] >= 3 else 0)
    score += 1 if 1 <= mot_de_passe["nbMinuscule"] <= 2 else (2 if mot_de_passe["nbMinuscule"] >= 3 else 0)
    score += 1 if 1 <= mot_de_passe["nbNombres"] <= 2 else (2 if mot_de_passe["nbNombres"] >= 3 else 0)

    # Les caractères spéciaux augmentent considérablement l'entropie (Max : 3 points)
    score += 2 if 1 <= mot_de_passe["nbCaractereSpeciaux"] <= 2 else (3 if mot_de_passe["nbCaractereSpeciaux"] >= 3 else 0)

    # 3. Pénalité de répétition (Max : 2 points)
    score += 2 if mot_de_passe["nbMaxLettreConsecutive"][0] <= 2 else 0

    return min(100.0, round((score/27)*100, 2))

def choixMessage(score):
    if score < 40:
        return "Faible : Mot de passe facile à craquer."
    elif score < 70:
        return "Moyen : Peut mieux faire, ajoute des symboles."
    elif score < 90:
        return "Fort : Bon mot de passe."
    else:
        return "Robuste : Excellent rempart !"

def Mesurer_mot_de_passe(mot_de_passe_recu):

    mot_de_passe = analyser_mot_de_passe(mot_de_passe_recu)
    score = calculer_score(mot_de_passe)
    Text_Message = choixMessage(score)

    return {"score": score, "message": Text_Message, "details": mot_de_passe}

