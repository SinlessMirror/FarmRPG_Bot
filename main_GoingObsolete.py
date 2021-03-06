import cv2 as cv
import numpy as np
import os
import pyautogui
from time import time 
from time import sleep 
from windowcapture import WindowCapture
from vision import Vision
import pyautogui
# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# initialize the WindowCapture class
wincap = WindowCapture()
# initialize the Vision class
nextButton = Vision('next_button.jpg')
notYet = Vision('not_yet.jpg')
plantSeedButton = Vision('plantButton.jpg')
harvestableOnion = Vision('harvestableOnion.jpg')
harvestBarGreen = Vision('harvestBarGreen.jpg')
tooSoon = Vision('tooSoon.jpg')
pepperReady = Vision('pepperReady.jpg')
radishReady = Vision('radishReady.jpg')
carrotReady = Vision('carrotReady.jpg')
cancelButton = Vision('cancelButton.jpg')
outOfSeeds = Vision('outOfSeeds.jpg')
refreshWindowTimer = time()
'''
# https://www.crazygames.com/game/guns-and-bottle
wincap = WindowCapture()
vision_gunsnbottle = Vision('gunsnbottle.jpg')
'''

announcmentActive = None
selectedCrop = None

loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()
    #show screenshot
    #cv.imshow('screenshot', screenshot)

    # display the processed image
    #points = nextButton.find(screenshot, 0.95, 'rectangles')
    plantSeed = plantSeedButton.find(screenshot, 0.9, 'points')
    if (plantSeed.any()):
        print(plantSeed)
        print("Detected plant seed button")
        #Try to use the plantSeed array coordinates to click on the plantSeed
        rebuy = 0
        for plantSeeds in plantSeed:
            rebuy = rebuy + 1
            sleep(.3)
            pyautogui.moveTo(plantSeeds[0]+40, plantSeeds[1]+40)
            pyautogui.click()
            print('Clicked at', plantSeeds[0]+40, plantSeeds[1]+40)
        print("Done planting 4x4")
        print("Rebuying seeds...")
        pyautogui.click(116, 180) # CLICK HOME
        sleep(1.3)
        pyautogui.click(535, 430) # CLICK GO TO TOWN
        sleep(1.3)
        pyautogui.click(508, 318) # 
        sleep(1.3)
        i = 24
        while i > rebuy:
            pyautogui.click(340, 516) # DOWN ARROW -> CARROT SET [PEPPER: 340, 413] [CARROT: 340, 516]
            i = i - 1
            sleep(.35)
        pyautogui.click(1478, 498) # CLICK BUY -> CARROT SET [PEPPER: 1478, 382] [CARROT: 1478, 498]
        sleep(1.3)
        pyautogui.click(960, 965) # CLICK OK
        sleep(1.3)
        pyautogui.click(966, 564) # CLICK GO TO FARM
        # longer sleep as 1 second would catch the screen half way swapped and mis-click then rebuy in error
        sleep(3)

    #Get updated screenshot as searching for plantSeed may have taken a bit of time
    screenshot = wincap.get_screenshot()
    harvest = carrotReady.find(screenshot, 0.91, 'points')
    if (harvest.any()):
        print("harvastable found, harvesting!")
        print(harvest)
        rebuy = 0
        for harvests in harvest:
            rebuy = rebuy + 1
            sleep(.25)
            pyautogui.moveTo(harvests[0]+40, harvests[1]+50)
            pyautogui.click()
            print('Clicked at', harvests[0]+40, harvests[1]+50)
        print("Done harvesting 4x4, replanting...")
        for harvests in harvest:
            sleep(.25)
            pyautogui.moveTo(harvests[0]+40, harvests[1]+50)
            pyautogui.click()
            print('Clicked at', harvests[0]+40, harvests[1]+50)
        print("Done replanting 4x4")
        #sell all the crops and rebuy more
        sleep(1.3)
        pyautogui.click(116, 180) # CLICK HOME
        sleep(1.3)
        pyautogui.click(535, 430) # CLICK GO TO TOWN
        sleep(1.3)
        pyautogui.click(508, 391) # CLICK MARKET
        sleep(1.3)
        pyautogui.click(743, 319) # CLICK SELL ALL CROPS
        sleep(1.3)
        pyautogui.click(960, 965)
        sleep(1.3)
        pyautogui.click(958, 607)
        sleep(2)
        pyautogui.click(116, 180)
        sleep(1.3)
        pyautogui.click(535, 430)
        sleep(1.3)
        pyautogui.click(508, 318)
        sleep(1.3)
        i = 24
        while i > rebuy:
            pyautogui.click(340, 516) # DOWN ARROW -> CARROT SET [PEPPER: 340, 413] [CARROT: 340, 516]
            i = i - 1
            sleep(.35)
        pyautogui.click(1478, 498) # CLICK BUY -> CARROT SET [PEPPER: 1478, 382] [CARROT: 1478, 498]
        sleep(1.3)
        pyautogui.click(960, 965) # CLICK OK
        sleep(1.3)
        pyautogui.click(966, 564) # CLICK GO TO FARM
        # longer sleep as 1 second would catch the screen half way swapped and mis-click then rebuy in error
        sleep(3)

        
    #Click to remove popup window that may appear
    clickPopup = tooSoon.find(screenshot, 0.9, 'points')
    if(clickPopup.any()):
        pyautogui.click(966, 596)
        print("Clicked at 966, 596 to remove popup window if present")
    #Click to remove cancel window that may appear and cause a loop
    clickCancel = cancelButton.find(screenshot, 0.8, 'points')
    if(clickCancel.any()):
        pyautogui.click(960, 1009)
        print("Clicked at 960, 1009 to remove cancel window")
    #check to see if out of seeds, rebuy if so
    outOfSeeds = Vision('outOfSeeds.jpg')
    if(outOfSeeds.find(screenshot, 0.9, 'points').any()):
        pyautogui.click(116, 180) # CLICK HOME
        sleep(1.3)
        pyautogui.click(535, 430) # CLICK GO TO TOWN
        sleep(1.3)
        pyautogui.click(508, 318) # CLICK MARKET 
        sleep(1.3)
        pyautogui.click(1478, 498) # CLICK BUY -> CARROT SET [PEPPER: 1478, 382] [CARROT: 1478, 498]
        sleep(1.3)
        pyautogui.click(960, 965) # CLICK OK
        sleep(1.3)
        pyautogui.click(966, 564) # CLICK GO TO FARM
        # longer sleep as 1 second would catch the screen half way swapped and mis-click then rebuy in error
        sleep(3)

    #refreshWindowTimer 
    if (time() - refreshWindowTimer > 240):
        sleep(3.5)
        pyautogui.click(1010, 80)
        print("Clicked at 1010, 80 on bookmark button")
        sleep(3.5)
        refreshWindowTimer = time()
        pyautogui.click(116, 185)
        print("Clicked at 116, 185 on home button to refresh")
        sleep(3.5)
        pyautogui.click(465, 253)
        print("Clicked at 465, 253 to return to farm")
        sleep(3.5)


    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')
