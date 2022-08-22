#Script de génération des fichiers tests
#Import des modules nécessaires au script
from calendar import c
import os
import re
import random
def verifypip():
    print("Vérification de la présence de PIP")
    os.system("py -m ensurepip --default-pip")
    print ("Installation du module docx nécessaire")
    os.system("py -m pip install python-docx")
#verifypip()
#Choix du produit
def userproduct():
    global userproductinput
    userproductinput = input("Renseignez le numéro du produit a valider parmi cette liste : \n01) - Serveur \n02) - Nextbus \n03) - TFT \n04) - Marcus \n05) - PGD \n06) - Client \n07) - Interne \n08) - SAE \n09) - Annuler \n")
    while not (userproductinput):
        userproductinput = input("Renseignez le numéro du produit a valider parmi cette liste : \n01) - Serveur \n02) - Nextbus \n03) - TFT \n04) - Marcus \n05) - PGD \n06) - Client \n07) - Interne \n08) - SAE \n09) - Annuler \n")
    if (userproductinput == "09"):
        print(":/")
        exit(0)
    if (userproductinput == "01" or userproductinput == "02" or userproductinput == "03" or userproductinput == "04" or userproductinput == "05" or userproductinput == "06" or userproductinput == "07" or userproductinput == "08"):
        print("Réponse prise en compte")
    else :
        print ("Réponse incorrecte, veuillez saisir un chiffre (Exemple : 01 pour valider le produit Serveur)")
        userproduct()
userproduct()
#Choix du type de validation
def userproductbis():
    global userproductinputbis
    global userproductchoose
    global validtotalpercentile
    userproductinputbis = input("De quel type de validation s'agit-il ? \n01) - Validation Soft Produit \n02) - Validation affaire standard\n")
    while not userproductinputbis :
        userproductinputbis= input("De quel type de validation s'agit-il ?\n01) - Validation Soft Produit \n02) - Validation affaire standard\n")
    if (userproductinputbis == "01" or userproductinputbis == "02") :
        print("Réponse prise en compte")
    else :
        print ("Réponse incorrecte, veuillez saisir un chiffre (Exemple : 01 pour valider le produit Serveur)")
        userproductbis()
    if (userproductinputbis == "01"):
        validtotalpercentile = "50%"
    else :
        validtotalpercentile = "10%"
    if (userproductinput == "01") :
        userproductchoose = "01_SERVEUR"
        print ("Sélection des cahiers de tests pour le produit n°{} avec un taux de validation de {}".format(userproductchoose, validtotalpercentile))
    elif (userproductinput == "02") :
        userproductchoose = "02_NEXTBUS"
        print ("Sélection des cahiers de tests pour le produit n°{} avec un taux de validation de {}".format(userproductchoose, validtotalpercentile))
    elif (userproductinput == "03") :
        userproductchoose = "03_TFT"
        print ("Sélection des cahiers de tests pour le produit n°{} avec un taux de validation de {}".format(userproductchoose, validtotalpercentile))
    elif (userproductinput == "04") :
        userproductchoose = "04_MARCUS"
        print ("Sélection des cahiers de tests pour le produit n°{} avec un taux de validation de {}".format(userproductchoose, validtotalpercentile))
    elif (userproductinput == "05") :
        userproductchoose = "05_PGD"
        print ("Sélection des cahiers de tests pour le produit n°{} avec un taux de validation de {}".format(userproductchoose, validtotalpercentile))
    elif (userproductinput == "06") :
        userproductchoose = "06_CLIENT"
        print ("Sélection des cahiers de tests pour le produit n°{} avec un taux de validation de {}".format(userproductchoose, validtotalpercentile))
    elif (userproductinput == "07") :
        userproductchoose = "07_INTERNE"
        print ("Sélection des cahiers de tests pour le produit n°{} avec un taux de validation de {}".format(userproductchoose, validtotalpercentile))
    elif (userproductinput == "08") :
        userproductchoose = "08_SAE"
        print ("Sélection des cahiers de tests pour le produit n°{} avec un taux de validation de {}".format(userproductchoose, validtotalpercentile))
userproductbis()
#Récupération des taux de validation
def testselection():
    from docx import Document
    #for i in os.listdir("T:\\04_SERVICES\\PAC Transport\\{}".format(userproductchoose)):
    #   print ("{}".format(i))
    alldocsfromchoose = os.listdir("T:\\04_SERVICES\\PAC Transport\\{}".format(userproductchoose))
    if validtotalpercentile == "50%" :
        howto = 50
    else :
        howto = 10
    x = 0
    y = 0
    z = 0
    mylistdocs = []
    mylistvalue = []
    docDict = {}
    for b in alldocsfromchoose :
        thedoc = b
        print("T:\\04_SERVICES\\PAC Transport\\{}\\{}".format(userproductchoose,thedoc))
        all_para = Document("T:\\04_SERVICES\\PAC Transport\\{}\\{}".format(userproductchoose,thedoc)).paragraphs
        if re.search(".*[A-Z]\\w*.[A-Z]\\w*.[A-Z]\\w*...\\d*.", str(all_para[0].text)) :
            unvalide = thedoc
            print ("Fichier valide")
            countablevar = all_para[0].text[-3:]
            countablechangeit = int(countablevar[0:-1:])
            print ("Ce cahier de test a un taux de validation de : {}%".format(countablechangeit)) 
            x = x + countablechangeit
            y = y + 1 
            mylistdocs.append(unvalide)
            #mylistvalue.append(countablechangeit)
            docDict[unvalide] = countablechangeit
    
        else :
            print ("Fichier non valide, ne sera donc pas pris en compte")
            z = z + 1
    print("{} cahiers de tests sont valide et seront pris en compte pour la séléction aléatoire. Le taux de validation total est de {}%".format(y, x))
    if y == 0 :
        print ("Fin du script, aucun document n'est validé par la regex")
        exit (0)
    if z >= 1 :
        print ("Il y a au total {} qui n'ont pas été pris en compte".format(z))
    print ("Sélection aléatoire parmi cette liste :\n{}".format(mylistdocs))
    def choixaléatoire():
            global asimpleint
            result = []
            global finalarray
            asimpleint = 0
            finalarray = []
            random_docs = random.sample(mylistdocs, k=random.randint(1,y))
            for elem in random_docs:
                result.append(docDict[elem])
            #result = random.sample(mylistvalue, k=random.randint(1,y))

            wut = -1
            # for i in result :
            #     wut = wut + 1
            #     asimpleint = asimpleint + result[wut]           
    choixaléatoire()
    while asimpleint != howto :
        choixaléatoire()
    #print (result)
    print (asimpleint)
testselection()
#Ouvrir les fiches de recettes sélectionnées, avec un CD de 10 ~ 15 secondes entre chaque ouverture pour éviter la surcharge de l'ordintateur
