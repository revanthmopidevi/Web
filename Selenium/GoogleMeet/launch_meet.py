import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from msedge.selenium_tools import Edge, EdgeOptions
import time
import datetime

#options = Options()
#cap = options.to_capabilities()
#capabilities = options.to_capabilities()
#driver = webdriver.Edge(capabilities=capabilities)

options = EdgeOptions()
options.set_capability("dom.webnotifications.enabled", 1)
options.set_capability("permissions.default.microphone", 1)
options.set_capability("permissions.default.camera", 1)
options.use_chromium = True
driver = Edge("C:\\msedgedriver.exe", options = options)
#driver = webdriver.Edge("C:/MicrosoftWebDriver.exe")

class Meet:
    def __init__(self, meet, ID, password):
        self.meet = meet
        self.ID = ID
        self.password = password
        self.email = self.ID + "@hyderabad.bits-pilani.ac.in"
        self.googleLogin()
        self.launchMeet()

    def googleLogin(self):
        driver.get("https://accounts.google.com")
        driver.find_element_by_xpath("""//*[@id="identifierId"]""").send_keys(self.email)
        driver.find_element_by_xpath("""//*[@id="identifierNext"]/div/button/div[2]""").click()
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, """//*[@id="password"]/div[1]/div/div[1]/input"""))).send_keys(self.password)
        driver.find_element_by_xpath("""//*[@id="passwordNext"]/div/button/div[2]""").click()
        time.sleep(2)
        return

    def launchMeet(self):
        driver.get(self.meet)
        time.sleep(5)
        joinnow = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Join now')]")))
        webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("d").perform()
        webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("e").perform()
        driver.execute_script("arguments[0].click();", joinnow)
    

def countdown(seconds = 3000):
    while seconds >= 0:
        seconds -= 1
        time.sleep(1)
    return

if __name__ == "__main__":
    meet = "https://meet.google.com/" + sys.argv[2]
    ID = f20170280
    password = sys.argv[1]
    Meet(meet, ID, password)
    countdown()
    driver.close()
