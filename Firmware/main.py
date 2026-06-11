#This will be the main file for the minikeyboard code
import board

from kmk.kmk_keyboard import keyboard
from kmk.keys import KC

keyboard= KMKKeyboard()

# Four direct-wired buttons
keyboard.direct_pins=[
    board.D0, #SW1
    board.D1, #SW2
    board.D2, #SW3
    board.D3, #SW4

]

keyboard.coord_mapping=(0,1,2,3)

# key assignments 
keyboard.keymap=[
    [
        KC.F13,
        KC.F14,
        KC.F15,
        KC.F16,
    ]
]

if __name__=="__main__":
  keyboard.go()