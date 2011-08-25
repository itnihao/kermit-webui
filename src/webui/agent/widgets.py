'''
Created on Aug 12, 2011

@author: mmornati
'''
from webui.widgets.base import Widget

class AgentsTree(Widget):
    template = "widgets/agent/agentstree.html"
    
    def get_context(self):
        super_context = super(self.__class__,self).get_context()
        return dict(super_context.items())
    
    
    
