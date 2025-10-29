import pyautogui
import time
import pandas as pd
import keyboard

df = pd.read_excel("PureData.xlsx")
count = 612
loop_var = 1
loop_var2 = 1
loop_var3 = 1
loop_var4 = 1
downloadpdf = 1
files = 1
errorval = 0

def cellcount():
    print("You're on cell number", count + 3)

keyboard.add_hotkey('g', cellcount)


while count < 697 :
    time.sleep(2)
    pyautogui.click(584, 127)
    pyautogui.typewrite("Google scholar", interval=0.01)
    pyautogui.press("enter")
    time.sleep(1)
    while loop_var == 1:
        try:
            image_test = pyautogui.locateOnScreen("Scholar5.png",confidence=.4)
            time.sleep(1)
            pyautogui.click(369, 607)
            loop_var += 1

        except pyautogui.ImageNotFoundException:
            print("not found 1")
            time.sleep(1)
    time.sleep(1)
    pyautogui.click(1150, 599)
    value = df.iloc[count, 0]
    pyautogui.typewrite(value, interval=.01)
    pyautogui.press("enter")
    while loop_var2 == 1:
        try:
            image_test = pyautogui.locateOnScreen("Scholar4.png", confidence=.4)
            time.sleep(1)
            pyautogui.click(782, 452)
            loop_var2 += 1

        except pyautogui.ImageNotFoundException:
            print("not found 2")
            time.sleep(1)
            
    time.sleep(1)
    while loop_var3 == 1:
        if errorval < 5:
            try:
                image_test = pyautogui.locateOnScreen("ScienceDirect.png", confidence= .7)
                time.sleep(2)
                pyautogui.click(811, 449)
                loop_var3 += 1
                time.sleep(1)
                while downloadpdf == 1:
                    try:
                        image_test = pyautogui.locateOnScreen("downloadpdf.png", confidence=.7)
                        time.sleep(2)
                        pyautogui.click(2355, 244)
                        downloadpdf += 1

                    except pyautogui.ImageNotFoundException:
                        print("not found 3")
                        time.sleep(1)
                time.sleep(1)
                while files == 1:
                    try:
                        image_test = pyautogui.locateOnScreen("files.png", confidence=.7)
                        time.sleep(2)
                        pyautogui.click(1781, 1134)
                        files += 1

                    except pyautogui.ImageNotFoundException:
                        print("not found 4")
                        time.sleep(1)
                time.sleep(1)
                pyautogui.keyDown("ctrl")
                pyautogui.press("w")
                pyautogui.press("w")
                time.sleep(1)
                pyautogui.press("t")
                pyautogui.keyUp("ctrl")
                errorval = 0
                loop_var = 1
                loop_var2 = 1
                loop_var4 = 1
                downloadpdf = 1
                files = 1

            except pyautogui.ImageNotFoundException:
                time.sleep(1)
                print("not found 5")
                errorval += 1
        else:
            print("couldn't download cell", count + 3)
            pyautogui.keyDown("ctrl")
            pyautogui.press("t")
            pyautogui.keyUp("ctrl")
            errorval = 0
            loop_var = 1
            loop_var2 = 1
            loop_var4 = 1
            downloadpdf = 1
            files = 1
            loop_var3 += 1
    count += 1
    loop_var3 = 1

