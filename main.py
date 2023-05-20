basic.show_string("Good Morring")
basic.show_icon(IconNames.HAPPY) 
basic.show_leds("""
. # # . .
# . . # .
. # . . .
# . # . .
# # # . .
""")
def on_button_pressed_a():
    
    basic.show_string("Birthday year")
    basic.show_number(2004)
input.on_button_pressed(Button.B, on_button_pressed_a)
def on_gesture_shake():
    basic.show_string("My Age")
basic.show_number(19)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)