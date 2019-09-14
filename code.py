import time
import PIL.ImageOps
from Actions import *
from numpy import *
from quickGrab import *
from MenuItems import *
def startGame():
    #for play
    setMousePos((323,208))
    leftClick()
    time.sleep(.1)

    #for continuing
    setMousePos((350,390))
    leftClick()
    time.sleep(.1)

    #for skipping the tutorial
    setMousePos((595,458))
    leftClick()
    time.sleep(.1)

    #for continuing
    setMousePos((427,390))
    leftClick()
    time.sleep(.1)

def clear_tables():
    setMousePos(Cord.plate1)
    leftClick()

    setMousePos(Cord.plate2)
    leftClick()

    setMousePos(Cord.plate3)
    leftClick()

    setMousePos(Cord.plate4)
    leftClick()

    setMousePos(Cord.plate5)
    leftClick()

    setMousePos(Cord.plate6)
    leftClick()
    time.sleep(.1)

def makeFood(food):
    if food == 'caliroll':
        print ('Making a caliroll')
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 1
        setMousePos(Cord.rice)
        leftClick()
        time.sleep(.05)
        setMousePos(Cord.nori)
        leftClick()
        time.sleep(.05)
        setMousePos(Cord.roe)
        leftClick()
        time.sleep(.1)
        foldMat()

    elif food == 'onigiri':
        print ('Making a onigiri')
        foodOnHand['rice'] -= 2
        foodOnHand['nori'] -= 1
        setMousePos(Cord.rice)
        leftClick()
        time.sleep(.05)
        setMousePos(Cord.rice)
        leftClick()
        time.sleep(.05)
        setMousePos(Cord.nori)
        leftClick()
        time.sleep(.1)
        foldMat()

    elif food == 'gunkan':
        print('Making a gunkan')
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 2
        setMousePos(Cord.rice)
        leftClick()
        time.sleep(.05)
        setMousePos(Cord.nori)
        leftClick()
        time.sleep(.05)
        setMousePos(Cord.roe)
        leftClick()
        time.sleep(.05)
        setMousePos(Cord.roe)
        leftClick()
        time.sleep(.1)
        foldMat()

    elif food == 'salmon':
        setMousePos(Cord.rice)
        leftClick()
        time.sleep(.05)
        setMousePos(Cord.nori)
        leftClick()
        time.sleep(.05)
        setMousePos(Cord.salmon)
        leftClick()
        time.sleep(.05)
        setMousePos(Cord.salmon)
        leftClick()
        time.sleep(.1)
        foldMat()

    elif food == 'shrimp':
        setMousePos(Cord.rice)
        leftClick()
        time.sleep(.05)
        setMousePos(Cord.nori)
        leftClick()
        time.sleep(.05)
        setMousePos(Cord.shrimp)
        leftClick()
        time.sleep(.05)
        setMousePos(Cord.shrimp)
        leftClick()
        time.sleep(.1)
        foldMat()

    elif food == 'shrimp':
        setMousePos(Cord.rice)
        leftClick()
        time.sleep(.05)
        setMousePos(Cord.nori)
        leftClick()
        time.sleep(.05)
        setMousePos(Cord.unagi)
        leftClick()
        time.sleep(.05)
        setMousePos(Cord.unagi)
        leftClick()
        time.sleep(.1)
        foldMat()

    elif food == 'combo':
        setMousePos(Cord.rice)
        leftClick()
        time.sleep(.05)
        setMousePos(Cord.rice)
        leftClick()
        time.sleep(.05)
        setMousePos(Cord.nori)
        leftClick()
        time.sleep(.05)
        setMousePos(Cord.roe)
        leftClick()
        time.sleep(.05)
        setMousePos(Cord.salmon)
        leftClick()
        time.sleep(.05)
        setMousePos(Cord.unagi)
        leftClick()
        time.sleep(.05)
        setMousePos(Cord.shrimp)
        leftClick()
        time.sleep(.1)
        foldMat()

    elif food == 'dragon':
        setMousePos(Cord.rice)
        leftClick()
        time.sleep(.05)
        setMousePos(Cord.rice)
        leftClick()
        time.sleep(.05)
        setMousePos(Cord.nori)
        leftClick()
        time.sleep(.05)
        setMousePos(Cord.roe)
        leftClick()
        time.sleep(.05)
        setMousePos(Cord.unagi)
        leftClick()
        time.sleep(.05)
        setMousePos(Cord.unagi)
        leftClick()
        time.sleep(.1)
        foldMat()

def checkFood():
    for key, value in foodOnHand.items():
        if key == 'nori' or key == 'rice' or key == 'roe':
            if value < 4:
                print (key+'is low and needs to be replenished')
                buyFood(key)

def buyFood(food):
    if food == 'rice':
        setMousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        setMousePos(Cord.p_rice)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        if s.getpixel(Cord.buy_rice) != (218, 255, 236):
            print (s.getpixel(Cord.buy_rice))
            setMousePos(Cord.buy_rice)
            time.sleep(.1)
            leftClick()
            setMousePos(Cord.p_delivery)
            time.sleep(.1)
            leftClick()
            foodOnHand['rice'] += 10
            time.sleep(2.5)
        else:
            print ('rice is NOT available')
            setMousePos(Cord.p_exit_phone_rice)
            leftClick()
            time.sleep(1.5)
            buyFood('rice')

    if food == 'nori':
        setMousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        setMousePos(Cord.p_topping)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        time.sleep(.1)
        if s.getpixel(Cord.p_nori) != (218, 255, 236):
            print ('nori is available')
            setMousePos(Cord.p_nori)
            time.sleep(.1)
            leftClick()
            setMousePos(Cord.p_delivery)
            time.sleep(.1)
            leftClick()
            foodOnHand['nori'] += 10
            time.sleep(2.5)
        else:
            print('nori is NOT available')
            setMousePos(Cord.p_exit_phone_toppings)
            leftClick()
            time.sleep(1)
            buyFood(food)

    if food == 'roe':
        setMousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        setMousePos(Cord.p_topping)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        time.sleep(.1)
        if s.getpixel(Cord.p_roe) != (218, 255, 236):
            print('roe is available')
            setMousePos(Cord.p_roe)
            time.sleep(.1)
            leftClick()
            setMousePos(Cord.p_delivery)
            time.sleep(.1)
            leftClick()
            foodOnHand['roe'] += 10


            time.sleep(2.5)
        else:
            print ('roe is NOT available')
            setMousePos(Cord.p_exit_phone_toppings)
            leftClick()
            time.sleep(1)
            buyFood(food)

def main():
    makeFood('caliroll')
    makeFood('caliroll')
    makeFood('onigiri')
    makeFood('onigiri')
    makeFood('onigiri')
    makeFood('onigiri')
    makeFood('caliroll')
    makeFood('caliroll')
    checkFood()

if __name__ == '__main__':
    main()
