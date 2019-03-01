from listeJoueurs import *
from plateau import *
from random import *

def Labyrinthe(nomsJoueurs=["joueur1","joueurs2"],nbTresors=24, nbTresorsMax=0):
    """
    permet de créer un Labyrinthe avec nbJoueurs joueurs, nbTresors trésors
    chacun des joueurs aura au plus nbTresorMax à trouver
    si ce dernier paramètre est à 0, on distribuera le maximum de trésors possible 
    à chaque joueur en restant équitable
    un joueur courant est choisi et la phase est initialisée
    paramètres: nomsJoueurs est la liste des noms des joueurs participant à la partie (entre 1 et 4)
                nbTresors le nombre de trésors différents il en faut au moins 12 et au plus 49
                nbTresorMax le nombre de trésors maximum distribué à chaque joueur
    résultat: le Labyrinthe crée
    """
    Labyrinthe={}
    Labyrinthe["Joueurs"]=ListeJoueurs(nomsJoueurs)
    initAleatoireJoueurCourant(Labyrinthe["Joueurs"])
    distribuerTresors(Labyrinthe["Joueurs"],nbTresors, nbTresorsMax)
    Labyrinthe["Phase"]=1
    Labyrinthe["CoupPrecedent"]=None
    Labyrinthe["Plateau"]=Plateau(getNbJoueurs(Labyrinthe["Joueurs"]),nbTresors)
    for i in range(1,len(Labyrinthe["Joueurs"])):
        if i == 1:
            poserPionPlateau(Labyrinthe["Plateau"],0,0,i)
        if i == 2:
            poserPionPlateau(Labyrinthe["Plateau"],0,6,i)
        if i == 3:
            poserPionPlateau(Labyrinthe["Plateau"],6,0,i)
        if i == 4:
            poserPionPlateau(Labyrinthe["Plateau"],6,6,i)
    return Labyrinthe
laby=Labyrinthe()
print(laby)
def getPlateau(Labyrinthe):
    """
    retourne la matrice représentant le plateau de jeu
    paramètre: Labyrinthe le Labyrinthe considéré
    résultat: la matrice représentant le plateau de ce Labyrinthe
    """
    return Labyrinthe["Plateau"]
#print(getPlateau(laby))
def getNbParticipants(Labyrinthe):
    """
    retourne le nombre de joueurs engagés dans la partie
    paramètre: Labyrinthe le Labyrinthe considéré
    résultat: le nombre de joueurs de la partie
    """
    return getNbJoueurs(Labyrinthe["Joueurs"])
#print(getNbParticipants(laby))
def getNomJoueurCourant(Labyrinthe):
    """
    retourne le nom du joueur courant
    paramètre: Labyrinthe le Labyrinthe considéré
    résultat: le nom du joueurs courant
    """
    return nomJoueurCourant(Labyrinthe["Joueurs"])
#print(getNomJoueurCourant(laby))
def getNumJoueurCourant(Labyrinthe):
    """
    retourne le numero du joueur courant
    paramètre: Labyrinthe le Labyrinthe considéré
    résultat: le numero du joueurs courant
    """
    return numJoueurCourant(Labyrinthe["Joueurs"])
#print(getNumJoueurCourant(laby))

def getPhase(Labyrinthe):
    """
    retourne la phase du jeu courante
    paramètre: Labyrinthe le Labyrinthe considéré
    résultat: le numéro de la phase de jeu courante
    """   
    return Labyrinthe["Phase"]
#print(getPhase(laby))

def changerPhase(Labyrinthe):
    """
    change de phase de jeu en passant la suivante
    paramètre: Labyrinthe le Labyrinthe considéré
    la fonction ne retourne rien mais modifie le Labyrinthe
    """    
    if getPhase(Labyrinthe)==2 :
        changerJoueurCourant(Labyrinthe['Joueurs'])
        Labyrinthe["Phase"]=1
        
    else:
        
        Labyrinthe["Phase"]=2
        

def getNbTresors(Labyrinthe):
    """
    retourne le nombre de trésors qu'il reste sur le Labyrinthe
    paramètre: Labyrinthe le Labyrinthe considéré
    résultat: le nombre de trésors sur le plateau
    """ 
    return Labyrinthe["Plateau"]["nbTresors"]
