'''
Created on Dec 10, 2013

@author: abench
'''




from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time




success = True
wd = WebDriver()
wd.implicitly_wait(60)

def pppoe(success):
    try:
        adminUser = "admin"
        adminPassword = "admin"
        login(adminUser, adminPassword)
        portLocator = "//blockquote/form/div/table/tbody/tr[1]/td[2]/input"
        # port
        wd.find_element_by_xpath(portLocator).click()
        wd.find_element_by_xpath(portLocator).clear()
        wd.find_element_by_xpath(portLocator).send_keys("0")
        #vpi
        vpiLocator = "//blockquote/form/div/table/tbody/tr[2]/td[2]/input"
        wd.find_element_by_xpath(vpiLocator).click()
        wd.find_element_by_xpath(vpiLocator).clear()
        wd.find_element_by_xpath(vpiLocator).send_keys("0")
        #vci
        vciLocator = "//blockquote/form/div/table/tbody/tr[3]/td[2]/input"
        wd.find_element_by_xpath(vciLocator).click()
        wd.find_element_by_xpath(vciLocator).clear()
        wd.find_element_by_xpath(vciLocator).send_keys("35")
        
        
        # press next
        nextButtonLocator = "//blockquote/form/center/input"
        wd.find_element_by_xpath(nextButtonLocator).click()
        
        # select PPP over Ethernet
        pppoeSelectLocator = "//blockquote/form/table/tbody/tr[3]/td/input"
        wd.find_element_by_xpath(pppoeSelectLocator).click()
        # press next button
        nextButton1Locator = "//blockquote/form/p[2]/input[2]"
        wd.find_element_by_xpath(nextButton1Locator).click()
        # enter pppoe username
        pppoeUsernameLocator = "//blockquote/form/table[1]/tbody/tr[1]/td[2]/input"
        pppoeUserName = "admin"
        wd.find_element_by_xpath(pppoeUsernameLocator).click()
        wd.find_element_by_xpath(pppoeUsernameLocator).clear()        
        wd.find_element_by_xpath(pppoeUsernameLocator).send_keys(pppoeUserName)
        # enter pppoe password
        pppoePasswordLocator = "//blockquote/form/table[1]/tbody/tr[2]/td[2]/input"
        pppoeUserPassword = "admin"
        wd.find_element_by_xpath(pppoePasswordLocator).click()
        wd.find_element_by_xpath(pppoePasswordLocator).clear()        
        wd.find_element_by_xpath(pppoePasswordLocator).send_keys(pppoeUserPassword)
        # confirm pppoe password
        pppoePasswordConfirmLocator = "//blockquote/form/table[1]/tbody/tr[3]/td[2]/input"
        wd.find_element_by_xpath(pppoePasswordConfirmLocator).click()
        wd.find_element_by_xpath(pppoePasswordConfirmLocator).clear()
        wd.find_element_by_xpath(pppoePasswordConfirmLocator).send_keys(pppoeUserPassword)
        # press next
        nextButton2Locator = "//blockquote/form/center/input[2]"
        wd.find_element_by_xpath(nextButton2Locator).click()
        # press next
        nextButton3Locator = "//blockquote/form/center/input[2]"
        wd.find_element_by_xpath(nextButton3Locator).click()
        # press next
        nextButton4Locator = "//blockquote/form/center/input[2]"
        wd.find_element_by_xpath(nextButton4Locator).click()
        # press save
        nextButton5Locator = "//blockquote/form/center/input[2]"
        wd.find_element_by_xpath(nextButton5Locator).click()
        
    finally:
        wd.quit()
        if not success:
            raise Exception("Test failed.")



def login(adminUser, adminPassword):
    return wd.get("http://" + adminUser + ":" + adminPassword + "@192.168.1.1/")


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

pppoe(success, wd)
