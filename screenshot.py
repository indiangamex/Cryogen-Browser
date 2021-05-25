# importing random module
import random
import pyautogui
import ctypes
# defining the limit of random number to be and storing it into a variable
s = random.randint(1, 100)
# screenshot variable containing screenshot taken by pyautogui module
screenshot = pyautogui.screenshot()
# saving the screenshot and storing with random number in order to seperate other screenshots in the same device
screenshot.save("image{t}.png".format(t=s))
ctypes.windll.user32.MessageBoxW(0, "screenshot has been taken please search it by the name of image", "screenshot notification", 1)
