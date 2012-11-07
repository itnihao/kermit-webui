'''
Created on Nov 7, 2012

@author: mmornati
'''

import os

def installed_plugins_list():
    path = os.path.dirname(__file__)
    installed_platforms = []
    for module in os.listdir(path):
        if os.path.isdir(path + '/' + module) == True:
            installed_platforms.append(module)
    return installed_platforms
