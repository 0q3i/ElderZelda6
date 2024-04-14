#fonction main.py
import pyxel
import fonction_homepage as foncH
import fonction_jeu as foncJ
  #variables importentes
Screen_h = 160
Screen_w = 120
posXjoueur = foncJ.posXjoueur
posYjoueur = foncJ.posYjoueur
joueurW=foncJ.joueurW
joueurH=foncJ.joueurH
posXfille = foncJ.posXfille
posYfille = foncJ.posYfille
filleW=foncJ.filleW
filleH=foncJ.filleH
run = False 

pyxel.init(Screen_h, Screen_w,title="Elder Zelda 6",fps=60)

pyxel.load("mygame.pyxres")

def update():
#variable global ou local:
  global run
  mouse_x = pyxel.mouse_x
  mouse_y = pyxel.mouse_y
  global posXjoueur,posYjoueur
  global joueurW,joueurH
  global posXfille,posYfille
  global filleW,filleH
#quiter l'appli:
  if pyxel.btnp(pyxel.KEY_Q):
    pyxel.quit()

#le bouton start:
  if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and foncH.interaction(mouse_x,mouse_y,foncH.menu_interface[1]["postionX"],foncH.menu_interface[1]["postionY"],foncH.menu_interface[4]["rectW"],foncH.menu_interface[4]["rectH"]):
    run = True

#mise a jour posjoueur:
  posXjoueur, posYjoueur = foncJ.joueur_deplacement(posXjoueur, posYjoueur)

#mis a jour posfille:
  posXfille, posYfille = foncJ.filleQuiSuiteJoueur(posXjoueur,posYjoueur,posXfille,posYfille)

def draw():
  foncJ.NoirMap(0)
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
  if run:
  #Camera/ecranjoueur
    foncJ.ecranjoueur(posXjoueur, posYjoueur, joueurW, joueurH)
  #Map
    pyxel.rect(-100,-100,w=1000,h=1000,col=11)
    pyxel.rect(100, 0, w=40, h=1000, col=8)
    pyxel.rect(0, 100, w=1000, h=40, col=8)
    #fille
    pyxel.rect(posXfille, 
               posYfille, 
               filleW,
               filleH,      
               col=16)
    pyxel.blt(posXfille,
               posYfille,
               0,
               0,
               16,
               8,
               8)
    print("posXfille",posXfille,"posYfille",posYfille)
  #joueur
    #pyxel.circ(posXjoueur, posYjoueur, 20, col=10)
    pyxel.rect(posXjoueur,
               posYjoueur,
               joueurW,
               joueurH,
               col=6)
    pyxel.blt(posXjoueur,
               posYjoueur,
               0,
               16,
               0,
               8,
               8)
    
    print("posXjoueur",posXjoueur,"posYjoueur",posYjoueur)
  
pyxel.run(update, draw)
