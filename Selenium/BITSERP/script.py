from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.common.exceptions import NoSuchElementException
import time

PATH = "C:\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

def main():        
        # erp links
        erp_login_link = "https://sis.erp.bits-pilani.ac.in/psp/sisprd/?cmd=login"
        erp_login_error = "https://sis.erp.bits-pilani.ac.in/psp/sisprd/?&cmd=login&errorCode=105&languageCd=ENG"
        erp_landing_page = "https://sis.erp.bits-pilani.ac.in/psp/sisprd/EMPLOYEE/HRMS/h/?tab=DEFAULT"
        erp_swap_link = ""

        # "41120170280", "ZOMN^6zQ"
        print("THIS APPLICATION CAN REGISTER COURSES THAT HAVE ONLY LECTURE SECTIONS\n")
        # erp credentials
        userID , password = getCredentials()
        # courses to drop and pick
        toDrop = getDropClass()
        toPick = getPickClass()
        print("LOGGING IN...")
        if login(erp_login_link, erp_login_error, userID, password):
                        print("SUCCESFULLY LOGGED IN")
        else:
                print("YOUR USER ID AND/OR PASSWORD ARE INVALID OR ERP IS DOWN")
                driver.quit()
        while True:
                if swap(erp_swap_link,toDrop, toPick):
                        print("COURSE SUCCESFULLY SWAPPED")
                        driver.quit()
                        break
                else:
                        print("RETRYING...")
def getCredentials():
        userID = input("ENTER USER ID: ")
        password = input("ENTER PASSWORD: ")
        return userID, password

def getPickClass():
        DeptNums = {}
        # EXAMPLE: BITS, CS, ECON, GS, HSS
        classDept = input("ENTER DEPARTMENT CODE: ")
        # EXAMPLE: F211
        classCode = input("ENTER LAST FOUR DIGITS OF THE CLASS CODE: ")
        return {"option": classDept, "code": classCode}

def getDropClass():
        classCode = input("ENTER COURSE CODE: ").strip().upper()
        className = input("ENTER COURSE NAME: ").strip().upper()
        toDrop = classCode + ": " + className
        print(f"COURSE TO DROP: '{toDrop}' ")
        return toDrop

def login(erp_login_link, erp_login_error, userID, password):
        driver.get(erp_login_link)
        driver.find_element_by_id('userid').send_keys(userID)
        driver.find_element_by_id('pwd').send_keys(password)
        driver.find_element_by_class_name('psloginbutton').click()
        time.sleep(1)
        if driver.current_url == erp_login_error:
                return False
        else:
                return True

def swap(erp_swap_link, toDrop, toPick):
        driver.get(erp_swap_link)
        driver.switch_to.frame(driver.find_element_by_xpath("""//*[@id="ptifrmtgtframe"]"""))
        try:
                elem=element1 = driver.find_element_by_name("DERIVED_REGFRM1_DESCR50$37$")
                if elem.is_displayed():
                        drp1 = Select(element1)
                        drp1.select_by_visible_text(toDrop)
                        driver.find_element_by_xpath("""//*[@id="DERIVED_REGFRM1_SSR_PB_SRCH$41$"]""").click()
                        time.sleep(1)
                        driver.find_element_by_name("CLASS_SRCH_WRK2_SUBJECT$64$")
                        # TODO
                        driver.find_element_by_xpath("""//*[@id="CLASS_SRCH_WRK2_SUBJECT$64$"]/option[6]""").click()
                        time.sleep(1)
                        driver.find_element_by_xpath("""//*[@id="CLASS_SRCH_WRK2_CATALOG_NBR$72$"]""").send_keys(toPick['code'])
                        driver.find_element_by_xpath("""//*[@id="CLASS_SRCH_WRK2_SSR_PB_CLASS_SRCH"]""").click()
                        time.sleep(1)
                        try:
                                elem = driver.find_element_by_xpath("""//*[@id="CLASS_SRCH_WRK2_SSR_PB_SELECT$0"]""")
                                if elem.is_displayed():
                                        elem.click()
                                        time.sleep(1)
                                        driver.find_element_by_xpath("""//*[@id="DERIVED_CLS_DTL_NEXT_PB$75$"]""").click()
                                        time.sleep(1)
                                        driver.find_element_by_xpath("""//*[@id="DERIVED_REGFRM1_SSR_PB_SUBMIT"]""").click()
                                        return True
                        except NoSuchElementException:
                                driver.close()
                                return False
        except NoSuchElementException:
                driver.close()
                return False

if __name__ == "__main__":
        main()