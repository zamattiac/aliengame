# Matthew Keitelman (mak2vr)
# Fernando Mata Cordero (fm5ew)

import pygame
import gamebox

camera = gamebox.Camera(1000,800,True)
alien = gamebox.from_image(150, 15, "http://people.virginia.edu/~mak2vr/files/alien/alien.png")
alien.scale_by(1.6)
alien.yspeed = 0

levels = gamebox.from_image(400,465,"right-side.png")


blue_hole_sheet = gamebox.load_sprite_sheet("http://people.virginia.edu/~mak2vr/files/alien/bluehole.png",1,5)
x = 0

blueholes = [
    # gamebox.from_image(150,7,blue_hole_sheet[0]),
    gamebox.from_image(100,7,blue_hole_sheet[0]),
    gamebox.from_image(200,7,blue_hole_sheet[1]),
    gamebox.from_image(300,7,blue_hole_sheet[2]),
    gamebox.from_image(400,7,blue_hole_sheet[3])
]

for bluehole in blueholes:
    bluehole.scale_by(3)

platforms = [
    # gamebox.from_color(-100, 600, "black", 3000, 100),
    levels
    # ground1
]

def tick(keys):

    global x
    x += 1

    if x == 3:
        x = 0

    for bluehole in blueholes:
        bluehole.image = blue_hole_sheet[x]

    # GRAVITY
    alien.yspeed += 1
    alien.y = alien.y + alien.yspeed

    if pygame.K_s in keys:
        alien.image = "http://people.virginia.edu/~mak2vr/files/alien/alien_top.png"
    elif pygame.K_d in keys:
        alien.image = "http://people.virginia.edu/~mak2vr/files/alien/alien_middle.png"
    elif pygame.K_f in keys:
        alien.image = "http://people.virginia.edu/~mak2vr/files/alien/alien_bottom.png"
    else:
        alien.image = "http://people.virginia.edu/~mak2vr/files/alien/alien.png"

    for platform in platforms:
        if alien.touches(platform):
            alien.move_to_stop_overlapping(platform)

    if pygame.K_RIGHT in keys:
        alien.x += 5
    if pygame.K_LEFT in keys:
        alien.x -= 5
    camera.clear("skyblue")
    camera.draw(alien)
    for platform in platforms:
        camera.draw(platform)
    for bluehole in blueholes:
        camera.draw(bluehole)
    camera.display()
ticks_per_second = 30

def start(keys):

    camera.clear("skyblue")
    camera.draw(gamebox.from_text(500,500,"Our Game", "Futura",20,"black"))
    camera.draw(gamebox.from_text(500,600,"Press SPACE to start", "Futura",20,'black'))

    camera.display()
    if pygame.K_SPACE in keys:
        gamebox.timer_loop(ticks_per_second, tick)

gamebox.timer_loop(ticks_per_second,start)
# keep this line the last one in your program

