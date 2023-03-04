import pygame
from pygamekit import Window
from pygamekit import optimization
from pygamekit import Label

win = Window()

# win.open()

text = Label(x=50, y=50)

#@optimization.memoize

@win.schedule_every('1s')
def function_who_print():
    # print('Tick !')
    win.clear()
    text.draw(win)
    win.update()

win.schedule(0, win.handle_events)

win.run()
