from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
import time
from selenium.common.exceptions import NoSuchElementException

if __name__ == "__main__":
        while True:
                # path to chrome driver
                # make sure the driver version matches google chrome's version
                driver = webdriver.Chrome('C:\\chromedriver.exe')
                # ERP login page 
                driver.get('https://sis.erp.bits-pilani.ac.in/psp/sisprd/?cmd=login')
                driver.find_element_by_xpath("""//*[@id="userid"]""").send_keys("41120170280")
                driver.find_element_by_xpath("""//*[@id="pwd"]""").send_keys("5NJU*5iL")
                driver.find_element_by_xpath("""/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[1]/td/table[2]/tbody/tr[4]/td[3]/input""").click()
                # ERP swap page
                driver.get("")
                driver.switch_to.frame(driver.find_element_by_xpath("""//*[@id="ptifrmtgtframe"]"""))
                try:
                        elem=element1 = driver.find_element_by_name("DERIVED_REGFRM1_DESCR50$37$")
                        if elem.is_displayed():
                                drp1 = Select(element1)
                                drp1.select_by_visible_text("HSS F244: CRIME AND NEW MEDIA")
                                driver.find_element_by_xpath("""//*[@id="DERIVED_REGFRM1_SSR_PB_SRCH$41$"]""").click()
                                time.sleep(1)
                                driver.find_element_by_name("CLASS_SRCH_WRK2_SUBJECT$64$")
                                # select course discipline (CS, EEE, ECE, INSTR, FIN, ECON etc.) by changing option[num]
                                driver.find_element_by_xpath("""//*[@id="CLASS_SRCH_WRK2_SUBJECT$64$"]/option[6]""").click()
                                time.sleep(1)
                                # course code
                                driver.find_element_by_xpath("""//*[@id="CLASS_SRCH_WRK2_CATALOG_NBR$72$"]""").send_keys("F372")
                                driver.find_element_by_xpath("""//*[@id="CLASS_SRCH_WRK2_SSR_PB_CLASS_SRCH"]""").click()
                                time.sleep(1)
                                try:
                                        elem = driver.find_element_by_xpath("""//*[@id="CLASS_SRCH_WRK2_SSR_PB_SELECT$0"]""")
                                        if elem.is_displayed():
                                                # click the element if present
                                                elem.click()
                                                time.sleep(1)
                                                driver.find_element_by_xpath("""//*[@id="DERIVED_CLS_DTL_NEXT_PB$75$"]""").click()
                                                time.sleep(1)
                                                driver.find_element_by_xpath("""//*[@id="DERIVED_REGFRM1_SSR_PB_SUBMIT"]""").click()
                                                print("\nSWAP SUCCESFUL.\n")
                                                break
                                except NoSuchElementException:
                                    driver.close()
                except NoSuchElementException:
                        driver.close()


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# elems = driver.find_element_by_xpath("""//*[@id="CLASS_SRCH_WRK2_SSR_PB_SELECT$0"]""")

# if len(elems) > 0 and elems[0].is_displayed():
#     elems[0].click()
#     print("SWAP SUCCESFUL.")
# else: 
#     print ("NO LINK FOUND")
# driver.find_element_by_xpath("""//*[@id="CLASS_SRCH_WRK2_SSR_PB_SELECT$0"]""").click()

# time.sleep(0.5)
# driver.find_element_by_xpath("""//*[@id="DERIVED_CLS_DTL_NEXT_PB$75$"]""").click()
# time.sleep(0.5)
# driver.find_element_by_xpath("""//*[@id="DERIVED_REGFRM1_SSR_PB_SUBMIT"]""").click()
