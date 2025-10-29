import pyautogui
import time
import pandas as pd


count = 1
loop_var = 1
loop_var2 = 1
loop_var3 = 1
loop_var4 = 1
downloadpdf = 1
files = 1
errorval = 0

while count < 100 :
    time.sleep(2)
    pyautogui.click(584, 127)
    pyautogui.typewrite("Google scholar", interval=0.01)
    pyautogui.press("enter")
    time.sleep(1)
    while loop_var == 1:
        try:
            image_test = pyautogui.locateOnScreen("Scholar3.png",confidence=.8)
            time.sleep(1)
            pyautogui.click(369, 607)
            loop_var += 1

        except pyautogui.ImageNotFoundException:
            print("not found 1")
            time.sleep(1)
    time.sleep(1)
    pyautogui.click(1150, 599)
    pyautogui.typewrite("https://www.sciencedirect.com/science/article/pii/S2376060524001354", interval=.01)
    pyautogui.press("enter")
    while loop_var2 == 1:
        try:
            image_test = pyautogui.locateOnScreen("Scholar4.png", confidence=.8)
            time.sleep(1)
            pyautogui.click(761, 455)
            loop_var2 += 1

        except pyautogui.ImageNotFoundException:
            print("not found 2")
            time.sleep(1)
    time.sleep(1)
    while loop_var3 == 1:
        if errorval < 5:
            try:
                image_test = pyautogui.locateOnScreen("ScienceDirect.png", confidence= .8)
                time.sleep(2)
                pyautogui.click(809, 344)
                loop_var3 += 1
                time.sleep(1)
                while downloadpdf == 1:
                    try:
                        image_test = pyautogui.locateOnScreen("downloadpdf.png", confidence=.8)
                        time.sleep(2)
                        pyautogui.click(2355, 244)
                        downloadpdf += 1

                    except pyautogui.ImageNotFoundException:
                        print("not found 4")
                        time.sleep(1)
                time.sleep(1)
                while files == 1:
                    try:
                        image_test = pyautogui.locateOnScreen("files.png", confidence=.8)
                        time.sleep(2)
                        pyautogui.click(1781, 1134)
                        files += 1

                    except pyautogui.ImageNotFoundException:
                        print("not found 5")
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
                print("not found 3")
                time.sleep(1)
                errorval += 1
        else:
            print("couldn't download cell", count + 1)
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

