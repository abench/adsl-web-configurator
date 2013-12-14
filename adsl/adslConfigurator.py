'''
Created on Dec 14, 2013

@author: abench
'''

from adsl.adslModem import adslModem

class adslConfigurator():
    def __init__(self,name):
        self.modem = adslModem(name)
        
    def setBridgeMode(self,param):
        with self.modem as m, param as p:                        
            m.login(p["adminUser"], p["adminPassword"])
            m.setPortNum(p["portNum"])
            m.setVpi(p["vpiNum"])
            m.setVci(p["vciNum"])
            m.enableQoS()
            m.clickNextButton()
            m.selectBridgingMode()
            m.enableBridgeService()
            m.setServiceName(p["serviceName"])
            m.clickNextButton2()
            m.setModemIP(p["modemIP"])
            m.setModemNetMask(p["modemNetMask"])
            m.clickNextButton2()
            m.clickNextButton2()
            
    def setPppoeMode (self,param):
        with self.modem as m, param as p:
            m.login(p["adminUser"], p["adminPassword"])
            m.setPortNum(p["portNum"])
            m.setVpi(p["vpiNum"])
            m.setVci(p["vciNum"])
            m.clickNextButton()
            m.selectPppoe()
            m.clickNextButton3()        
            m.setPppoeUserName(p["pppoeUserName"])
            m.setPppoeUserPassword(p["pppoeUserPassword"])
            m.confirmPppoeUserPassword(p["pppoeUserPassword"])
            m.clickNextButton2()
            m.clickNextButton2()
            m.clickNextButton2()
            m.clickNextButton2()

            

        
    
        