jugador = 0
bot = 0

def on_button_pressed_a():
    global jugador
    jugador = randint(1, 3)
    if jugador == 1:
        basic.show_icon(IconNames.SQUARE)
    elif jugador == 2:
        basic.show_icon(IconNames.SMALL_SQUARE)
    else:
        basic.show_icon(IconNames.SCISSORS)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global bot
    bot = randint(1, 3)
    if bot == 1:
        basic.show_icon(IconNames.SQUARE)
    elif bot == 2:
        basic.show_icon(IconNames.SMALL_SQUARE)
    else:
        basic.show_icon(IconNames.SCISSORS)
input.on_button_pressed(Button.B, on_button_pressed_b)
