input.onButtonPressed(Button.A, function () {
    if (canastahorizontal > 0) {
        canasta.delete()
        canastahorizontal += -1
        canasta = game.createSprite(canastahorizontal, canastavertical)
    }
})
input.onButtonPressed(Button.B, function () {
    if (canastahorizontal < 4) {
        canasta.delete()
        canastahorizontal += 1
        canasta = game.createSprite(canastahorizontal, canastavertical)
    }
})
let bola: game.LedSprite = null
let bolahorizontal3 = 0
let bola3: game.LedSprite = null
let bolahorizontal2 = 0
let bola2: game.LedSprite = null
let bolavertical = 0
let fallas = 0
let canasta: game.LedSprite = null
let canastahorizontal = 0
let canastavertical = 0
canastavertical = 4
canastahorizontal = 2
let bolahorizontal = 2
let bolavertical2 = -1
let bolavertical3 = -2
let velocidadbola = 1000
game.setScore(0)
basic.showIcon(IconNames.Heart)
canasta = game.createSprite(canastahorizontal, canastavertical)
basic.forever(function () {
    if (fallas <= 3) {
        if (bolavertical == 4) {
            if (bolahorizontal == canastahorizontal) {
                game.addScore(1)
                music.ringTone(262)
                basic.pause(50)
                music.stopAllSounds()
                basic.pause(velocidadbola)
                if (velocidadbola > 500) {
                    velocidadbola += -5
                }
            } else {
                fallas += 1
                basic.pause(velocidadbola)
            }
        }
    }
})
basic.forever(function () {
    if (fallas <= 3) {
        if (game.score() > 10) {
            if (bolavertical2 < 4) {
                bola2 = game.createSprite(bolahorizontal2, bolavertical2)
                basic.pause(velocidadbola)
                bola2.delete()
                bolavertical2 += 1
                basic.pause(100)
            } else {
                bolavertical2 = bolavertical - 2
                bolahorizontal2 = randint(0, 4)
                basic.pause(100)
            }
        }
    }
})
basic.forever(function () {
    if (fallas <= 3) {
        if (bolavertical2 == 4) {
            if (bolahorizontal2 == canastahorizontal) {
                game.addScore(1)
                music.ringTone(262)
                basic.pause(50)
                music.stopAllSounds()
                basic.pause(velocidadbola)
                if (velocidadbola > 500) {
                    velocidadbola += -5
                }
            } else {
                fallas += 1
                basic.pause(velocidadbola)
            }
        }
    }
})
basic.forever(function () {
    if (fallas <= 3) {
        if (game.score() > 25) {
            if (bolavertical3 < 4) {
                bola3 = game.createSprite(bolahorizontal3, bolavertical3)
                basic.pause(velocidadbola)
                bola3.delete()
                bolavertical3 += 1
                basic.pause(100)
            } else {
                bolavertical3 = bolavertical2 - 2
                bolahorizontal3 = randint(0, 4)
                basic.pause(100)
            }
        }
    }
})
basic.forever(function () {
    if (fallas <= 3) {
        if (bolavertical3 == 4) {
            if (bolahorizontal3 == canastahorizontal) {
                game.addScore(1)
                music.ringTone(262)
                basic.pause(50)
                music.stopAllSounds()
                basic.pause(velocidadbola)
                if (velocidadbola > 500) {
                    velocidadbola += -5
                }
            } else {
                fallas += 1
                basic.pause(velocidadbola)
            }
        }
    }
})
basic.forever(function () {
    if (fallas > 3) {
        soundExpression.giggle.play()
        game.gameOver()
    }
})
basic.forever(function () {
    if (fallas <= 3) {
        if (bolavertical < 4) {
            bola = game.createSprite(bolahorizontal, bolavertical)
            basic.pause(velocidadbola)
            bola.delete()
            bolavertical += 1
            basic.pause(100)
        } else {
            bolavertical = 0
            bolahorizontal = randint(0, 4)
            basic.pause(100)
        }
    }
})
