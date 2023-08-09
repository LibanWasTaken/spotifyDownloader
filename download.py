import pyautogui

# https://spotifydown.com/
# 50% zoom out

def trackmouse():
    print('Press Ctrl-C to quit.')
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n') 

# trackmouse()

def download(scrollCount):
    pyautogui.click(x=1049, y=162) # search bar
    pyautogui.typewrite(playlistLink) # paste link
    pyautogui.click(x=950, y=183) # enter
    pyautogui.sleep(3)

    if scrollCount > 0:
         for i in range(scrollCount):
            pyautogui.press('pagedown')
            pyautogui.sleep(1)
    pyautogui.moveTo(x=1125, y=yPosition, duration=0.2)
    pyautogui.click() # download button
    pyautogui.sleep(1)
    if scrollCount > 0:
        pyautogui.press('home')
    pyautogui.sleep(30)
    pyautogui.click(x=842, y=303) # download track
    pyautogui.sleep(3)
    # Name
    # pyautogui.press('left')
    # pyautogui.sleep(1)
    # pyautogui.hotkey('ctrl', 'shift', 'left')
    # pyautogui.sleep(1)
    # pyautogui.hotkey('ctrl', 'shift', 'left')
    # pyautogui.sleep(1)
    # pyautogui.press('backspace')

    pyautogui.click(x=796, y=506) # save
    pyautogui.sleep(1)
    pyautogui.click(x=957, y=493) # close
    pyautogui.sleep(1)
    pyautogui.click(x=1088, y=309) # another song
    pyautogui.sleep(2)


count = 0
scroll = 0

playlistLink = "https://open.spotify.com/playlist/06BMp2O4VZ3QgTw6V294oc"
totalCount = 32
yPosition = 306 #starting track y position

pyautogui.click(x=1000, y=1062) # open chrome
pyautogui.sleep(1)

while count < totalCount:
    # correction (just the download fucntion:
    # if count > 25:
    download(scroll)
    yPosition += 32
    if yPosition > 1030:
        # if scroll == 1:
        #     # 2 scroll
        #     yPosition = 200

        # 1 scroll
        yPosition = 200
        scroll += 1

    print(count)
    count += 1