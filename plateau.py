from matrice import *
from carte import *
from random import *

def Plateau(nbJoueurs, nbTresors):
    """
    créer un nouveau plateau contenant nbJoueurs et nbTrésors
    paramètres: nbJoueurs le nombre de joueurs (un nombre entre 1 et 4)
                nbTresors le nombre de trésor à placer (un nombre entre 1 et 49)
    resultat: un couple contenant
              - une matrice de taille 7x7 représentant un plateau de labyrinthe où les cartes
                ont été placée de manière aléatoire
              - la carte amovible qui n'a pas été placée sur le plateau
    """ 
    laby=Matrice(7,7,0)
    setVal(laby,0,0,Carte(True,False,False,True,0,[]))
    setVal(laby,0,2,Carte(True,False,False,False,0,[]))
    setVal(laby,0,4,Carte(True,False,False,False,0,[]))
    setVal(laby,0,6,Carte(True,True,False,False,0,[]))
    setVal(laby,2,0,Carte(False,False,False,True,0,[]))
    setVal(laby,2,2,Carte(False,False,False,True,0,[]))
    setVal(laby,2,4,Carte(True,False,False,False,0,[]))
    setVal(laby,2,6,Carte(False,True,False,False,0,[]))
    setVal(laby,4,0,Carte(False,False,False,True,0,[]))
    setVal(laby,4,2,Carte(False,False,True,False,0,[]))
    setVal(laby,4,4,Carte(False,True,False,False,0,[]))
    setVal(laby,4,6,Carte(False,True,False,False,0,[]))
    setVal(laby,6,0,Carte(False,False,True,True,0,[]))
    setVal(laby,6,2,Carte(False,False,True,False,0,[]))
    setVal(laby,6,4,Carte(False,False,True,False,0,[]))
    setVal(laby,6,6,Carte(False,True,True,False,0,[ ]))
    liste=[Carte(True,False,False,True,0,[]),Carte(True,False,False,True,0,[]),Carte(True,False,False,True,0,[]),Carte(True,False,False,True,0,[]),Carte(True,False,False,True,0,[]),Carte(True,False,False,True,0,[]),Carte(True,False,False,True,0,[]),Carte(True,False,False,True,0,[]),Carte(True,False,False,True,0,[]),Carte(True,False,False,True,0,[]),Carte(True,False,False,True,0,[]),Carte(True,False,False,True,0,[]),Carte(True,False,False,True,0,[]),Carte(True,False,False,True,0,[]),Carte(True,False,False,True,0,[]),Carte(True,False,False,True,0,[]),Carte(False,True,False,False,0,[]),Carte(False,True,False,False,0,[]),Carte(False,True,False,False,0,[]),Carte(False,True,False,False,0,[]),Carte(False,True,False,False,0,[]),Carte(False,True,False,False,0,[]),Carte(False,True,False,True,0,[]),Carte(False,True,False,True,0,[]),Carte(False,True,False,True,0,[]),Carte(False,True,False,True,0,[]),Carte(False,True,False,True,0,[]),Carte(False,True,False,True,0,[]),Carte(False,True,False,True,0,[]),Carte(False,True,False,True,0,[]),Carte(False,True,False,True,0,[]),Carte(False,True,False,True,0,[]),Carte(False,True,False,True,0,[]),Carte(False,True,False,True,0,[])]
    shuffle(liste)
    for y in range(getNbColonnes(laby)):
        if y % 2 == 0:
            for x in range(1,getNbLignes(laby),2):
                choix=choice(range(len(liste)))
                carte=liste[choix]
                del liste[choix]
                setVal(laby,x,y,tourneAleatoire(carte))
        else:
            for x in range(0,getNbLignes(laby)):
                choix=choice(range(len(liste)))
                carte=liste[choix]
                del liste[choix]
                setVal(laby,x,y,tourneAleatoire(carte))
        
   
    carterestant=tourneAleatoire(liste[0])
    
    plateau={"nbJoueurs":nbJoueurs,"nbTresors":nbTresors,"plateau":{"matrice":laby,"carteAmovible":carterestant}}

    listeTresors=[]
    
    for i in range(1,nbTresors+1):
        listeTresors.append(i)
    shuffle(listeTresors)
    listecoord=[]
    
    for y in range(len(plateau["plateau"]["matrice"]["valeurs"])):
        for x in range(len(plateau["plateau"]["matrice"]["valeurs"][y])):
            listecoord.append((x,y))
    coordchoisie=sample(listecoord,nbTresors)
    
    for coord in coordchoisie:
        plateau["plateau"]["matrice"]["valeurs"][coord[0]][coord[1]]["tresor"]=listeTresors[0]
        del listeTresors[0]

    return plateau

   

    



def prendreTresorPlateau(plateau,lig,col,numTresor):
    """
    prend le tresor numTresor qui se trouve sur la carte en lin,col du plateau
    retourne True si l'opération s'est bien passée (le trésor était vraiment sur
    la carte
    paramètres: plateau: le plateau considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
                numTresor: le numéro du trésor à prendre sur la carte
    resultat: un booléen indiquant si le trésor était bien sur la carte considérée
    """
    
    if plateau["plateau"]["matrice"]["valeurs"][lig][col]["tresor"]==numTresor:
        plateau["plateau"]["matrice"]["valeurs"][lig][col]["tresor"]=0
        return True
    else:
        return False


