from random import *
from joueur import *

def ListeJoueurs(nomsJoueurs):
    """
    créer une liste de joueurs dont les noms sont dans la liste de noms passés en paramètre
    Attention il s'agit d'une liste de joueurs qui gère la notion de joueur courant
    paramètre: nomsJoueurs une liste de chaines de caractères
    résultat: la liste des joueurs avec un joueur courant mis à 0
    """
    res = []
    for joueur in nomsJoueurs:
        res.append([joueur,[]])
    return res


def ajouterJoueur(joueurs, joueur):
    """
    ajoute un nouveau joueur à la fin de la liste
    paramètres: joueurs un liste de joueurs
                joueur le joueur à ajouter
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    joueurs.append([joueur,[]])


def initAleatoireJoueurCourant(joueurs):
    """
    tire au sort le joueur courant
    paramètre: joueurs un liste de joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    joueurCourant = randint(1,len(joueurs))
    joueurs.reverse()
    joueurs.append(joueurCourant)
    joueurs.reverse()


def distribuerTresors(joueurs,nbTresors=24, nbTresorMax=0):
    """
    distribue de manière aléatoire des trésors entre les joueurs.
    paramètres: joueurs la liste des joueurs
                nbTresors le nombre total de trésors à distribuer (on rappelle 
                        que les trésors sont des entiers de 1 à nbTresors)
                nbTresorsMax un entier fixant le nombre maximum de trésor 
                            qu'un joueur aura après la distribution
                            si ce paramètre vaut 0 on distribue le maximum
                            de trésor possible  
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    tresorsADistribuer = list(range(1,nbTresors+1))
    shuffle(tresorsADistribuer)
    if nbTresorMax!=0 :
        for i in range(1,len(joueurs)):
            for _ in range(nbTresorMax):
                joueurs[i][1].append(tresorsADistribuer[0])
                del tresorsADistribuer[0]
    else :
        while len(tresorsADistribuer) >= len(joueurs)-1:
            for i in range(1,len(joueurs)):
                joueurs[i][1].append(tresorsADistribuer[0])
                del tresorsADistribuer[0]


def changerJoueurCourant(joueurs):
    """
    passe au joueur suivant (change le joueur courant donc)
    paramètres: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """   
    joueurs[0] += 1
    if joueurs[0] > len(joueurs)-1:
        joueurs[0] = 1


def getNbJoueurs(joueurs):
    """
    retourne le nombre de joueurs participant à la partie
    paramètre: joueurs la liste des joueurs
    résultat: le nombre de joueurs de la partie
    """
    return len(joueurs)-1


def getJoueurCourant(joueurs):
    """
    retourne le joueur courant
    paramètre: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    return joueurs[joueurs[0]]


def joueurCourantTrouveTresor(joueurs):
    """
    Met à jour le joueur courant lorsqu'il a trouvé un trésor
    c-à-d enlève le trésor de sa liste de trésors à trouver
    paramètre: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    tresorTrouve(joueurs[joueurs[0]])


def nbTresorsRestantsJoueur(joueurs,numJoueur):
    """
    retourne le nombre de trésor restant pour le joueur dont le numero 
    est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur
    résultat: le nombre de trésors que joueur numJoueur doit encore trouver
    """
    return getNbTresorsRestants(joueurs[numJoueur])


def numJoueurCourant(joueurs):
    """
    retourne le numéro du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le numéro du joueur courant
    """
    return joueurs[0]


def nomJoueurCourant(joueurs):
    """
    retourne le nom du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le nom du joueur courant
    """
    return joueurs[joueurs[0]][0]


def nomJoueur(joueurs,numJoueur):
    """
    retourne le nom du joueur dont le numero est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur    
    résultat: le nom du joueur numJoueur
    """
    return joueurs[numJoueur][0]


def prochainTresorJoueur(joueurs,numJoueur):
    """
    retourne le trésor courant du joueur dont le numero est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur    
    résultat: le prochain trésor du joueur numJoueur (un entier)
    """
    return joueurs[numJoueur][0]


def tresorCourant(joueurs):
    """
    retourne le trésor courant du joueur courant
    paramètre: joueurs la liste des joueurs 
    résultat: le prochain trésor du joueur courant (un entier)
    """
    return joueurs[joueurs[0]][1][0]


def joueurCourantAFini(joueurs):
    """
    indique si le joueur courant a gagné
    paramètre: joueurs la liste des joueurs 
    résultat: un booleen indiquant si le joueur courant a fini
    """
    if joueurs[joueurs[0]][1] == []:
        return True
    return False