'''
Created on Dec 12, 2013

@author: abench
'''

from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time


class webHelper():
    def __init__(self):
        self.success = True
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        
    def setText(self, locator, text):
        self.wd.find_element_by_xpath(locator).click()
        self.wd.find_element_by_xpath(locator).clear()
        self.wd.find_element_by_xpath(locator).send_keys(text)
        
    def selectCheckbox(self, locator):
        if not self.wd.find_element_by_xpath(locator).is_selected():
            self.wd.find_element_by_xpath(locator).click()
        
    def unselectCheckBox(self, locator):
        if self.wd.find_element_by_xpath(locator).is_selected():
            self.wd.find_element_by_xpath(locator).click()
        
    def clickButton(self, locator):
        self.wd.find_element_by_xpath(locator).click()    
        
    def open(self,locator):
        self.wd.get(locator)     
            