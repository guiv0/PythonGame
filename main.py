import pygame
import pygame as pg

print("setup start")
pg.init();
screen = pg.display.set_mode(size=(600, 400))
print('setup end')

print('loop start')
while True:
    # Check for all events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()  # Close Window
            quit()  # End Pygame

