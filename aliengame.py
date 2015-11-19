# Matthew Keitelman (mak2vr)
# Fernando Mata Cordero (fm5ew)

import pygame
import gamebox

camera = gamebox.Camera(1000,800)
character = gamebox.from_color(150, 10, "red", 30, 60)
character.yspeed = 0

levels = gamebox.from_image(400,400,"levels.png")
levels.scale_by(1.5)

platforms = [
    # gamebox.from_color(-100, 600, "black", 3000, 100),
    levels
    # ground1
]

def tick(keys):

    # GRAVITY
    character.yspeed += 1
    character.y = character.y + character.yspeed

    for platform in platforms:
        if character.touches(platform):
            character.move_to_stop_overlapping(platform)

    if pygame.K_RIGHT in keys:
        character.x += 5
    if pygame.K_LEFT in keys:
        character.x -= 5
    camera.clear("cyan")
    camera.draw(character)
    for platform in platforms:
        camera.draw(platform)
    camera.display()
ticks_per_second = 30

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)
