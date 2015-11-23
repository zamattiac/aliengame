# Matthew Keitelman (mak2vr)
# Fernando Mata Cordero (fm5ew)

import pygame
import gamebox
import random

camera = gamebox.Camera(1000,800,True)
alien = gamebox.from_image(300, 15, "http://people.virginia.edu/~mak2vr/files/alien/alien.png")
alien.scale_by(1.3)
alien.yspeed = 0


platforms = [
    gamebox.from_color(500,400,"black",1000,30),
    gamebox.from_color(1500,600,"black",500,30),
]

radius = 250
platform_x = 1500
platform_length = 500
platform_end = 1750
prev_length = 0
prev_end = 0
prev_x = 0
prev_radius = 0
platform_end

time_on = 300

y=0

blue_hole_sheet = gamebox.load_sprite_sheet("http://people.virginia.edu/~mak2vr/files/alien/bluehole.png",1,5)
x = 1500

blueholes = []

for bluehole in blueholes:
    bluehole.scale_by(4)

score = 0

speed = 10

def tick(keys):



    global x, score, y, platform_x, time_on, speed, platform_length, platform_end, prev_length, prev_end, prev_x, radius, prev_radius

    if y > 3:
        y =0
    y+=1

    if camera.x % 2000 == 0:
        speed += 3

    score = int(camera.x)
    scoreboard = gamebox.from_text(camera.x+300,50,(str(score)),"Verdana",26,"black")

    camera.x += speed
    alien.x += speed




    if alien.x >= (platform_x - platform_length/2) and alien.x <= (platform_x - platform_length/2):
        time_on += speed
    elif alien.x >= platform_x - platform_length/2:
        time_on = 0


    if len(platforms) < 10:
        prev_length = int(platform_length)
        prev_x = int(platform_x)
        prev_end = int(platform_end)
        prev_radius = radius

        platform_length = int(random.randint(300,600))
        radius = int(platform_length/2)
        platform_x = prev_end + radius + random.randint(25,200)

        platform_end = platform_x + radius


        height = random.randint(300,700)
        platforms.append(gamebox.from_color(platform_x,height,"black",2*radius,30))


    if len(blueholes) < 4:
        bluehole_x = random.randint(camera.x,camera.x+500)
        bluehole_y = random.randint(100,700)

        blueholes.append(gamebox.from_image(bluehole_x,bluehole_y,blue_hole_sheet[y]))








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
                alien.yspeed -= 30


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

    for bluehole in blueholes:
        bluehole.image = blue_hole_sheet[y]
        if bluehole.x < (camera.x-1000):
            blueholes.remove(bluehole)
        if alien.touches(bluehole):
            end()


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

