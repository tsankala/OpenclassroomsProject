from chercher_chaine_saisie import chaine_saisie,demander_saisie
def chaine_texte():
    '''
    Cette fonction enregistre 2 chaîne dans une fichier texte.
    :return: Aucun
    '''
    chaine_1,chaine_2=demander_saisie()
    f_1 = open('texte.txt', 'w')
    f_1.write(chaine_1+'\n')
    f_1.write(chaine_2+'\n')
    f_1.close()
    return None

def lire_chaine_texte ():
    '''
    Cette fonction lit 2 chaînes dans un fichier texte.
    :return: Aucun
    '''
    nouvelle_liste_chaine =[]
    f_2 = open('texte.txt','r')
    liste_chaine= f_2.readlines()
    f_2.close()
    for t in liste_chaine:
        t = t.rstrip('\n')
        nouvelle_liste_chaine.append(t)
    chaine_1 = nouvelle_liste_chaine[0]
    chaine_2=nouvelle_liste_chaine[1]
    chaine_saisie(chaine_1, chaine_2)
    return None

chaine_texte()
lire_chaine_texte()

