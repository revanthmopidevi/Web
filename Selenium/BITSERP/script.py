from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
import time

class erp:
        def __init__(self):
                try:
                        self.driver = webdriver.Chrome("C:\\chromedriver.exe")
                except WebDriverException:
                        print("|| WEB DRIVER NOT FOUND, KINDLY REFER TO README ||")
                        time.sleep(10)
                        exit()
                self.erp_login_link = "https://sis.erp.bits-pilani.ac.in/psp/sisprd/?cmd=login"
                self.erp_login_error = "https://sis.erp.bits-pilani.ac.in/psp/sisprd/?&cmd=login&errorCode=105&languageCd=ENG"
                self.erp_landing_page = "https://sis.erp.bits-pilani.ac.in/psp/sisprd/EMPLOYEE/HRMS/h/?tab=DEFAULT"
                self.erp_swap_link = "https://sis.erp.bits-pilani.ac.in/psp/sisprd/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSR_SSENRL_SWAP.GBL?FolderPath=PORTAL_ROOT_OBJECT.CO_EMPLOYEE_SELF_SERVICE.HCCC_ENROLLMENT.HC_SSR_SSENRL_SWAP&IsFolder=false&IgnoreParamTempl=FolderPath%2cIsFolder"
                self.erp_weekly_schedule = "https://sis.erp.bits-pilani.ac.in/psp/sisprd/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSR_SSENRL_SWAP.GBL?FolderPath=PORTAL_ROOT_OBJECT.CO_EMPLOYEE_SELF_SERVICE.HCCC_ENROLLMENT.HC_SSR_SSENRL_SWAP&IsFolder=false&IgnoreParamTempl=FolderPath%2cIsFolder"
                
                self.userID = self.__getUserID()
                self.password = self.__getPassword()
                self.toDrop = self.__getDropClass()
                self.toPick = self.__getPickClass()
        
        def run(self):
                if not self.__login():
                        print("|| YOUR USER ID AND/OR PASSWORD ARE INVALID || THE ERP IS DOWN ||")
                        time.sleep(10)
                        self.driver.quit()
                        exit()
                while True:
                        flag = self.__swap()
                        if flag:
                                self.driver.get(self.erp_weekly_schedule)
                                break

        def __swap(self):
                self.driver.get(self.erp_swap_link)
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("""//*[@id="ptifrmtgtframe"]"""))
                try:
                        elem = elementOne = self.driver.find_element_by_name("DERIVED_REGFRM1_DESCR50$37$")
                        if elem.is_displayed():
                                selectOne = Select(elementOne)
                                selectOne.select_by_visible_text(self.toDrop)
                                self.driver.find_element_by_name("DERIVED_REGFRM1_SSR_PB_SRCH$41$").click()
                                time.sleep(1)
                                self.driver.find_element_by_name("CLASS_SRCH_WRK2_CATALOG_NBR$72$").send_keys(self.toPick['code'])
                                elementTwo = self.driver.find_element_by_name("CLASS_SRCH_WRK2_SUBJECT$64$")
                                selectTwo = Select(elementTwo)
                                selectTwo.select_by_value(self.toPick['dept'])
                                self.driver.find_element_by_name("CLASS_SRCH_WRK2_SSR_PB_CLASS_SRCH").click()
                                time.sleep(1)
                                #TODO
                                try:
                                        elem = self.driver.find_element_by_xpath("""//*[@id="CLASS_SRCH_WRK2_SSR_PB_SELECT$0"]""")
                                        if elem.is_displayed():
                                                elem.click()
                                                time.sleep(1)
                                                self.driver.find_element_by_xpath("""//*[@id="DERIVED_CLS_DTL_NEXT_PB$75$"]""").click()
                                                time.sleep(1)
                                                self.driver.find_element_by_xpath("""//*[@id="DERIVED_REGFRM1_SSR_PB_SUBMIT"]""").click()
                                                return True
                                except NoSuchElementException:
                                        # driver.close()
                                        return False
                except NoSuchElementException:
                        # driver.close()
                        return False
        
        def __login(self):
                self.driver.get(self.erp_login_link)
                self.driver.find_element_by_id('userid').send_keys(self.userID)
                self.driver.find_element_by_id('pwd').send_keys(self.password)
                self.driver.find_element_by_class_name('psloginbutton').click()
                time.sleep(1)
                if self.driver.current_url == self.erp_login_error:
                        return False
                else:
                        return True
        
        def __getUserID(self):
                return input("USER ID: ")

        def __getPassword(self):
                return input("PASSWORD: ")

        def __getDropClass(self):
                print("|| DROP COURSE ||")
                return input("COURSE NAME: ")

        def __getPickClass(self):
                print("|| PICK COURSE ||")
                classDept = input("DEPARTMENT CODE: ").upper()
                classCode = input("COURSE CODE: ")
                return {"dept": classDept, "code": classCode}


if __name__ == "__main__":
    bot = erp()
    bot.run()