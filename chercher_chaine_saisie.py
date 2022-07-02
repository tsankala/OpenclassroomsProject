def chaine_saisie(chaine_1,chaine_2):
    """ttttttthomas

    Cette fonction prend 2 chaînes de caractère 'string ' à l'entré et calcul combien de fois la 2 chaîne se trouve
    dans la chaîne 1.
    :param chaine_1:
    :param chaine_2:
    :return: Aucun
    """
    nombre_de_fois=0
    while (len(chaine_2)< 1 ) or (len(chaine_1) < len(chaine_2)):
        chaine_2 = input("entrer la 2 eme chaine( minimum 1 caractère et doit être plus courte que la 1ere chaine rentrer)")
    print(chaine_1)
    print(chaine_2)
    if (chaine_2 in chaine_1):
     i=0
     while i<len(chaine_1):
        if chaine_1[i:i + len(chaine_2)] == chaine_2:
            nombre_de_fois +=1
            i += len(chaine_2)
        else:
            i+=1
    print("La chaîne 2 se retrouve {} fois dans la chaîne 1".format(nombre_de_fois))



def demander_saisie ():
    """
    Cette fonction demander à l'utilisateur de saisir 2 chaîne de caractère et s'assurent
    que les restrictions sont respectés
    :return: Aucun
    """
    chaine_1=input("entrer la 1 ere chaine( minimum 4 caractère)")
    while len(chaine_1)< 4:
        chaine_1 = input("entrer la 1 ere chaine( minimum 4 caractère)")
    chaine_2 = input("entrer la 2 eme chaine( minimum 1 caractère et doit être plus courte que la 1ere chaine rentrer)")
    while (len(chaine_2)< 1 ) or (len(chaine_1) < len(chaine_2)):
        chaine_2 = input("entrer la 2 eme chaine( minimum 1 caractère et doit être plus courte que la 1ere chaine rentrer)")
    return (chaine_1,chaine_2)


chaine_1,chaine_2 = demander_saisie()
chaine_saisie(chaine_1,chaine_2)