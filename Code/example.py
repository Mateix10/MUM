# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.extensions.media_keys import MediaKeys

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
PINS = [board.D1, board.D2, board.D4, board.D3, board.D0, board.D7, board.D29]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
# Also, here for media keys: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/media_keys.md
keyboard.keymap = [
    [KC.Macro(Tap(KC.MEDIA_PREV_TRACK), Tap(KC.MEDIA_REWIND)), KC.MEDIA_PLAY_PAUSE, KC.Macro(Tap(KC.MEDIA_NEXT_TRACK), Tap(KC.MEDIA_FAST_FORWARD)), KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP, KC.Macro(Press(KC.LCTRL), Press(KC.LGUI), Tap(KC.C), Release(KC.LCTRL), Release(KC.LGUI)), KC.Macro(Press(KC.LCTRL), Press(KC.LGUI), Tap(KC.V), Release(KC.LCTRL), Release(KC.LGUI))]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()