let jugador = 0
let bot = 0
input.onButtonPressed(Button.A, function () {
    jugador = randint(1, 3)
    if (jugador == 1) {
        basic.showIcon(IconNames.Square)
    } else if (jugador == 2) {
        basic.showIcon(IconNames.SmallSquare)
    } else {
        basic.showIcon(IconNames.Scissors)
    }
})
input.onButtonPressed(Button.AB, function () {
    if (jugador == 1 && bot == 2 || (jugador == 2 && bot == 3 || jugador == 3 && bot == 1)) {
        basic.showIcon(IconNames.Yes)
    } else if (jugador == 1 && bot == 3 || (jugador == 3 && bot == 2 || jugador == 2 && bot == 1)) {
        basic.showIcon(IconNames.No)
    } else {
        basic.showIcon(IconNames.Sad)
    }
})
input.onButtonPressed(Button.B, function () {
    bot = randint(1, 3)
    if (bot == 1) {
        basic.showIcon(IconNames.Square)
    } else if (bot == 2) {
        basic.showIcon(IconNames.SmallSquare)
    } else {
        basic.showIcon(IconNames.Scissors)
    }
})