#print(getNbTresors(laby))

def getListeJoueurs(Labyrinthe):
    """
    retourne la liste joueur structures qui gèrent les joueurs et leurs trésors
    paramètre: Labyrinthe le Labyrinthe considéré
    résultat: les joueurs sous la forme de la structure implémentée dans listeJoueurs.py    
    """
    return Labyrinthe["Joueurs"]


def enleverTresor(Labyrinthe,lin,col,numTresor):
    """
    enleve le trésor numTresor du plateau du Labyrinthe. 
    Si l'opération s'est bien passée le nombre total de trésors dans le Labyrinthe
    est diminué de 1
    paramètres: Labyrinthe: le Labyrinthe considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
                numTresor: le numéro du trésor à prendre sur la carte
    la fonction ne retourne rien mais modifie le Labyrinthe
    """
    if Labyrinthe["Plateau"]["plateau"]["matrice"]["valeurs"][lin][col]["tresor"]==numTresor:
        plateau["plateau"]["matrice"]["valeurs"][lin][col]["tresor"]=0
        Labyrinthe["Plateau"]["nbTresors"]-=1

def prendreJoueurCourant(Labyrinthe,lin,col):
    """
    enlève le joueur courant de la carte qui se trouve sur la case lin,col du plateau
    si le joueur ne s'y trouve pas la fonction ne fait rien
    paramètres: Labyrinthe: le Labyrinthe considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
    la fonction ne retourne rien mais modifie le Labyrinthe    
    """
    if getNumJoueurCourant(Labyrinthe) in Labyrinthe["Plateau"]["plateau"]["matrice"]["valeurs"][lin][col]["pions"]:
        prendrePionPlateau(Labyrinthe["Plateau"],lin,col,getNumJoueurCourant(Labyrinthe))

def poserJoueurCourant(Labyrinthe,lin,col):
    """
    pose le joueur courant sur la case lin,col du plateau
    paramètres: Labyrinthe: le Labyrinthe considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
    la fonction ne retourne rien mais modifie le Labyrinthe     
    """
    poserPionPlateau(Labyrinthe["Plateau"],lin,col,getNumJoueurCourant(Labyrinthe))
poserJoueurCourant(laby,0,0)
def getCarteAJouer(Labyrinthe):
    """
    donne la carte à jouer
    paramètre: Labyrinthe: le Labyrinthe considéré
    résultat: la carte à jouer    
    """    
    return Labyrinthe['Plateau']['plateau']['carteAmovible']

def coupInterdit(Labyrinthe,direction,rangee):
    """ 
    retourne True si le coup proposé correspond au coup interdit
    elle retourne False sinon
    paramètres: Labyrinthe: le Labyrinthe considéré
                direction: un caractère qui indique la direction choisie ('N','S','E','O')
                rangee: le numéro de la ligne ou de la colonne choisie
    résultat: un booléen indiquant si le coup est interdit ou non
    """
    if Labyrinthe['CoupPrecedent']==None:
        return False
    if Labyrinthe['CoupPrecedent'][0]=='N':
        if direction=='S' and Labyrinthe['CoupPrecedent'][1]==rangee:
            return True
    if Labyrinthe['CoupPrecedent'][0]=='S':
        if direction=='N' and Labyrinthe['CoupPrecedent'][1]==rangee:
            return True
    if Labyrinthe['CoupPrecedent'][0]=='E':
        if direction=='O' and Labyrinthe['CoupPrecedent'][1]==rangee:
            return True
    if Labyrinthe['CoupPrecedent'][0]=='O':
        if direction=='E' and Labyrinthe['CoupPrecedent'][1]==rangee:
            return True

def getCoordonneesJoueurCourant(Labyrinthe):
    """
    donne les coordonnées du joueur courant sur le plateau
    paramètre: labyritnthe: le Labyrinthe considéré 
    resultat: les coordonnées du joueur courant ou None si celui-ci 
              n'est pas sur le plateau
    """
    return getCoordonneesJoueur(Labyrinthe["Plateau"],getNumJoueurCourant(Labyrinthe))

