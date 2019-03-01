from random import * 


"""
la liste des caractères semi-graphiques correspondant aux différentes cartes
l'indice du caractère dans la liste correspond au codage des murs sur la carte
le caractère 'Ø' indique que l'indice ne correspond pas à une carte
"""
listeCartes=['╬','╦','╣','╗','╩','═','╝','Ø','╠','╔','║','Ø','╚','Ø','Ø','Ø']


def Carte( nord, est, sud, ouest, tresor=0, pions=[]):
    """
    permet de créer une carte:
    paramètres:
    nord, est, sud et ouest sont des booléens indiquant s'il y a un mur ou non dans chaque direction
    tresor est le numéro du trésor qui se trouve sur la carte (0 s'il n'y a pas de trésor)
    pions est la liste des pions qui sont posés sur la carte (un pion est un entier entre 1 et 4)
    """
    
    c={}
    c["mur"]=[]
    if nord:
        c["mur"].append('nord')
    if est:
        c["mur"].append('est')
    if sud:
        c["mur"].append('sud')
    if ouest:
        c["mur"].append('ouest')
    c["tresor"]=tresor
    c["pions"]=pions
    return c
    
assert Carte(True,False,True,False,1,[1,2]) == {'mur': ["nord","sud"], 'tresor': 1, 'pions': [1, 2]}
assert Carte(False,False,False,False,1,[]) == {'mur':[], 'tresor': 1, 'pions': []}

def estValide(c):
    """
    retourne un booléen indiquant si la carte est valide ou non c'est à dire qu'elle a un ou deux murs
    paramètre: c une carte
    """
    if len(c["mur"])<=2:
        return True
    else: 
        return False

assert estValide(Carte(True,False,True,False,1,[1,2])) == True
assert estValide(Carte(True,True,True,True,1,[])) == False

def murNord(c):
    """
    retourne un booléen indiquant si la carte possède un mur au nord
    paramètre: c une carte
    """
    return "nord" in c["mur"] 

assert murNord(Carte(True,False,True,False,1,[1,2])) == True
assert murNord(Carte(False,False,True,False,1,[1,2])) == False

def murSud(c):
    """
    retourne un booléen indiquant si la carte possède un mur au sud
    paramètre: c une carte
    """
    return "sud" in c["mur"] 

assert murSud(Carte(True,False,True,False,1,[1,2])) == True
assert murSud(Carte(False,True,False,False,1,[1,2])) == False

def murEst(c):
    """
    retourne un booléen indiquant si la carte possède un mur à l'est
    paramètre: c une carte
    """
    return "est" in c["mur"] 

assert murEst(Carte(True,False,True,False,1,[1,2])) == False
assert murEst(Carte(False,True,False,False,1,[1,2])) == True

def murOuest(c):
    """
    retourne un booléen indiquant si la carte possède un mur à l'ouest
    paramètre: c une carte
    """
    return "ouest" in c["mur"] 

assert murOuest(Carte(True,False,True,False,1,[1,2])) == False
assert murOuest(Carte(False,True,False,True,1,[1,2])) == True

def getListePions(c):
    """
    retourne la liste des pions se trouvant sur la carte
    paramètre: c une carte
    """
    return c["pions"]

assert getListePions(Carte(True,False,True,False,1,[1,2])) == [1,2]

def setListePions(c,listePions):
    """
    place la liste des pions passées en paramètre sur la carte
    paramètres: c: est une carte
                listePions: la liste des pions à poser
    Cette fonction ne retourne rien mais modifie la carte
    """
    c["pions"]=listePions
    

def getNbPions(c):
    """
    retourne le nombre de pions se trouvant sur la carte
    paramètre: c une carte
    """
    return len(c["mur"])

assert getNbPions(Carte(True,False,True,False,1,[1,2])) == 2

def possedePion(c,pion):
    """
    retourne un booléen indiquant si la carte possède le pion passé en paramètre
    paramètre: c une carte
    """
    return pion in c["pions"]

assert possedePion(Carte(True,False,True,False,1,[1,2]),3) == False
assert possedePion(Carte(True,False,True,False,1,[1,2]),1) == True

def getTresor(c):
    """
    retourne la valeur du trésor qui se trouve sur la carte (0 si pas de trésor)
    paramètre: c une carte
    """
    return c["tresor"]

assert getTresor(Carte(True,False,True,False,1,[1,2])) == 1
assert getTresor(Carte(True,False,True,False,4,[1,2])) == 4

def prendreTresor(c):
    """
    enlève le trésor qui se trouve sur la carte et retourne la valeur de ce trésor
    paramètre: c une carte
    Cette fonction modifie la carte mais ne retourne rien
    """
    tresorpris=c["tresor"]
    c["tresor"]=0
    return tresorpris

assert prendreTresor(Carte(True,False,True,False,4,[1,2])) == 4

def mettreTresor(c,tresor):
    """
    met le trésor passé en paramètre sur la carte et retourne la valeur de l'ancien trésor
    paramètres: c une carte
                tresor un entier positif
    Cette fonction modifie la carte mais ne retourne rien
    """
    tresorchangé=c["tresor"]
    c["tresor"]=tresor
    return tresorchangé

assert mettreTresor(Carte(True,False,True,False,4,[1,2]),2) == 4

def prendrePion(c, pion):
    """
    enlève le pion passé en paramètre de la carte. Si le pion n'y était pas ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien    
    """
    if pion in c["pion"]:
        pion.remove(pion)



def poserPion(c, pion):
    """
    pose le pion passé en paramètre sur la carte. Si le pion y était déjà ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien    
    """
    if pion not in c["pion"]:
        pion.append(pion)


