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

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False
    
#    
# locators
#

portLocator = "//blockquote/form/div/table/tbody/tr[1]/td[2]/input"
vpiLocator = "//blockquote/form/div/table/tbody/tr[2]/td[2]/input"
vciLocator = "//blockquote/form/div/table/tbody/tr[3]/td[2]/input"
qosLocator = "//blockquote/form/div/div/table/tbody/tr/td[2]/input"
nextButtonLocator = "//blockquote/form/center/input"
bridgingModeLocator = "//blockquote/form/table/tbody/tr[9]/td/input"
enableBridgeServiceLocator = "//blockquote/form/p[2]/input[2]"
enableBridgeSelectorLocator = "//blockquote/form/table/tbody/tr[1]/td[2]/input"
nextButton2Locator = "//blockquote/form/center/input[2]"

serviceNameLocator = "//blockquote/form/table/tbody/tr[2]/td[2]/input"
modemIPLocator = "//blockquote/form/table/tbody/tr[1]/td[2]/input"
modemNetMaskLocator="//blockquote/form/table/tbody/tr[2]/td[2]/input"
startPageLocator ="http://%s:%s@192.168.1.1/"



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


def setPortNum(num):
    setText(wd,portLocator,num)
    
def setVpi(num):
    setText(wd,vpiLocator,num)
    
def setVci(num):
    setText(wd,vciLocator,num)
    
def enableQoS():
    selectCheckbox(wd, qosLocator)
    
def clickNextButton():
    clickButton(wd, nextButtonLocator)
    
def selectBridgingMode():
    clickButton(wd, bridgingModeLocator)

def login(adminUser, adminPassword):
    wd.get("http://" + adminUser + ":" + adminPassword + "@192.168.1.1/")





def enableBridgeService():
    clickButton(wd, enableBridgeServiceLocator)    
    unselectCheckBox(wd, enableBridgeSelectorLocator)


def clickNextButton2():
    return wd.find_element_by_xpath(nextButton2Locator).click()


def setServiceName(serviceName):
    setText(wd, serviceNameLocator, serviceName)


def setModemIP(modemIP):
    setText(wd, modemIPLocator, modemIP)


def setModemNetMask(modemNetMask):
    setText(wd, modemNetMaskLocator, modemNetMask)

def bridge(success, wd):
    try:
        # login
        adminUser = "admin"
        adminPassword = "admin"
        portNum = "0"
        vpiNum = "0"
        vciNum = "35"
        serviceName = "br_0_0_35"
        modemIP = "192.168.1.1"
        modemNetMask = "255.255.255.0"
        
        
        login(adminUser, adminPassword)
        setPortNum(portNum)
        setVpi(vpiNum)
        setVci(vciNum)
        enableQoS()
        clickNextButton()
        selectBridgingMode()
        enableBridgeService()
        setServiceName(serviceName)
        clickNextButton2()
        setModemIP(modemIP)
        setModemNetMask(modemNetMask)
        clickNextButton2()
        clickNextButton2()
        
    finally:
        wd.quit()
        if not success:
            raise Exception("Test failed.")




bridge(success, wd)
