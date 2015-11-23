# Matthew Keitelman (mak2vr)
# Fernando Mata Cordero (fm5ew)

import pygame
import gamebox
import random

camera = gamebox.Camera(1000,800,True)
alien = gamebox.from_image(30, 15, "http://people.virginia.edu/~mak2vr/files/alien/alien.png")
alien.scale_by(1.6)
alien.yspeed = 0


platforms = [gamebox.from_color(50,100,"black",1000,20),

]


blue_hole_sheet = gamebox.load_sprite_sheet("http://people.virginia.edu/~mak2vr/files/alien/bluehole.png",1,5)
x = 0

blueholes = []

for bluehole in blueholes:
    bluehole.scale_by(3)

score = 0


def tick(keys):

    global x, score
    x += 10

    score += 1
    scoreboard = gamebox.from_text(800+x,50,(str(score)),"Verdana",26,"black")

    camera.x += 10
    alien.x += 10

    for bluehole in blueholes:
        bluehole.image = blue_hole_sheet[x]

    # GRAVITY
    alien.yspeed += 1
    alien.y = alien.y + alien.yspeed

    if pygame.K_SPACE in keys:
        alien.yspeed -= 10

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
        if platform.x < (camera.x-1000):
            platforms.remove(platform)

    if pygame.K_RIGHT in keys:
        alien.x += 5
    if pygame.K_LEFT in keys:
        alien.x -= 5
    camera.clear("skyblue")
    camera.draw(alien)
    camera.draw(scoreboard)
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

