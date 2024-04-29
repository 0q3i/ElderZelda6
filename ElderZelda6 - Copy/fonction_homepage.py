import pyxel 
# fonction global
menu_interface= [
  {"nom":"Zone Elder Zelda 6","postionX":45,"postionY":30},
  {"nom":"bouton pour jouer","postionX":45,"postionY":70},
  {"text":"Elder Zelda 6","postionX":55,"postionY":38},
  {"text":"start","postionX":70,"postionY":78},
  {"rectW":70,"rectH":20}
]

def interaction(mouse_x, mouse_y, x=0 , y=0 , w =0, h=0):
  """Renvois un bool. regarde si les carré de collision sont en train de ce cheuvaucher"""
  if mouse_x > x and mouse_x < x + w and mouse_y > y and mouse_y < y + h:
    return True
  return False
