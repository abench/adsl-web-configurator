'''
Created on Dec 14, 2013

@author: abench
'''
from util.configParser import parseConfig
from adsl.adslConfigurator import adslConfigurator 

if __name__=="__main__":
    params=parseConfig("settings.ini")
    configurator=adslConfigurator( params["modemModel"])
    if params["modemMode"]=="bridge":
        configurator.setBridgeMode(params)
    else:
        if ["modemMode"]=="pppoe":
            configurator.setPppoeMode(params)
        
        
