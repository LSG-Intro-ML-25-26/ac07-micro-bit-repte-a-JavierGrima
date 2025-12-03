mano = 0

def on_gesture_shake():
    global mano
    mano = randint(1, 3)
    if mano == 1:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif mano == 2:
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_icon(IconNames.SCISSORS)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
