'''
Created on Dec 12, 2013

@author: abench
'''

import csv
from util.configParser import parseConfig

class uiMap():
    def __init__(self,name):
        self.locators={}
        self.loadFromFile(name)
        return
    def get(self,locatorName):
        if self.locators!=None:
            return self.locators[locatorName]
        else:
            pass
    def set(self,locatorName,value):
        self.locators[locatorName]=value
        
    def loadFromFile(self,fname):
        self.locators = parseConfig(fname)