from selenium import webdriver
import time
from datetime import datetime

driver = webdriver.Chrome(".\\chromedriver.exe")
driver.maximize_window()
file = open(".\\channel_name.txt", "r")
log = open(".\\log.txt", "w")
channel_name = file.readline()[0:].lower()
driver.get("https://www.twitch.tv/"+channel_name)
try:
    try:
        but_play = driver.find_element_by_xpath('//*[@class="player-button qa-pause-play-button"]').click()
    except Exception:
        but_play = driver.find_element_by_xpath('//*[@class="player-content-button js-player-mature-accept js-mature-accept-label"]').click()
    time.sleep(10)
    need_tab = driver.find_element_by_xpath('//*[@class="tw-font-size-5" and contains(text(),"События")]').click()
    time.sleep(3)
    need_tab = driver.find_element_by_xpath('//*[@class="tw-font-size-5" and contains(text(),"Видеоматериалы")]').click()
    time.sleep(3)
    driver.close()
    log.write("Все действия сценария выполнены." + str(datetime.now()))
except Exception:
    log.write("Такого канала нет на " + str(datetime.now()))
    driver.close()
