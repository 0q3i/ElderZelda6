import pyxel
import math
import fonction_homepage as foncH
import fonction_jeu as foncJ
#variables importentes
Screen_h = 160
Screen_w = 120
run = False 
win = False
lost = False

pyxel.load("mygame.pyxres")

#variable importer
posXjoueur = foncJ.posXjoueur
posYjoueur = foncJ.posYjoueur
joueurW=foncJ.joueurW
joueurH=foncJ.joueurH
posXfille = foncJ.posXfille
posYfille = foncJ.posYfille
filleW=foncJ.filleW
filleH=foncJ.filleH
posXmonstre = foncJ.posXmonstre
posYmonstre= foncJ.posYmonstre
monstreW = foncJ.monstreW
monstreH =foncJ.monstreH
dict_tile = foncJ.dict_tile



#variable pour tilemap
tilemap = pyxel.tilemaps[0]
tilemap_width = Screen_w
tilemap_height = Screen_h

def update():
#variable global ou local:
  global run
  global win
  global lost
  mouse_x = pyxel.mouse_x
  mouse_y = pyxel.mouse_y
  global posXjoueur,posYjoueur
  global joueurW,joueurH
  global posXfille,posYfille
  global filleW,filleH
  global posXmonstre,posYmonstre
  global monstreH,monstreW
  global Screen_w,Screen_h
#quiter l'appli:
  if pyxel.btnp(pyxel.KEY_Q):
    pyxel.quit()

#le bouton start:
  if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and foncH.interaction(mouse_x,mouse_y,foncH.menu_interface[1]["postionX"],foncH.menu_interface[1]["postionY"],foncH.menu_interface[4]["rectW"],foncH.menu_interface[4]["rectH"]):
    run = True

#mise a jour posjoueur:
  posXjoueur, posYjoueur = foncJ.joueur_deplacement(posXjoueur, posYjoueur)

#mis a jour posEntier:
  posXfille, posYfille = foncJ.SuivreLEJoueur(posXjoueur,posYjoueur,posXfille,posYfille)
  if foncJ.dansLazoneDattaque(posXjoueur,posYjoueur,posXmonstre,posYmonstre):
    posXmonstre , posYmonstre = foncJ.SuivreLEJoueur(posXjoueur,posYjoueur,posXmonstre,posYmonstre)
    posXmonstre -= 0.5
    posYmonstre -= 0.5
#collision
  if foncJ.collision(posXjoueur,posYjoueur,dict_tile):
    posXjoueur-= 4
    posYjoueur-= 4
    
  if foncJ.collisionperdre(posXjoueur,posYjoueur,joueurW,joueurH,posXmonstre, posYmonstre,monstreW,monstreH):
    run = False
    lost = True
    
  if foncJ.collisionGagnant(posXjoueur,posYjoueur,dict_tile):
    run = False
    win = True
    
def draw():
  pyxel.cls(0)
#Homepage
  if run == False:
  #zone titre
    pyxel.rect(foncH.menu_interface[0]["postionX"],
               foncH.menu_interface[0]["postionY"],
               w=70,
               h=20,
               col=5)
  #zone bouton
    pyxel.rect(foncH.menu_interface[1]["postionX"],
               foncH.menu_interface[1]["postionY"],
               w=70,
               h=20,
               col=9)
  #titre du jeu
    pyxel.text(foncH.menu_interface[2]["postionX"],
               foncH.menu_interface[2]["postionY"],
               foncH.menu_interface[2]["text"],
               pyxel.frame_count % 16)
  #titre bouton
    pyxel.text(foncH.menu_interface[3]["postionX"],
               foncH.menu_interface[3]["postionY"],
               foncH.menu_interface[3]["text"],
               pyxel.frame_count % 16)
    pyxel.mouse(True)
  