def getCoordonneesTresor(plateau,numTresor):
    """
    retourne les coordonnées sous la forme (lig,col) du trésor passé en paramètre
    paramètres: plateau: le plateau considéré
                numTresor: le numéro du trésor à trouver
    resultat: un couple d'entier donnant les coordonnées du trésor ou None si
              le trésor n'est pas sur le plateau
    """    
    for y in range(len(plateau["plateau"]["matrice"]["valeurs"])):
        for x in range(len(plateau["plateau"]["matrice"]["valeurs"][y])):
            if plateau["plateau"]["matrice"]["valeurs"][x][y]["tresor"]==numTresor:
                return (x,y)
    return None

def getCoordonneesJoueur(plateau,numJoueur):
    """
    retourne les coordonnées sous la forme (lig,col) du joueur passé en paramètre
    paramètres: plateau: le plateau considéré
                numJoueur: le numéro du joueur à trouver
    resultat: un couple d'entier donnant les coordonnées du joueur ou None si
              le joueur n'est pas sur le plateau
    """
    for y in range(len(plateau["plateau"]["matrice"]["valeurs"])):
        for x in range(len(plateau["plateau"]["matrice"]["valeurs"][y])):
            if numJoueur in plateau["plateau"]["matrice"]["valeurs"][x][y]["pions"]:
                return (x,y)
    return None

def prendrePionPlateau(plateau,lin,col,numJoueur):
    """
    prend le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    
    plateau["plateau"]["matrice"]["valeurs"][lin][col]["pions"].remove(numJoueur)   


def poserPionPlateau(plateau,lin,col,numJoueur):
    """
    met le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    
    plateau["plateau"]["matrice"]["valeurs"][lin][col]["pions"].append(numJoueur)

def accessible(plateau,ligD,colD,ligA,colA):
    """
    indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du labyrinthe
    paramètres: plateau: le plateau considéré
                ligD: la ligne de la case de départ
                colD: la colonne de la case de départ
                ligA: la ligne de la case d'arrivée
                colA: la colonne de la case d'arrivée
    résultat: un boolean indiquant s'il existe un chemin entre la case de départ
              et la case d'arrivée
    """
    c = Matrice(7,7)
    
    setVal(c,ligD,colD,1)
    fini = False
    mat = 1
    while not fini:
        c_fin = Matrice(7,7)
        c_fin["valeurs"] = [list(elem) for elem in c["valeurs"]]
        mat += 1
        fini = True
        
        for i in range(getNbLignes(c)):
            for j in range(getNbColonnes(c)):
                carte = plateau["plateau"]["matrice"]["valeurs"][i][j]
                
                if i-1 >= 0 and getVal(c,i,j) != 0:
                    if passageNord(carte,plateau["plateau"]["matrice"]["valeurs"][i-1][j]) and c["valeurs"][i-1][j] == 0:
                        setVal(c_fin ,i-1,j,mat)
                        fini = False
                if i+1 < 7 and getVal(c,i,j) != 0:
                    if passageSud(carte, plateau["plateau"]["matrice"]["valeurs"][i+1][j]) and c["valeurs"][i+1][j] == 0:
                        setVal(c_fin ,i+1,j,mat)
                        fini = False
                if j-1 >= 0 and getVal(c,i,j) != 0:
                    if passageOuest(carte, plateau["plateau"]["matrice"]["valeurs"][i][j-1]) and c["valeurs"][i][j-1] == 0:
                        setVal(c_fin ,i,j-1,mat)
                        fini = False
                if j+1 < 7 and getVal(c,i,j) != 0:
                    if passageEst(carte, plateau["plateau"]["matrice"]["valeurs"][i][j+1]) and c["valeurs"][i][j+1] == 0:
                        setVal(c_fin ,i,j+1,mat)
                        fini = False
                
                if c_fin["valeurs"][int(ligA)][int(colA)] != 0:
                    fini = True
        c["valeurs"] = c_fin["valeurs"]
        
        
    return c



def accessibleDist(plateau,ligD,colD,ligA,colA):
    """
    indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du plateau
    mais la valeur de retour est None s'il n'y a pas de chemin, 
    sinon c'est un chemin possible entre ces deux cases sous la forme d'une liste
    de coordonées (couple de (lig,col))
    paramètres: plateau: le plateau considéré
                ligD: la ligne de la case de départ
                colD: la colonne de la case de départ
                ligA: la ligne de la case d'arrivée
                colA: la colonne de la case d'arrivée
    résultat: une liste de coordonées indiquant un chemin possible entre la case
              de départ et la case d'arrivée
    """
    c=accessible(plateau,ligD,colD,ligA,colA)
    if c["valeurs"][int(ligA)][int(colA)] != 0:
        listeVal=[(ligA,colA)]
        ligAc=ligA
        colAc=colA
        for i in range(c["valeurs"][ligA][colA]-1):
            if c["valeurs"][ligAc-1][colAc]==c["valeurs"][ligAc][colAc]-1:
                listeVal.append((ligAc-1,colAc))
                ligAc=ligAc-1
            elif ligA!=6 and c["valeurs"][ligAc+1][colAc]==c["valeurs"][ligAc][colAc]-1:
                listeVal.append((ligAc+1,colAc))
                ligAc=ligAc+1
            elif c["valeurs"][ligAc][colAc-1]==c["valeurs"][ligAc][colAc]-1:
                listeVal.append((ligAc,colAc-1))
                colAc=colAc-1
            elif c["valeurs"][ligAc][colAc+1]==c["valeurs"][ligAc][colAc]-1:
                listeVal.append((ligAc,colAc+1))
                colAc=colAc+1
        listeVal.reverse()
        
        return listeVal

    else:
        return None