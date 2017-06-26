#! /usr/bin/env python3

import socket

class banner_grabbing(object):

    def setting_vars(self, ports):
        self.parse_ports = ports.split(':')

    def run(self, ip, filename):

        for port in self.parse_ports:
            if filename is None:
                try:
                    sck = socket.socket()
                    sck.settimeout(5)
                    print("Connecting to %s in the port: %s" % (ip, str(port)))
                    sck.connect((str(ip), int(port)))
                    banner = sck.recv(1024)
                    print(banner)
                except:
                    print("Connection failed.")
            else:
                try:
                    sck = socket.socket()
                    sck.settimeout(5)
                    print("Connecting to %s in the port: %s" % (ip, str(port)))
                    sck.connect((str(ip), int(port)))
                    banner = sck.recv(1024)
                    file = open(filename, 'a')
                    file.write(banner)
                except:
                    print('Connection failed.')

    def __init__(self, ip, ports, filename ):
        self.setting_vars(ports)
        self.run(ip, filename)
        print("All available banners grabbed.")