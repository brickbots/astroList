SC_IP='192.168.1.108'
SC_PORT=3292
BUFFER_SIZE=1024

import socket

class SkyChartControl(object):

    def __init__(self):
        #open socket and prep for commands
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.settimeout(1)
        try:
            self._socket.connect((SC_IP, SC_PORT))
            data = self._socket.recv(BUFFER_SIZE)
            print "Connection opened to skychart\n\t" + data
        except:
            print "SKYCHART: Could not open socket"
            self._socket=None


    def _sendCommand(self, command):
        if self._socket:
            #clear buffer
            data = self._socket.recv(BUFFER_SIZE)
            print "SKYCHART OUT: " + command
            self._socket.send(command + '\r\n')
            data = self._socket.recv(BUFFER_SIZE)
            print "SKYCHART IN:" + data
            return data
        else:
            return None

    def findObject(self, objectID):

        message='search %s' % objectID
        return self._sendCommand(message)

    def setFOV(self, fov):
        self._sendCommand('setfov %f' % fov)
        self._sendCommand('redraw')

    def disconnect(self):
        if self._socket:
            self._socket.close()