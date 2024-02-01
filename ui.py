import pygame_widgets
import pygame
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

from dmx import DMX

dmx = DMX()

pygame.init()
win = pygame.display.set_mode((1100, 800))

#slider_base = Slider(win, 100, 100, 800, 40, initial=255, min=0, max=255, step=1)
slider_r = Slider(win, 100, 200, 800, 40, initial=0, min=0, max=255, step=1)
slider_g = Slider(win, 100, 300, 800, 40, initial=0, min=0, max=255, step=1)
slider_b = Slider(win, 100, 400, 800, 40, initial=0, min=0, max=255, step=1)
slider_w = Slider(win, 100, 500, 800, 40, initial=0, min=0, max=255, step=1)
#slider_effect = Slider(win, 100, 600, 800, 40, initial=0, min=0, max=255, step=1)

run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()

    win.fill((255, 255, 255))

    #dmx.set_value("base", slider_base.getValue())
    dmx.set_value("r", slider_r.getValue())
    dmx.set_value("g", slider_g.getValue())
    dmx.set_value("b", slider_b.getValue())
    dmx.set_value("w", slider_w.getValue())
    #dmx.set_value("effect", slider_effect.getValue())

    pygame_widgets.update(events)
    pygame.display.update()

dmx.close()