def tournerHoraire(c):
    """
    fait tourner la carte dans le sens horairenord
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    if "nord" in c["mur"]:
        nord=True
    else:
        nord=False
    if "est" in c["mur"]:
        est=True
    else:
        est=False
    if "sud" in c["mur"]:
        sud=True
    else:
        sud=False
    if "ouest" in c["mur"]:
        ouest=True
    else:
        ouest=False       
    stock=est
    est=nord
    nord=ouest
    ouest=sud
    sud=stock
    
    c["mur"]=[]
    if nord:
        c["mur"].append('nord')
    if est:
        c["mur"].append('est')
    if sud:
        c["mur"].append('sud')
    if ouest:
        c["mur"].append('ouest')
    
def tournerAntiHoraire(c):
    """
    fait tourner la carte dans le sens anti-horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    if "nord" in c["mur"]:
        nord=True
    else:
        nord=False
    if "est" in c["mur"]:
        est=True
    else:
        est=False
    if "sud" in c["mur"]:
        sud=True
    else:
        sud=False
    if "ouest" in c["mur"]:
        ouest=True
    else:
        ouest=False       
    stock=ouest
    ouest=nord
    nord=est
    est=sud
    sud=stock
    
    c["mur"]=[]
    if nord:
        c["mur"].append('nord')
    if est:
        c["mur"].append('est')
    if sud:
        c["mur"].append('sud')
    if ouest:
        c["mur"].append('ouest')
    
def tourneAleatoire(c):
    """
    faire tourner la carte d'un nombre de tours aléatoire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    for x in range(0,randint(0,3)):
        tournerHoraire(c)
    return c
    

def coderMurs(c):
    """
    code les murs sous la forme d'un entier dont le codage binaire 
    est de la forme bNbEbSbO où bN, bE, bS et bO valent 
       soit 0 s'il n'y a pas de mur dans dans la direction correspondante
       soit 1 s'il y a un mur dans la direction correspondante
    bN est le chiffre des unité, BE des dizaine, etc...
    le code obtenu permet d'obtenir l'indice du caractère semi-graphique
    correspondant à la carte dans la liste listeCartes au début de ce fichier
    paramètre c une carte
    retourne un entier indice du caractère semi-graphique de la carte
    """
    res = 0
    if "nord" in c["mur"]:
        res+=1
    if "est" in c["mur"]:
        res+=10
    if "sud" in c["mur"]:
        res+=100
    if "ouest" in c["mur"]:
        res+=1000
    return int(str(res),2)

assert coderMurs(Carte(True,False,True,False,4,[1,2])) == 5

def decoderMurs(c,code):
    """
    positionne les murs d'une carte en fonction du code décrit précédemment
    paramètres c une carte
               code un entier codant les murs d'une carte
    Cette fonction modifie la carte mais ne retourne rien
    """ 
    c["mur"]=[]   
    if code -8 >= 0:
        code=code-8
        c["mur"].append("ouest")
    if code - 4 >= 0:
        code=code-4
        c["mur"].append("sud")
    if code - 2 >= 0:
        code=code-2
        c["mur"].append("est")
    if code - 1 >= 0:
        code=code-1
        c["mur"].append("nord")
    
    
    
def toChar(c):
    """
    fournit le caractère semi graphique correspondant à la carte (voir la variable listeCartes au début de ce script)
    paramètres c une carte
    """
    return listeCartes[coderMurs(c)]

def passageNord(carte1,carte2):
    """
    suppose que la carte2 est placée au nord de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le nord
    paramètres carte1 et carte2 deux carte
    résultat un booléen
    """
    return not "sud" in carte2["mur"] and not "nord" in carte1["mur"]
        

# assert passageNord(Carte(False,False,True,False,4,[1,2]),Carte(True,False,False,False,4,[1,2])) == True
# assert passageNord(Carte(False,False,True,False,4,[1,2]),Carte(True,False,True,False,4,[1,2])) == False

def passageSud(carte1,carte2):
    """
    suppose que la carte2 est placée au sud de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le sud
    paramètres carte1 et carte2 deux carte
    résultat un booléen
    """
    return not "sud" in carte1["mur"] and not "nord" in carte2["mur"]

# assert passageSud(Carte(True,False,True,False,4,[1,2]),Carte(True,False,True,False,4,[1,2])) == True
# assert passageSud(Carte(False,False,False,False,4,[1,2]),Carte(True,False,True,False,4,[1,2])) == False

def passageOuest(carte1,carte2):
    """
    suppose que la carte2 est placée à l'ouest de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'ouest
    paramètres carte1 et carte2 deux carte
    résultat un booléen
    """
    return  not "ouest" in carte1["mur"] and not "est" in carte2["mur"]
    
# assert passageOuest(Carte(True,False,True,False,4,[1,2]),Carte(True,False,True,False,4,[1,2])) == False
# assert passageOuest(Carte(False,False,False,True,4,[1,2]),Carte(True,True,True,False,4,[1,2])) == True

def passageEst(carte1,carte2):
    """
    suppose que la carte2 est placée à l'est de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'est
    paramètres carte1 et carte2 )deux carte
    résultat un booléen    
    """
    return not "ouest" in carte2["mur"] and not "est" in carte1["mur"]
        

# assert passageEst(Carte(True,False,True,True,4,[1,2]),Carte(True,True,True,False,4,[1,2])) == False
# assert passageEst(Carte(False,True,False,False,4,[1,2]),Carte(True,False,True,True,4,[1,2])) == True