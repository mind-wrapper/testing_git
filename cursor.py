from pynput import mouse
import random as rd


m=mouse.Controller()
def on_click(x, y, button, pressed):
    if(pressed):
        x=rd.randint(0,900)
        y=rd.randint(0,1200)
        m.position=(x,y)


with mouse.Listener(on_click=on_click) as listener:
    listener.join()
