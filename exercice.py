import re
# String
# Exercice 1  : Prendre une chaîne de caractères et retourne la chaîne inversé

def inverser_chaine(chaine=""):    
    return "".join(reversed(chaine))
print("Exercice 1")
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
print("Exercice 2")
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
print("Exercice 4")
print(remplacer_espaces('Ma chaine de caractere'))

# Exercice 5 : Mot le plus long

def mot_le_plus_long(chaine=""):

    mots = chaine.split(' ')    
    plus_long = " "
    for mot in mots:
        if len(mot) > len(plus_long):
            plus_long = mot

    return plus_long
print("Exercice 5")
print(mot_le_plus_long('Ma chaine de caractere'))

# Exercice 6 : regex match

match_regex = r"\d{2}\/\d{2}\/\d{4}"
validate_string = "Les dates importantes sont 12/05/2022 et 23/11/2023"
print("Exercice 6")
print(re.findall(match_regex, validate_string))

# Listes
# Exercice 7 : Liste reverse

def reverse_liste(liste = []):
    return list(reversed(liste))
print("Exercice 7")
print(reverse_liste(['1','2','3','4','5']))

# Tuples
# Exercice 11 : Imprimer le 2eme element du tuples
mon_tuple = (1, "chat", 3.14, True)
print("Exercice 11")
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
print("Exercice 13")
print("Max Min Moyenne :",resultatMoyenneTuple)

# Exercice 14 : Tri des étudiants par note

def trier_etudiants(etudiants_tuple):
    etudiants_tuple.sort(key=lambda x: x[1])
    return etudiants_tuple

etudiants = [('Alice',87),('Bob', 90),('Charlie',75),('Delta',95)]

etudiants_tries = trier_etudiants(etudiants)
print("Exercice 14")
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
print("Exercice 15")
print(resultat)

# Dictionnaires
# Exercice 16 : Acceder a une cle

livre = {'titre':"Les Miserables",'auteur':"Victor Hugo",'annee':'1862'}
print("Exercice 16")
print(livre['auteur'])

# Exercice 17 : Modification et ajout de valeur

livre['annee'] = '1865'
livre['genre'] = 'Roman'
print("Exercice 17")
print(livre)

# Exercice 18 : Affichage des paire clé valeurs
print("Exercice 18")
for key, value in livre.items():
    print(key.capitalize() + ' : ' + value)

# Exercice 19 : Fusion de 2 dictionnaires

dictionnaire1 = {'un':1,'deux':2,'trois':3}

dictionnaire2 = {'quatre':4,'cinq':5,'six':6}

dictionnaire1.update(dictionnaire2)
print("Exercice 19")
print(dictionnaire1)

# Exercice 20 : Nouveau dictionnaire à partir de 2 dictionnaires

def dictionnaire_croise(dico1, dico2):
    dico_croise = {}

    for key,value in dico2.items():
        if value in dico1:
            dico_croise[value] = dico1[value]

    return dico_croise

dico1 = {"a": 1, "b": 2, "c": 3}

dico2 = {"x": "a", "y": "b"}

resultat_dico_croise = dictionnaire_croise(dico1, dico2)
print("Exercice 20")
print(resultat_dico_croise)

# Ensembles (set)

# Exercice 21 : Set sans les multiples de 3

def intersect_without_multiple_three(set1, set2):
    set1.intersection(set2)
    set_intersect = set()
    for value in set1:
        if value % 3 != 0:
            set_intersect.add(value)
    return set_intersect

set1 = {1, 2, 3, 4, 6, 9}

set2 = {2, 3, 5, 6, 7, 9}
print("Exercice 21")
print(intersect_without_multiple_three(set1,set2))

# Exercice 22 : Union moins une valeur

def union_excluding_n(list_of_sets, n):    
    set_intersect = set.union(*list_of_sets)
    set_intersect.remove(n)
    return set_intersect

list_of_sets = [{1, 2, 3}, {3, 4, 5}, {5, 6, 7}]
n = 5
print("Exercice 22")
print(union_excluding_n(list_of_sets, n))

