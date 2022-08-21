def on_button_pressed_a():
    global canastahorizontal, canasta
    if canastahorizontal > 0:
        canasta.delete()
        canastahorizontal += -1
        canasta = game.create_sprite(canastahorizontal, canastavertical)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global canastahorizontal, canasta
    if canastahorizontal < 4:
        canasta.delete()
        canastahorizontal += 1
        canasta = game.create_sprite(canastahorizontal, canastavertical)
input.on_button_pressed(Button.B, on_button_pressed_b)

bolahorizontal3 = 0
bola3: game.LedSprite = None
bolahorizontal2 = 0
bola2: game.LedSprite = None
bola: game.LedSprite = None
canasta: game.LedSprite = None
canastahorizontal = 0
canastavertical = 0
canastavertical = 4
canastahorizontal = 2
bolahorizontal = 2
bolavertical = 0
bolavertical2 = -1
bolavertical3 = -2
velocidadbola = 1000
fallas = 0
game.set_score(0)
basic.show_icon(IconNames.HEART)
canasta = game.create_sprite(canastahorizontal, canastavertical)

def on_forever():
    global bola, bolavertical, bolahorizontal
    if fallas <= 3:
        if bolavertical < 4:
            bola = game.create_sprite(bolahorizontal, bolavertical)
            basic.pause(velocidadbola)
            bola.delete()
            bolavertical += 1
            basic.pause(100)
        else:
            bolavertical = 0
            bolahorizontal = randint(0, 4)
            basic.pause(100)
basic.forever(on_forever)

def on_forever2():
    global velocidadbola, fallas
    if fallas <= 3:
        if bolavertical == 4:
            if bolahorizontal == canastahorizontal:
                game.add_score(1)
                music.ring_tone(262)
                basic.pause(50)
                music.stop_all_sounds()
                basic.pause(velocidadbola)
                if velocidadbola > 500:
                    velocidadbola += -5
            else:
                fallas += 1
                basic.pause(velocidadbola)
basic.forever(on_forever2)

def on_forever3():
    global bola2, bolavertical2, bolahorizontal2
    if fallas <= 3:
        if game.score() > 10:
            if bolavertical2 < 4:
                bola2 = game.create_sprite(bolahorizontal2, bolavertical2)
                basic.pause(velocidadbola)
                bola2.delete()
                bolavertical2 += 1
                basic.pause(100)
            else:
                bolavertical2 = bolavertical - 2
                bolahorizontal2 = randint(0, 4)
                basic.pause(100)
basic.forever(on_forever3)

def on_forever4():
    global velocidadbola, fallas
    if fallas <= 3:
        if bolavertical2 == 4:
            if bolahorizontal2 == canastahorizontal:
                game.add_score(1)
                music.ring_tone(262)
                basic.pause(50)
                music.stop_all_sounds()
                basic.pause(velocidadbola)
                if velocidadbola > 500:
                    velocidadbola += -5
            else:
                fallas += 1
                basic.pause(velocidadbola)
basic.forever(on_forever4)

def on_forever5():
    global bola3, bolavertical3, bolahorizontal3
    if fallas <= 3:
        if game.score() > 25:
            if bolavertical3 < 4:
                bola3 = game.create_sprite(bolahorizontal3, bolavertical3)
                basic.pause(velocidadbola)
                bola3.delete()
                bolavertical3 += 1
                basic.pause(100)
            else:
                bolavertical3 = bolavertical2 - 2
                bolahorizontal3 = randint(0, 4)
                basic.pause(100)
basic.forever(on_forever5)

def on_forever6():
    global velocidadbola, fallas
    if fallas <= 3:
        if bolavertical3 == 4:
            if bolahorizontal3 == canastahorizontal:
                game.add_score(1)
                music.ring_tone(262)
                basic.pause(50)
                music.stop_all_sounds()
                basic.pause(velocidadbola)
                if velocidadbola > 500:
                    velocidadbola += -5
            else:
                fallas += 1
                basic.pause(velocidadbola)
basic.forever(on_forever6)

def on_forever7():
    if fallas > 3:
        soundExpression.giggle.play()
        game.game_over()
basic.forever(on_forever7)
