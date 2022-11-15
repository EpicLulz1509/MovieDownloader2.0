from selenium import webdriver
import time
import pyautogui
from pynput.keyboard import Key, Controller
keyboard = Controller()
from qbittorrent import Client
import pyautogui

chromeOptions = webdriver.ChromeOptions()
path = input("Where do you want to download the file?")
prefs = {"download.default_directory": path}  # downloaded file location
chromeOptions.add_experimental_option("prefs", prefs)
chromeOptions.headless = False           #put true for headless mode, script wont work tho

driverPath = input("Enter the path of your chrome web driver.")
driver = webdriver.Chrome(executable_path=str(driverPath), options=chromeOptions)
chromeOptions = webdriver.ChromeOptions()
driver.set_window_size(1024, 600)
driver.maximize_window()

driver.get("https://www.1377x.to/popular-movies")

#put cursor on search box
time.sleep(5)
print(pyautogui.position())
#put output position on line 34 in main.py 

#put cursor on search button
time.sleep(5)
print(pyautogui.position())
#put output position on line 38 in main.py 
