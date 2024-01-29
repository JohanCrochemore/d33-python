# String
# Exercice 1  : Prendre une chaîne de caractères et retourne la chaîne inversé

def inverser_chaine(chaine=""):    
    return "".join(reversed(chaine))

print(inverser_chaine("bonjour"))

# Exercice 2 : Nombre d'occurences

def occurences(chaine=""):
    chaine = chaine.lower()
    occurences = {}
    for letter in chaine:
        if letter in occurences:
            occurences[letter] += 1
        else:
            occurences[letter] = 1
    return occurences

print(occurences('Ma chaine de caractere'))

# Exercice 4 : Remplacer espaces

def remplacer_espaces(chaine="", separator="-"):
    modifier = []
    for letter in chaine:
        if letter == " ":
            modifier.append(separator)    
        else:
            modifier.append(letter)
    
    return ''.join(modifier)

print(remplacer_espaces('Ma chaine de caractere'))

# Exercice 5 : Mot le plus long

def mot_le_plus_long(chaine=""):

    mots = chaine.split(' ')    
    plus_long = " "
    for mot in mots:
        if len(mot) > len(plus_long):
            plus_long = mot

    return plus_long

print(mot_le_plus_long('Ma chaine de caractere'))

# Listes
# Exercice 7 : Liste reverse

def reverse_liste(liste = []):
    return list(reversed(liste))

print(reverse_liste(['1','2','3','4','5']))

# Tuples
# Exercice 11 : Imprimer le 2eme element du tuples
mon_tuple = (1, "chat", 3.14, True)

print(mon_tuple[1])

# Exercice 12 : Modification 

# On ne peut pas modifier un tuple directement. 

# Exercice 13 : Min Max Moyenne

def max_min_moyenne(liste_tuple):

    min_value = min(liste_tuple)    
    max_value = max(liste_tuple)
    moyenne = sum(liste_tuple) / len(liste_tuple)
    return min_value, max_value, moyenne

moyenne_tuple = (10,20,30,40,50)

resultatMoyenneTuple = max_min_moyenne(moyenne_tuple)

print("Max Min Moyenne :",resultatMoyenneTuple)

# Exercice 14 : Tri des étudiants par note

def trier_etudiants(etudiants_tuple):
    etudiants_tuple.sort(key=lambda x: x[1])
    return etudiants_tuple

etudiants = [('Alice',87),('Bob', 90),('Charlie',75),('Delta',95)]

etudiants_tries = trier_etudiants(etudiants)

print("Etudiants tries :",etudiants_tries)

# Exercice 15 : Traiter donner actif/inactif puis ordre décroissant

def traiter_donnees(donnees_tuple):

    liste_active = []
    for donnees in donnees_tuple:
        if donnees[2] == "actif":
            tuple_buffer = (donnees[0],donnees[1])
            liste_active.append(tuple_buffer)

    liste_active.sort(key=lambda x: x[1], reverse=True)

    return liste_active

data = [("id1", 10, "actif"), ("id2", 15, "inactif"), ("id3", 20, "actif")]

resultat = traiter_donnees(data)

print(resultat)