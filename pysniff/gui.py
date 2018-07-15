from .libs.observer import Observer
from .proxy import Proxy

from appJar import gui

import re

class Gui(Observer):

    def __init__(self):
        """Constructor"""
        Proxy().register(self)
        self.title = 'pysniff'
        self.app = gui(showIcon=False)
        self.log = ''

    def frame(self):
        """Setup the basic application frame."""
        self.app.setSize('1080x600')
        self.app.setFont(8)
        self.app.setTitle(self.title)
        
        self.app.startScrollPane('Pane')
        self.app.addMessage(self.title, self.log)
        self.app.registerEvent(self.updateWidget)
        self.app.stopScrollPane()
        self.app.go()

    def updateWidget(self):
        """Update event handler

        Updates the text on the text widget.
        """
        self.app.setMessage(self.title, self.log)

    def update(self, text=''):
        """Implementation of the observable update method.

        Updates the log text with new sniffed data.

        Args:
            text (str, optional): New log data. Defaults to an empty string.
        """
        text = re.sub(r'\n', '', text)
        self.log += re.sub(
            r'(GET|POST|PUT|DELETE|HEAD|CONNECT|OPTIONS|TRACE|PATCH)', 
            r'\n\n\1',
            text
        )
        print('Message: {}'.format(text.encode('utf-8', errors='ignore')))
