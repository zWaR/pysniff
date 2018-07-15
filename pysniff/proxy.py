import re
import socket
import string
import sys
import codecs

from .libs.subject import Subject

class Proxy(Subject):

    def __init__(self):
        """Constructor
        """
        self.port = 8080
        self.host = 'localhost'
        self.log_filename = 'pysniff.log'
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        codecs.register_error('dotescape', self._dotescape)
    
    def bind(self):
        """Bind to a port.

        Bind the socker listener to a port.
        """
        try:
            self.socket.bind((self.host, self.port))
        except Exception as exception:
            print('Binding {} to {} failed with {}'
                .format(self.host, self.port, exception))

    def listen(self):
        """Start listening (accepting connection) on the open socket.
        """
        self.socket.listen(10)

    def close(self):
        """Close the socket.
        """
        self.socket.close()

    def write_log(self, data):
        """Write the sniffed data to a log.

        Writes the data to a log file. It also converts the binary object to
        a printable string.

        Args:
            data (obj): A binary object of data which has to be stored to a
                log.
        """
        with open(self.log_filename, 'a', encoding='utf-8') as log:
            text = data.decode('utf-8', 'dotescape')
            text = re.sub(
                r'(GET|POST|PUT|DELETE|HEAD|CONNECT|OPTIONS|TRACE|PATCH)', 
                r'\n\n\1', 
                text
            )
            log.write(text)
        self.notify(text)

    def proxy_up(self):
        """Starts the proxy.
        """
        self.bind()
        self.listen()
        while True:
            conn, addr = self.socket.accept()
            print('Connected with {}:{}'.format(self.host, self.port))
            data = conn.recv(1000)
            # print(data)
            text = self.write_log(data)
        self.close()

    def _dotescape(self, err):
        """Decode error handler.

        Escape error handler for the decode method. It handles the unicode
        decode errors, which are thrown when decode does not know how to
        convert a specific character.

        Args:
            err (obj): Error object.
        """
        # print(err, dir(err), err.start, err.end, err.object[:err.start])
        byte = err.object[err.start:err.end]
        reply = '.'
        if len(byte) == 1:
            reply = u'\\x'+hex(ord(byte))[2:]
        else:
            for i in range(len(byte)):
                reply = '{}.'.format(reply)
        return (reply, err.end)
