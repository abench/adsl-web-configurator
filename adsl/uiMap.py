'''
Created on Dec 12, 2013

@author: abench
'''

import csv

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
        with open(fname, 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                self.locators.set(row[0],row[1])       