def jouerCarte(Labyrinthe,direction,rangee):
    """
    fonction qui joue la carte amovible dans la direction et sur la rangée passées 
    en paramètres. Cette fonction
       - met à jour le plateau du Labyrinthe
       - met à jour la carte à jouer
       - met à jour la nouvelle direction interdite
    paramètres: Labyrinthe: le Labyrinthe considéré
                direction: un caractère qui indique la direction choisie ('N','S','E','O')
                rangee: le numéro de la ligne ou de la colonne choisie
    Cette fonction ne retourne pas de résultat mais mais à jour le Labyrinthe
    """
    x=getCoordonneesJoueurCourant(Labyrinthe)[0]
    y=getCoordonneesJoueurCourant(Labyrinthe)[1]
    if direction=='N' and not coupInterdit(Labyrinthe,direction,rangee):
        if x==6 and y==rangee:
            prendreJoueurCourant(Labyrinthe,x,y)
            Labyrinthe["Plateau"]["plateau"]["carteAmovible"]=decalageColonneEnBas(Labyrinthe["Plateau"]["plateau"]["matrice"],rangee,Labyrinthe["Plateau"]["plateau"]["carteAmovible"])
            poserJoueurCourant(Labyrinthe,0,y)
        else:
            Labyrinthe["Plateau"]["plateau"]["carteAmovible"]=decalageColonneEnBas(Labyrinthe["Plateau"]["plateau"]["matrice"],rangee,Labyrinthe["Plateau"]["plateau"]["carteAmovible"])
    if direction=='S' and not coupInterdit(Labyrinthe,direction,rangee):
        if x==0 and y==rangee:
            prendreJoueurCourant(Labyrinthe,x,y)
            Labyrinthe["Plateau"]["plateau"]["carteAmovible"]=decalageColonneEnHaut(Labyrinthe["Plateau"]["plateau"]["matrice"],rangee,Labyrinthe["Plateau"]["plateau"]["carteAmovible"])
            poserJoueurCourant(Labyrinthe,6,y)
        else:
            Labyrinthe["Plateau"]["plateau"]["carteAmovible"]=decalageColonneEnHaut(Labyrinthe["Plateau"]["plateau"]["matrice"],rangee,Labyrinthe["Plateau"]["plateau"]["carteAmovible"])
    if direction=='E' and not coupInterdit(Labyrinthe,direction,rangee):
        if y==0 and x==rangee:
            prendreJoueurCourant(Labyrinthe,x,y)
            Labyrinthe["Plateau"]["plateau"]["carteAmovible"]=decalageLigneAGauche(Labyrinthe["Plateau"]["plateau"]["matrice"],rangee,Labyrinthe["Plateau"]["plateau"]["carteAmovible"])
            poserJoueurCourant(Labyrinthe,x,6)
        else:
            Labyrinthe["Plateau"]["plateau"]["carteAmovible"]=decalageLigneAGauche(Labyrinthe["Plateau"]["plateau"]["matrice"],rangee,Labyrinthe["Plateau"]["plateau"]["carteAmovible"]) 
    if direction=='O' and not coupInterdit(Labyrinthe,direction,rangee):
        if y==6 and x==rangee:
            prendreJoueurCourant(Labyrinthe,x,y)
            Labyrinthe["Plateau"]["plateau"]["carteAmovible"]=decalageLigneADroite(Labyrinthe["Plateau"]["plateau"]["matrice"],rangee,Labyrinthe["Plateau"]["plateau"]["carteAmovible"])
            poserJoueurCourant(Labyrinthe,x,0)
        else:
            Labyrinthe["Plateau"]["plateau"]["carteAmovible"]=decalageLigneADroite(Labyrinthe["Plateau"]["plateau"]["matrice"],rangee,Labyrinthe["Plateau"]["plateau"]["carteAmovible"])


def tournerCarte(Labyrinthe,sens='H'):
    """
    tourne la carte à jouer dans le sens indiqué en paramètre (H horaire A antihoraire)
    paramètres: labyritnthe: le Labyrinthe considéré
                sens: un caractère indiquant le sens dans lequel tourner la carte
     Cette fonction ne retourne pas de résultat mais mais à jour le Labyrinthe    
    """
    if sens=='H':
        tournerHoraire(Labyrinthe["Plateau"]["plateau"]["carteAmovible"])
    else:
        tournerAntiHoraire(Labyrinthe["Plateau"]["plateau"]["carteAmovible"])


