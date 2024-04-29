import pyxel 
import math

#variables importentes
Screen_h = 160
Screen_w = 120

pyxel.init(Screen_h, Screen_w,title="Elder Zelda 6",fps=60)

pyxel.load("mygame.pyxres")

"""map est une liste contenant des dictionnaires"""

'''R = droit; L = gauche; Pa = chmain; T = tourne ver; Dw = ver le bas
pour pouvoiur lire les chemain'''

dict_tile ={
  #tile noir
  "dark_tile":(0, 0),
  #vegetation 
  "grass_tile": (1, 0),
  "rock_tile" : (2, 0),
  "wood_tile" : (3, 0),#on peut pas traverser 
  "Jeunefleur_tile" :(4,0),
  "Rougefleur_tile" : (5,1),
  "buisson_tile" : (4,1),#on peut pas traverser
  "bouche_tile" : (5,0),
  #les chemain
  "Pa" : (0,1),
  "PaDw" : (1,1),
  "toutDirectionPa" : (2,1),
  "PaTDw": (3,1),
  "PaDwTR" : (0,2),
  "PaDwTL" : (1,2),
  "rondupR" : (2,2),
  "rondupL" : (3,2),
  "rondDwR" : (2,3),
  "rondDwL" : (3,3),
  #village
  "ble" : (4,2),
  "maison" : (6,0)
}
map_personnage = [
    {"personnage":"joueur","positionX":20,"positionY":10,"w":8,"h":8},
    {"personnage":"fille","positionX":19,"positionY":12,"w":8,"h":8},
    {"personnage":"monstre","positionX":450,"positionY":120,"w":8,"h":8}
    ]

# Variable utile 
posXjoueur = map_personnage[0]["positionX"]
posYjoueur = map_personnage[0]["positionY"]
joueurW = map_personnage[0]["w"]
joueurH = map_personnage[0]["h"]
posXfille  = map_personnage[1]["positionX"]
posYfille = map_personnage[1]["positionY"]
filleW = map_personnage[1]["w"]
filleH = map_personnage[1]["h"]
posXmonstre = map_personnage[2]["positionX"]
posYmonstre= map_personnage[2]["positionY"]
monstreW = map_personnage[2]["w"]
monstreH = map_personnage[2]["h"]
tilemap = pyxel.tilemaps[0]

def dansLazoneDattaque(posXjoueur,posYjoueur,posXmonstre,posYmonstre):
  if posXjoueur > (posXmonstre-posXmonstre/2) and posXjoueur < (posXmonstre + posXmonstre/2) and posYjoueur > (posYmonstre-posYmonstre/2) and posYjoueur <(posYmonstre+posYmonstre/2):
    return True
  else:
    return False 

def SuivreLEJoueur(posXjoueur,posYjoueur,posXentier,posYentier):
  """renvois None. permmet aux monstre et la fille de suivre le joueur"""
  posXjoueur-=8
  posYjoueur-=8
  if posXjoueur < posXentier:
    posXentier -= 1
  if posXjoueur > posXentier: 
    posXentier += 1
  if posYjoueur < posYentier:  
    posYentier -= 1
  if posYjoueur > posYentier:  
    posYentier += 1
  return posXentier  , posYentier 

def joueur_deplacement(posXjoueur, posYjoueur):
 """déplacement avec les touches de directions"""
 if pyxel.btn(pyxel.KEY_RIGHT):
     if (posXjoueur < 720) :
       posXjoueur = posXjoueur + 2
 if pyxel.btn(pyxel.KEY_LEFT):
     if (posXjoueur > 0) :
       posXjoueur = posXjoueur - 2
 if pyxel.btn(pyxel.KEY_DOWN):
     if (posYjoueur < 720) :
       posYjoueur = posYjoueur + 2
 if pyxel.btn(pyxel.KEY_UP):
     if (posYjoueur > 0) :
       posYjoueur = posYjoueur - 2
 return posXjoueur, posYjoueur

def collision(posXjoueur,posYjoueur,dict_tile):
  """renvois Booléen. regarde si le joueur et les obstacles sont en collision"""
  posXjoueur, posYjoueur = math.floor(posXjoueur/8),math.floor(posYjoueur/8)
  if tilemap.pget(posXjoueur,posYjoueur) == dict_tile["wood_tile"]:
    return True
  elif tilemap.pget(posXjoueur,posYjoueur) == dict_tile["buisson_tile"]:
    return True 
  else:
    return False

def collisionperdre(posXjoueur,posYjoueur,joueurW,joueurH,posXmonstre, posYmonstre,monstreW,monstreH):
  """renvois Booléen. regarde si le joueur et les obstacles sont en collision"""
  
  if posXjoueur < posXmonstre + monstreW and posXjoueur > posXmonstre and posYjoueur < posYmonstre + monstreH and posYjoueur > posYmonstre:
    return True
  else:
    return False  

def collisionGagnant(posXjoueur,posYjoueur,dict_tile):
  """renvois Booléen. regarde si le joueur et les obstacles sont en collision"""
  posXjoueur, posYjoueur = math.floor(posXjoueur/8),math.floor(posYjoueur/8)
  if tilemap.pget(posXjoueur,posYjoueur) == dict_tile["maison"]:
    return True
  else:
    return False
  
def lumierejoueur(posXjoueur, posYjoueur,screen_h, screen_w,joueurW,joueurH):
  """renvoie None.Efface l’écran avec la couleur col"""
  #rectangle du haut
  pyxel.rect(posXjoueur-joueurW*3,
             posYjoueur-joueurH*8,
             screen_w,
             screen_h/4,
             0
             )
  #retangle du bas 
  pyxel.rect(posXjoueur-joueurW*3,
             posYjoueur+joueurH*4,
             screen_w,
             screen_h/4,
             0
             )
  #retangle de la droit 
  pyxel.rect(posXjoueur-joueurW*10,
             posYjoueur-joueurH*7,
             screen_w/2,
             screen_h,
            0)
  #retangle de la gauche 
  pyxel.rect(posXjoueur+joueurW*4,
             posYjoueur-joueurH*7,
             screen_w,
             screen_h,
            0)
  return None

def ecranjoueur(posXjoueur, posYjoueur, joueurW, joueurH):
  """renvois un None. elle délimite une espace dans la map pour le joueur"""
  pyxel.camera(posXjoueur-joueurW*9,posYjoueur-joueurH*7)
  return None 



