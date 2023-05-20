basic.showString("Good Morring")
basic.showIcon(IconNames.Happy)
basic.showLeds(`
. # # . .
# . . # .
. # . . .
# . # . .
# # # . .
`)
input.onButtonPressed(Button.B, function on_button_pressed_a() {
    basic.showString("Birthday year")
    basic.showNumber(2004)
})
basic.showNumber(19)
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    basic.showString("My Age")
})
