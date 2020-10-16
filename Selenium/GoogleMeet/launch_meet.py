import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
"profile.default_content_setting_values.media_stream_mic": 1, 
"profile.default_content_setting_values.media_stream_camera": 1,
"profile.default_content_setting_values.geolocation": 1, 
"profile.default_content_setting_values.notifications": 1 
})

try:
    driver = webdriver.Chrome("C:\\chromedriver.exe", options=opt)
except WebDriverException:
    print("|| WEB DRIVER NOT FOUND, KINDLY REFER TO README ||")
    time.sleep(5)
    exit()

class Meet:
    def __init__(self):
        self.meet = "https::/meet.google.com/" + sys.argv[3] 
        self.ID = sys.argv[1]
        self.password = sys.argv[2]
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
    

if __name__ == "__main__":
    Meet()
