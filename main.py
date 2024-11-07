"""
"Code permettant de vérifier si mot est un palindrome
"""
#### Fonction secondaire



import string
from unidecode import unidecode

def ispalindrome(p):
    """
    "regarde si un mots est un palindrome et rencoit True si oui
    """
    palindrome = ""
    for i in range(len(p)-1,-1,-1):
        palindrome += p[i]
    translator = str.maketrans(string.punctuation , ' '*len(string.punctuation)) 
    p=p.translate(translator)
    p=unidecode(p.replace(' ','')).lower()
    palindrome=palindrome.translate(translator)
    palindrome=unidecode(palindrome.replace(' ','')).lower()
    if p == palindrome:
        return True
    return False

#### Fonction principale


def main():
    """
    "fonction principale qui teste les autres fonctions secondaire
    """
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
