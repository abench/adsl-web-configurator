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

try:
     wd.get("http://admin:admin@192.168.1.1/")
     wd.find_element_by_xpath("//blockquote/form/div/table/tbody/tr[1]/td[2]/input").click()
     wd.find_element_by_xpath("//blockquote/form/div/table/tbody/tr[1]/td[2]/input").clear()
     wd.find_element_by_xpath("//blockquote/form/div/table/tbody/tr[1]/td[2]/input").send_keys("0")
     wd.find_element_by_xpath("//blockquote/form/div/table/tbody/tr[2]/td[2]/input").click()
     wd.find_element_by_xpath("//blockquote/form/div/table/tbody/tr[2]/td[2]/input").clear()
     wd.find_element_by_xpath("//blockquote/form/div/table/tbody/tr[2]/td[2]/input").send_keys("0")
    wd.find_element_by_xpath("//blockquote/form/div/table/tbody/tr[3]/td[2]/input").click()
    wd.find_element_by_xpath("//blockquote/form/div/table/tbody/tr[3]/td[2]/input").clear()
    wd.find_element_by_xpath("//blockquote/form/div/table/tbody/tr[3]/td[2]/input").send_keys("35")
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
