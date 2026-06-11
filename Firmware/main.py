# main.py
import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC

keyboard = KMKKeyboard()

# Buttons wired to D0-D3 and GND
keyboard.direct_pins = [
    board.D0,  # SW1
    board.D1,  # SW2
    board.D2,  # SW3
    board.D3,  # SW4
]

keyboard.coord_mapping = (0, 1, 2, 3)

# Key assignments
keyboard.keymap = [
    [
        KC.COPY,
        KC.PASTE,
        KC.CUT,
        KC.UNDO,
    ]
]

if __name__ == "__main__":
    keyboard.go()
