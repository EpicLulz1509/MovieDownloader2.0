from selenium import webdriver
import time
import pyautogui
from pynput.keyboard import Key, Controller
keyboard = Controller()
from qbittorrent import Client

chromeOptions = webdriver.ChromeOptions()
path = "Downloads/Movies"
prefs = {"download.default_directory": path}  # downloaded file location
chromeOptions.add_experimental_option("prefs", prefs)
chromeOptions.headless = False           #put true for headless mode, script wont work tho

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe", options=chromeOptions)
chromeOptions = webdriver.ChromeOptions()
driver.set_window_size(1024, 600)
driver.maximize_window()

qb = Client("http://127.0.0.1:8080/")
qb.login("admin", "adminadmin")

driver.get("https://www.imdb.com/list/ls091520106/")
movie_names_arr = []
movie_name = ""


for i in range(1, 5) :
    movie_name = driver.find_element_by_xpath(f"/html/body/div[2]/div/div[2]/div[3]/div[1]/div/div[4]/div[3]/div[{i}]/div[2]/h3/a").text
    movie_names_arr.append(movie_name)

driver.get("https://www.1377x.to/popular-movies")

for i in range(1, 3):
    pyautogui.click(x=1251, y=207)
    # change it based on position of the searchbox in your browser
    time.sleep(2)
    keyboard.type(movie_names_arr[i-1])
    pyautogui.click(x=1500, y=207)
    # change it based on position of the search button in your browser
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/main/div/div/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/a[2]").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/main/div/div/div/div[2]/div[1]/ul[1]/li[7]/a").click()
    time.sleep(1)
    link = driver.find_element_by_xpath("/html/body/main/div/div/div/div[2]/div[1]/ul[1]/li[7]/ul/li[4]/a").get_attribute('href')
    qb.download_from_link(link)
    time.sleep(5)



    

driver.get("https://www.imdb.com/list/ls091520106/")