#jeu
  if run:

  #Camera/ecranjoueur
    foncJ.ecranjoueur(posXjoueur, posYjoueur, joueurW, joueurH)
  #generation de la map
    for y in range(tilemap_height):
      for x in range(tilemap_width):
        if tilemap.pget(x, y) == dict_tile["rock_tile"]:
          pyxel.blt(x *8, y*8, 0, 16, 0, 8, 8, 8)
        elif tilemap.pget(x, y) == dict_tile["grass_tile"]:
          pyxel.blt(x*8, y*8, 0, 8, 0, 8, 8, 8)
        elif tilemap.pget(x, y) == dict_tile["dark_tile"]:
          pyxel.blt(x*8, y*8, 0, 0, 0, 8, 8, 8)
        elif tilemap.pget(x, y) == dict_tile["wood_tile"]:
          pyxel.blt(x*8, y*8, 0, 24, 0, 8, 8, 8)
        elif tilemap.pget(x,y) == dict_tile["Jeunefleur_tile"]:
          pyxel.blt(x*8,y*8, 0, 32,0,8,8)
        elif tilemap.pget(x,y) == dict_tile["Rougefleur_tile"]:
          pyxel.blt(x*8,y*8,0,40,8,8,8)
        elif tilemap.pget(x,y) == dict_tile["buisson_tile"]:
          pyxel.blt(x*8,y*8,0,32,8,8,8)
        elif tilemap.pget(x,y) == dict_tile["bouche_tile"]:
          pyxel.blt(x*8,y*8,0,40,0,8,8)
        elif tilemap.pget(x,y) == dict_tile["Pa"]:
          pyxel.blt(x*8,y*8,0,0,8,8,8)  
        elif tilemap.pget(x,y) == dict_tile["PaDw"]:
          pyxel.blt(x*8,y*8,0,8,8,8,8)        
        elif tilemap.pget(x,y) == dict_tile["toutDirectionPa"]:
          pyxel.blt(x*8,y*8,0,16,8,8,8) 
        elif tilemap.pget(x,y) == dict_tile["PaTDw"]:
          pyxel.blt(x*8,y*8,0,24,8,8,8)
        elif tilemap.pget(x,y) == dict_tile["PaDwTR"]:
          pyxel.blt(x*8,y*8,0,0,16,8,8)
        elif tilemap.pget(x,y) == dict_tile["PaDwTL"]:
          pyxel.blt(x*8,y*8,0,8,16,8,8) 
        elif tilemap.pget(x,y) == dict_tile["rondupR"]:
          pyxel.blt(x*8,y*8,0,16,16,8,8) 
        elif tilemap.pget(x,y) == dict_tile["rondupL"]:
          pyxel.blt(x*8,y*8,0,24,16,8,8) 
        elif tilemap.pget(x,y) == dict_tile["rondDwR"]:
          pyxel.blt(x*8,y*8,0,16,24,8,8) 
        elif tilemap.pget(x,y) == dict_tile["rondDwL"]:
          pyxel.blt(x*8,y*8,0,24,24,8,8)   
        elif tilemap.pget(x,y) == dict_tile["maison"]:
          pyxel.blt(x*8,y*8,0,48,0,8,8)
        elif tilemap.pget(x,y) == dict_tile["ble"]:
          pyxel.blt(x*8,y*8,0,32,16,8,8)
  #mostre 
    pyxel.blt(posXmonstre,
              posYmonstre,
              0,
              16,
              32,
              monstreW,
              monstreH,
              0)
  #fille
    pyxel.blt(posXfille,
               posYfille,
               0,
               0,
               32,
               filleW,
               filleH,
               0)
  #joueur
    print(posXjoueur,posYjoueur)
    pyxel.blt(posXjoueur,
              posYjoueur,
              0,
              8,
              32,
              joueurW,
              joueurH,
              0)
  #visibliliter du jouer 
    foncJ.lumierejoueur(posXjoueur,posYjoueur,Screen_h,Screen_w,joueurW,joueurH)
  if lost :
    pyxel.camera(0,0)
    pyxel.cls(0)
    pyxel.text(foncH.menu_interface[2]["postionX"]-55,
            foncH.menu_interface[2]["postionY"],
            "perdu faut recommencer.l'orc vous a tuer",
            pyxel.frame_count % 16)
  if win :
    pyxel.camera(0,0)
    pyxel.cls(0)
    pyxel.text(foncH.menu_interface[2]["postionX"],
               foncH.menu_interface[2]["postionY"],
               foncH.menu_interface[2]["text"],
               pyxel.frame_count % 16)
    pyxel.text(foncH.menu_interface[3]["postionX"]-55,
               foncH.menu_interface[3]["postionY"]-30,
               """Bravo pour votre courage qui vous q 
permis de ramener la 
fille perdu a son village.""",
               pyxel.frame_count % 16)
    pyxel.text(foncH.menu_interface[3]["postionX"],
            foncH.menu_interface[3]["postionY"],
            "Dev Nicolas et Thomas",
            pyxel.frame_count % 16)



pyxel.run(update, draw)
