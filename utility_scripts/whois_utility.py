#! /usr/bin/env python3

import pythonwhois
from pprint import pformat, pprint

class whois_scan(object):

    def run(self, domain, filename):

        if filename is not None:
            file = open(filename, 'a')
            print("File opened\n"
              "Getting information and writing it on the file..")
            whois = pformat(pythonwhois.get_whois(domain))
            file.write(whois)
            file.close()
        else:
            "Getting information.."
            pprint(pythonwhois.get_whois(domain))


    def __init__(self, domain, filename):
        self.run(domain, filename)
        exit()