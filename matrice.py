#-----------------------------------------
# contructeur et accesseurs
#-----------------------------------------

def Matrice(nbLignes,nbColonnes,valeurParDefaut=0):
    """
    crée une matrice de nbLignes lignes sur nbColonnes colonnes en mettant 
    valeurParDefaut dans chacune des cases
    paramètres: 
      nbLignes un entier strictement positif qui indique le nombre de lignes
      nbColonnes un entier strictement positif qui indique le nombre de colonnes
      valeurParDefaut la valeur par défaut
    résultat la matrice ayant les bonnes propriétés
    """
    listevaleur=[]
    for i in range(nbLignes):
        listevaleur.append([valeurParDefaut]*nbColonnes)
    matrice={}
    matrice["nbLignes"]=nbLignes
    matrice["nbColonnes"]=nbColonnes
    matrice["valeurs"]=listevaleur
    return matrice

def getNbLignes(matrice):
    """
    retourne le nombre de lignes de la matrice
    paramètre: matrice la matrice considérée
    """
    return matrice["nbLignes"]

def getNbColonnes(matrice):
    """
    retourne le nombre de colonnes de la matrice
    paramètre: matrice la matrice considérée
    """
    return matrice["nbColonnes"]

def getVal(matrice,ligne,colonne):
    """
    retourne la valeur qui se trouve en (ligne,colonne) dans la matrice
    paramètres: matrice la matrice considérée
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
    """
    return matrice["valeurs"][ligne][colonne]


def setVal(matrice,ligne,colonne,valeur):
    """
    met la valeur dans la case se trouve en (ligne,colonne) de la matrice
    paramètres: matrice la matrice considérée
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
                valeur la valeur à stocker dans la matrice
    cettepass fonction ne retourne rien mais modifie la matrice
    """
    matrice["valeurs"][ligne][colonne]=valeur

#------------------------------------------        
# decalages
#------------------------------------------
def decalageLigneAGauche(matrice, numLig, nouvelleValeur=0):
    """
    permet de décaler une ligne vers la gauche en insérant une nouvelle
    valeur pour remplacer la premiere case à droite de cette ligne
    le fonction retourne la valeur qui a été éjectée
    paramèteres: matrice la matrice considérée
                 numLig le numéro de la ligne à décaler
                 nouvelleValeur la valeur à placer
    résultat la valeur qui a été ejectée lors du décalage
    """
    ejecte=getVal(matrice,numLig,0)
    for i in range(1,getNbColonnes(matrice)):
        setVal(matrice,numLig,i-1,getVal(matrice,numLig,i))
    setVal(matrice,numLig,getNbColonnes(matrice)-1,nouvelleValeur)
    return ejecte


def decalageLigneADroite(matrice, numLig, nouvelleValeur=0):
    """
    decale la ligne numLig d'une case vers la droite en insérant une nouvelle
    valeur pour remplacer la premiere case à gauche de cette ligne
    paramèteres: matrice la matrice considérée
                 numLig le numéro de la ligne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    ejecte=getVal(matrice,numLig,getNbColonnes(matrice)-1)
    nouvelleLigne=[nouvelleValeur]
    for i in range (1,getNbColonnes(matrice)):
        nouvelleLigne.append(getVal(matrice,numLig,i-1))
    for i in range (0,getNbColonnes(matrice)):
        setVal(matrice,numLig,i,nouvelleLigne[i])
    return ejecte


def decalageColonneEnHaut(matrice, numCol, nouvelleValeur=0):
    """
    decale la colonne numCol d'une case vers le haut en insérant une nouvelle
    valeur pour remplacer la premiere case en bas de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    ejecte=getVal(matrice,0,numCol)
    for i in range(1,getNbLignes(matrice)):
        setVal(matrice,i-1,numCol,getVal(matrice,i,numCol))
    setVal(matrice,getNbLignes(matrice)-1,numCol,nouvelleValeur)
    return ejecte


def decalageColonneEnBas(matrice, numCol, nouvelleValeur=0):
    """
    decale la colonne numCol d'une case vers le bas en insérant une nouvelle
    valeur pour remplacer la premiere case en haut de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    ejecte=getVal(matrice,getNbLignes(matrice)-1,numCol)
    nouvelleColonne=[nouvelleValeur]
    for i in range (1,getNbLignes(matrice)):
        nouvelleColonne.append(getVal(matrice,i-1,numCol))
    for i in range (0,getNbLignes(matrice)):
        setVal(matrice,i,numCol,nouvelleColonne[i])
    return ejecte