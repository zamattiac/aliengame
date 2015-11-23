# Matthew Keitelman (mak2vr)
# Fernando Mata Cordero (fm5ew)

import pygame
import gamebox
import random

camera = gamebox.Camera(1000,800,True)
alien = gamebox.from_image(500, 15, "http://people.virginia.edu/~mak2vr/files/alien/alien.png")
alien.scale_by(1.6)
alien.yspeed = 0


platforms = [gamebox.from_color(100,400,"black",1000,30),
             gamebox.from_color(500,400,"black",1000,30),
]
length = 1000
prev_length = 1000
time_on = 50
prev_height = 400
prev_x = 500
height = 30

y = 1000


blue_hole_sheet = gamebox.load_sprite_sheet("http://people.virginia.edu/~mak2vr/files/alien/bluehole.png",1,5)
x = 500

blueholes = []

for bluehole in blueholes:
    bluehole.scale_by(4)

score = 0

speed = 10

def tick(keys):

    global x, score, y, prev_length, time_on, speed, prev_height, length, height


    if camera.x % 2000 == 0:
        speed += 4

    score += speed
    scoreboard = gamebox.from_text(camera.x+300,50,(str(score)),"Verdana",26,"black")

    camera.x += speed
    alien.x += speed

    time_on += speed



    if time_on:
        time_on = 0
        prev_length = length
        prev_height = height
        length = random.randint(300,600)
        height = random.randint(300,700)
        platforms.append(gamebox.from_color(camera.x,height,"black",length,30))



    for bluehole in blueholes:
        bluehole.image = blue_hole_sheet[x]

    # GRAVITY
    alien.yspeed += 1.5
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
        if alien.bottom_touches(platform):
            alien.move_to_stop_overlapping(platform)
        if platform.x < (camera.x-1000):
            platforms.remove(platform)
        if alien.touches(platform):
            if pygame.K_SPACE in keys:
                alien.yspeed -= 35
                keys.clear()


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

    game_over = gamebox.from_text(camera.x,400,"Game Over","Arial",40,"black",True)
    def end():
        gamebox.pause()
        camera.clear("skyblue")
        camera.draw(game_over)
        camera.display()
        print(alien.x)
        print(speed)


    if alien.y >= 800:
        end()

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

