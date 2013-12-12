'''
Created on Dec 10, 2013

@author: abench
'''




from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from raw.bridge import clickNextButton




success = True
wd = WebDriver()
wd.implicitly_wait(60)

portLocator = "//blockquote/form/div/table/tbody/tr[1]/td[2]/input"
vpiLocator = "//blockquote/form/div/table/tbody/tr[2]/td[2]/input"
vciLocator = "//blockquote/form/div/table/tbody/tr[3]/td[2]/input"
nextButtonLocator = "//blockquote/form/center/input"
nextButton3Locator = "//blockquote/form/p[2]/input[2]"
nextButton2Locator = "//blockquote/form/center/input[2]"

pppoeSelectLocator = "//blockquote/form/table/tbody/tr[3]/td/input"
pppoeUsernameLocator = "//blockquote/form/table[1]/tbody/tr[1]/td[2]/input"
pppoePasswordLocator = "//blockquote/form/table[1]/tbody/tr[2]/td[2]/input"
pppoePasswordConfirmLocator = "//blockquote/form/table[1]/tbody/tr[3]/td[2]/input"

def setText(wd, locator, text):
    wd.find_element_by_xpath(locator).click()
    wd.find_element_by_xpath(locator).clear()
    wd.find_element_by_xpath(locator).send_keys(text)
    
def selectCheckbox(wd, locator):
    if not wd.find_element_by_xpath(locator).is_selected():
        wd.find_element_by_xpath(locator).click()
        
def clickButton(wd, locator):
    wd.find_element_by_xpath(locator).click()      


  
    
def unselectCheckBox(wd, locator):
    if wd.find_element_by_xpath(locator).is_selected():
        wd.find_element_by_xpath(locator).click()
        
        
def clickNextButton2():
    return clickButton(wd, nextButton2Locator)


def setPortNum(num):
    setText(wd,portLocator,num)
    
def setVpi(num):
    setText(wd,vpiLocator,num)
    
def setVci(num):
    setText(wd,vciLocator,num)

def login(adminUser, adminPassword):
    return wd.get("http://" + adminUser + ":" + adminPassword + "@192.168.1.1/")



def selectPppoe():
    return clickButton(wd, pppoeSelectLocator)


def clickNextButton3():
    return clickButton(wd, nextButton3Locator)


def setPppoeUserName(pppoeUserName):
    setText(wd, pppoeUsernameLocator, pppoeUserName)


def setPppoeUserPassword(pppoeUserPassword):
    setText(wd, pppoePasswordLocator, pppoeUserPassword)
    


def confirmPppoeUserPassword(pppoeUserPassword):
    setText(wd, pppoePasswordConfirmLocator, pppoeUserPassword)
    


def pppoe(success):
    try:
        adminUser = "admin"
        adminPassword = "admin"
        portNum = "0"
        vpiNum = "0"
        vciNum = "35"
        pppoeUserName = "admin"
        pppoeUserPassword = "admin"
                
        login(adminUser, adminPassword)
        setPortNum(portNum)
        setVpi(vpiNum)
        setVci(vciNum)
        clickNextButton()
        selectPppoe()
        clickNextButton3()        
        setPppoeUserName(pppoeUserName)
        setPppoeUserPassword(pppoeUserPassword)
        confirmPppoeUserPassword(pppoeUserPassword)
        clickNextButton2()
        clickNextButton2()
        clickNextButton2()
        clickNextButton2()

        
    finally:
        wd.quit()
        if not success:
            raise Exception("Test failed.")





def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

pppoe(success, wd)
