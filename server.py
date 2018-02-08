# server.py
# Math tools web application
# Author: Sébastien Combéfis
# Version: February 8, 2018

import cherrypy

class WebApp:
    @cherrypy.expose
    def index(self):
        '''Main page of the website'''
        return "".encode("utf-8")

cherrypy.quickstart(WebApp(), '', 'server.conf')
