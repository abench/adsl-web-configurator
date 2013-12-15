'''
Created on Dec 12, 2013

@author: abench
'''


from adsl.webHelper import webHelper as webHelper
from adsl.uiMap import uiMap as uiMap

class adslModem():
    def __init__(self,name):
        self.map =uiMap(name)  
        self.browser = webHelper()
        
    def clickNextButton2(self):
        self.browser.clickButton(self.map.get("nextButton2Locator"))    
    
    def setPortNum(self,num):
        self.browser.setText(self.map.get("portLocator"),num)
        
    def setVpi(self,num):
        self.browser.setText(self.map.get("vpiLocator"),num)
        
    def setVci(self,num):
        self.browser.setText(self.map.get("vciLocator"),num)

    def enableQoS(self):
        self.browser.selectCheckbox(self.map.get("qosLocator"))
        
    def clickNextButton(self):
        self.browser.clickButton(self.map.get("nextButtonLocator"))
        
    def selectBridgingMode(self):
        self.browser.clickButton(self.map.get("bridgingModeLocator"))
        
    def login(self, adminUser, adminPassword):
        self.browser.open(self.map.get("startPageLocator") % (adminUser, adminPassword))
        
    def enableBridgeService(self):
        self.browser.clickButton(self.map.get("enableBridgeServiceLocator"))    
        self.browser.unselectCheckBox(self.map.get("enableBridgeSelectorLocator"))
    
    def setServiceName(self,serviceName):
        self.browser.setText(self.map.get("serviceNameLocator"), serviceName)
    
    
    def setModemIP(self,modemIP):
        self.browser.setText(self.map.get("modemIPLocator"), modemIP)
    
    
    def setModemNetMask(self,modemNetMask):
        self.browser.setText(self.map.get("modemNetMaskLocator"), modemNetMask)
        
    def selectPppoe(self):
        self.browser.clickButton(self.map.get("pppoeSelectLocator"))


    def clickNextButton3(self,):
        self.browser.clickButton(self.map.get("nextButton3Locator"))
    
    
    def setPppoeUserName(self, pppoeUserName):
        self.browser.setText(self.map.get("pppoeUsernameLocator"), pppoeUserName)
    
    
    def setPppoeUserPassword(self, pppoeUserPassword):
        self.browser.setText(self.map.get("pppoePasswordLocator"), pppoeUserPassword)
        
    
    
    def confirmPppoeUserPassword(self, pppoeUserPassword):
        self.browser.setText(self.map.get("pppoePasswordConfirmLocator"), pppoeUserPassword)
        
        
          
    
