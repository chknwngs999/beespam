import time
import pyautogui

# this program types stuff

pyautogui.FAILSAFE = True

#sendorno = bool(input("True or False: Do you want to send or go to a new line?"))

time.sleep(2)
print("Starting in 3 seconds...")
time.sleep(1)
print("Starting in 2 seconds...")
time.sleep(1)
print("Starting in 1 second...")
time.sleep(1)

f = open("script.txt", "r")
# try:
for line in f.readlines():
    pyautogui.typewrite(line)
"""if sendorno:
  pyautogui.keyDown("shift")
  pyautogui.keyDown("enter")
  pyautogui.keyUp("enter")
  pyautogui.keyUp("shift")
else:"""
pyautogui.press("enter")
"""except:
  print("Looks like we've been failsafed!")  """

f.close()
print("hehe done.")

# https://pyautogui.readthedocs.io/en/latest/quickstart.html

"""
while True:
  pyautogui.typewrite("Krista")
  pyautogui.press("enter")
"""
