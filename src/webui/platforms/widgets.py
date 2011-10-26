'''
Created on Oct 25, 2011

@author: mmornati
'''
from webui.widgets.base import Widget
import logging
import settings as platform_settings
import imp
import sys
logger = logging.getLogger(__name__)

class ApplicationsStatus(Widget):
    template = "widgets/applistatus/applistatus.html"
    
    def get_context(self):
        super_context = super(self.__class__,self).get_context()
        applications = []
        for platform in platform_settings.INSTALLED_PLATFORMS:
            #TODO: Make this part dynamic
            platform_name = 'webui.platforms.' + platform
            try:
                platform_path = __import__(platform_name, {}, {}, [platform_name.split('.')[-1]]).__path__
            except AttributeError:
                continue
            
            try:
                fp, pathname, description = imp.find_module('applications', platform_path)
                mod = imp.load_module('applications', fp, pathname, description)
                applications_list = mod.getApplications(self.user)
                if applications_list:
                    applications.extend(applications_list)
            except:
                logger.debug('No module applications found for %s' % platform_path)
        widget_context = {"applications":applications}
        return dict(super_context.items() + widget_context.items())