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
        # portLocator
        wd.find_element_by_xpath(portLocator).click()
        wd.find_element_by_xpath(portLocator).clear()
        wd.find_element_by_xpath(portLocator).send_keys("0")
        #vpiLocator
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
        wd.find_element_by_xpath("//blockquote/form/center/input").click()
        
        
        wd.find_element_by_xpath("//blockquote/form/table/tbody/tr[3]/td/input").click()
        wd.find_element_by_xpath("//blockquote/form/p[2]/input[2]").click()
        
        wd.find_element_by_xpath("//blockquote/form/table[1]/tbody/tr[1]/td[2]/input").click()
        wd.find_element_by_xpath("//blockquote/form/table[1]/tbody/tr[1]/td[2]/input").clear()
        wd.find_element_by_xpath("//blockquote/form/table[1]/tbody/tr[1]/td[2]/input").send_keys("admin")
        
        wd.find_element_by_xpath("//blockquote/form/table[1]/tbody/tr[2]/td[2]/input").click()
        wd.find_element_by_xpath("//blockquote/form/table[1]/tbody/tr[2]/td[2]/input").clear()
        wd.find_element_by_xpath("//blockquote/form/table[1]/tbody/tr[2]/td[2]/input").send_keys("admin")
        
        wd.find_element_by_xpath("//blockquote/form/table[1]/tbody/tr[3]/td[2]/input").click()
        wd.find_element_by_xpath("//blockquote/form/table[1]/tbody/tr[3]/td[2]/input").clear()
        wd.find_element_by_xpath("//blockquote/form/table[1]/tbody/tr[3]/td[2]/input").send_keys("admin")
        
        wd.find_element_by_xpath("//blockquote/form/center/input[2]").click()
        
        wd.find_element_by_xpath("//blockquote/form/center/input[2]").click()
        
        wd.find_element_by_xpath("//blockquote/form/center/input[2]").click()
        
        wd.find_element_by_xpath("//blockquote/form/center/input[2]").click()
        
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
