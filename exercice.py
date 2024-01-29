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