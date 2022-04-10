import webbrowser
import pyautogui
import time
import pywhatkit
from datetime import datetime,timedelta
import clipboard


# open whatsapp web
webbrowser.open('https://web.whatsapp.com/')

time.sleep(15)
# print(pyautogui.position())

# search group
pyautogui.click(457,266)
pyautogui.typewrite("texting")

time.sleep(1)

# select group
pyautogui.click(458,371)

time.sleep(1)

# go to group settings
pyautogui.click(1116,123)

time.sleep(1)

# scroll down
pyautogui.click(1591,471)
pyautogui.hscroll(-1000)

time.sleep(1)

# click on invite link btn
pyautogui.click(1414,767)

time.sleep(1)

#copy link
pyautogui.click(1449,425)

time.sleep(1)


# get time after 1min
now = datetime.now()
now_plus_1 = now + timedelta(minutes = 1)
now_plusH = now_plus_1.strftime("%H")
now_plusM = now_plus_1.strftime("%M")

# get invite link from clipboard
msg = clipboard.paste()

# send msg
pywhatkit.sendwhatmsg("+94775667922", msg, now_plusH, now_plusM)