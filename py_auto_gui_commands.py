import pyautogui
print(pyautogui.size()) #gets screen size
print(pyautogui.position()) #get current coordinates of cursor 
pyautogui.moveTo(10, 10, duration=1.5) #uses x nad y coordinates, duration makes it slower, this is 1.5 seconds
pyautogui.moveRel(200,0, duration=2) #this moves the mouse to the right by 200 pixels
pyautogui.moveRel(0,-100, duration=1) #this moves the mouse up by 100 px
print(pyautogui.position()) #gets the current mouse position
#pyautogui.click(x,y) clicks on coordinates on the screen
#pyautogui.doubleClick(x,y)
#pyautogui.rightClick(x,y)
#pyautogui.middleClick(x,y)
#pyautogui.click() with no arguments it clicks on current mouse position
#if you lose control of the mouse just slam top left at (0,0) and it will stop executing


#to get coordinates on screen while moving the mouse its best to use the commandline
#import pyautogui
#pyautogui.displayMousePosition()

# ********** keyboard commands **********
#pyautogui.typewrite('Hello World!', interval=0.2) #interval between each charachter
#pyautogui.typewrite(['a', 'b', 'left', 'left'], interval = 0.4) #this is how you call shift ctrl and others
#pyautogui.KEYBOARD_KEYS #returns a list of keys you can use
#pyautogui.press('f1') #if you want a single key press
#pyautogui.hotkey('ctrl', 'o') #presses a series of keys









