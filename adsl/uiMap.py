'''
Created on Dec 12, 2013

@author: abench
'''

class uiMap():
    def __init__(self):
        self.locators=None
        return
    def get(self,locatorName):
        if self.locators!=None:
            return self.locators[locatorName]
        else:
            pass
    def set(self,locatorName,value):
        self.locators[locatorName]=value
        
    def loadFromFile(self,fname):
        pass
        
        