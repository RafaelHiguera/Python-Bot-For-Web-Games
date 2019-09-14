import win32api,win32con,time

topGameCornerX = 463
topGameCornerY = 254
mat = (185,363)

def foldMat():
    setMousePos(mat)
    leftClick()
    time.sleep(1.5)

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print ('left click')

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print ('left Down')

def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print ('left release.')

def setMousePos(coordinates):
    win32api.SetCursorPos((topGameCornerX+coordinates[0],topGameCornerY+coordinates[1]))

def get_coordinates():
    x,y = win32api.GetCursorPos()
    x -= topGameCornerX
    y -= topGameCornerY
    print (x,y)
