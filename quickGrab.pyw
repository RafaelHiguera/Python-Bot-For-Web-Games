import PIL.ImageGrab
import os
import time
import MenuItems

topGameCornerX = 463
topGameCornerY = 254

def screenGrab():
    box = (topGameCornerX,topGameCornerY,topGameCornerX+641,topGameCornerY+481)
    im = PIL.ImageGrab.grab(box)
    ##im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im

def main():
    screenGrab()

if __name__ == '__main__':
    main()