def getTresorCourant(Labyrinthe):
    """
    retourne le numéro du trésor que doit cherche le joueur courant
    paramètre: labyritnthe: le Labyrinthe considéré 
    resultat: le numéro du trésor recherché par le joueur courant
    """
    return tresorCourant(Labyrinthe['Joueurs'])


def getCoordonneesTresorCourant(Labyrinthe):
    """
    donne les coordonnées du trésor que le joueur courant doit trouver
    paramètre: labyritnthe: le Labyrinthe considéré 
    resultat: les coordonnées du trésor à chercher ou None si celui-ci 
              n'est pas sur le plateau
    """
    return getCoordonneesTresor(Labyrinthe["Plateau"],getTresorCourant(Labyrinthe))


def executerActionPhase1(Labyrinthe,action,rangee):
    """
    exécute une action de jeu de la phase 1
    paramètres: Labyrinthe: le Labyrinthe considéré
                action: un caractère indiquant l'action à effecter
                        si action vaut 'T' => faire tourner la carte à jouer
                        si action est une des lettres N E S O et rangee est un des chiffre 1,3,5 
                        => insèrer la carte à jouer à la direction action sur la rangée rangee
                           et faire le nécessaire pour passer en phase 2
    résultat: un entier qui vaut
              0 si l'action demandée était valide et demandait de tourner la carte
              1 si l'action demandée était valide et demandait d'insérer la carte
              2 si l'action est interdite car l'opposée de l'action précédente
              3 si action et rangee sont des entiers positifs
              4 dans tous les autres cas
    """
    if action=='T':
        tournerCarte(Labyrinthe)
        return 0
    if action in ["N","E","S","O"] and rangee in [1,3,5]:
        if not coupInterdit(Labyrinthe,action,rangee):
            jouerCarte(Labyrinthe,action,rangee)
            changerPhase(Labyrinthe)
            Labyrinthe["CoupPrecedent"]=(action,rangee)
            return 1
        else :
            return 2
    if type(action)==int and action>0 and type(rangee)==int and rangee>0:
        return 3
    return 4



def accessibleDistJoueurCourant(Labyrinthe, ligA,colA):
    """
    verifie si le joueur courant peut accéder la case ligA,colA
    si c'est le cas la fonction retourne une liste représentant un chemin possible
    sinon ce n'est pas le cas, la fonction retourne None
    paramètres: Labyrinthe le Labyrinthe considéré
                ligA la ligne de la case d'arrivée
                colA la colonne de la case d'arrivée
    résultat: une liste de couples d'entier représentant un chemin que le joueur
              courant atteigne la case d'arrivée s'il existe None si pas de chemin
    """
    coords = getCoordonneesJoueurCourant(Labyrinthe)
    return accessibleDist(Labyrinthe["Plateau"],coords[0],coords[1],ligA,colA)


def finirTour(Labyrinthe):
    """
    vérifie si le joueur courant vient de trouver un trésor (si oui fait le nécessaire)
    vérifie si la partie est terminée, si ce n'est pas le cas passe au joueur suivant
    paramètre: Labyrinthe le Labyrinthe considéré
    résultat: un entier qui vaut
              0 si le joueur courant n'a pas trouvé de trésor
              1 si le joueur courant a trouvé un trésor mais la partie n'est pas terminée
              2 si le joueur courant a trouvé son dernier trésor (la partie est donc terminée)
    """
    coordsTresor = getCoordonneesTresorCourant(Labyrinthe)
    coordsJoueur = getCoordonneesJoueurCourant(Labyrinthe)
    #print(laby)
    if coordsJoueur==coordsTresor:
        tresorTrouve(Labyrinthe['Joueurs'][getNumJoueurCourant(Labyrinthe)])
        enleverTresor(Labyrinthe,coordsTresor[0],coordsTresor[1],prochainTresorJoueur(Labyrinthe['Joueurs'],numJoueurCourant(Labyrinthe['Joueurs'])))
        if joueurCourantAFini(Labyrinthe['Joueurs']):
            return 2
        else :
            return 1
    return 0
#print(finirTour(laby))
