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
# locators
portLocator = "//blockquote/form/div/table/tbody/tr[1]/td[2]/input"
vpiLocator = "//blockquote/form/div/table/tbody/tr[2]/td[2]/input"
vciLocator = "//blockquote/form/div/table/tbody/tr[3]/td[2]/input"
qosLocator = "//blockquote/form/div/div/table/tbody/tr/td[2]/input"


def setText(wd, locator, text):
    wd.find_element_by_xpath(locator).click()
    wd.find_element_by_xpath(locator).clear()
    wd.find_element_by_xpath(locator).send_keys(text)
    
def selectCheckbox(wd, locator):
    if not wd.find_element_by_xpath(locator).is_selected():
        wd.find_element_by_xpath(locator).click()
        
def clickButton(wd, locator):
    wd.find_element_by_xpath(locator).click()        
    

def setPortNum(num):
    setText(wd,portLocator,num)
    
def setVpi(num):
    setText(wd,vpiLocator,num)
    
def setVci(num):
    setText(wd,vciLocator,num)
    
def enableQoS():
    selectCheckbox(wd, qosLocator)


def bridge(success, wd):
    try:
        # login
        wd.get("http://admin:admin@192.168.1.1/")
        # port
        
        portNum = "0"
        setPortNum(portNum)
        # vpi
        
        vpiNum = "0"
        setVpi(vpiNum)
        #vci
        
        vciNum = "35"
        setVci(vciNum)
        
        # Enable Quality of service
        enableQoS()
        # press next    
        nextButtonLocator = "//blockquote/form/center/input"
        wd.find_element_by_xpath(nextButtonLocator).click()
        # set bridging mode
        bridgingModeLocator = "//blockquote/form/table/tbody/tr[9]/td/input"
        wd.find_element_by_xpath(bridgingModeLocator).click()
        # set enable bridge service
        wd.find_element_by_xpath("//blockquote/form/p[2]/input[2]").click()
        if wd.find_element_by_xpath("//blockquote/form/table/tbody/tr[1]/td[2]/input").is_selected():
            wd.find_element_by_xpath("//blockquote/form/table/tbody/tr[1]/td[2]/input").click()
        
        # set service name
        serviceNameLocator = "//blockquote/form/table/tbody/tr[2]/td[2]/input"
        serviceName = "br_0_0_35"
        wd.find_element_by_xpath(serviceNameLocator).click()            
        wd.find_element_by_xpath(serviceNameLocator).clear()        
        wd.find_element_by_xpath(serviceNameLocator).send_keys(serviceName)
        # press next
        nextButton2Locator = "//blockquote/form/center/input[2]"
        wd.find_element_by_xpath(nextButton2Locator).click()
        # set modem ip
        modemIPLocator = "//blockquote/form/table/tbody/tr[1]/td[2]/input"
        modemIP = "192.168.1.1"
        wd.find_element_by_xpath(modemIPLocator).click()
        wd.find_element_by_xpath(modemIPLocator).clear()        
        wd.find_element_by_xpath(modemIPLocator).send_keys(modemIP)
        # set net mask for modem
        modemNetMaskLocator="//blockquote/form/table/tbody/tr[2]/td[2]/input"
        modemNetMask = "255.255.255.0"
        wd.find_element_by_xpath(modemNetMaskLocator).click()
        wd.find_element_by_xpath(modemNetMaskLocator).clear()        
        wd.find_element_by_xpath(modemNetMaskLocator).send_keys(modemNetMask)
        # press next
        wd.find_element_by_xpath(nextButton2Locator).click()
        # press next
        wd.find_element_by_xpath(nextButton2Locator).click()
    finally:
        wd.quit()
        if not success:
            raise Exception("Test failed.")




bridge(success, wd)
