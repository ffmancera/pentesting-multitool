#! /usr/bin/env python3

import dns, dns.resolver

class dns_scan(object):

    def run(self, domain, record, filename):

        if filename is not None:
            file = open(filename, 'a')
            print("File opened\n"
              "Writing the information on the file..")
            ans = dns.resolver.query(domain, record)
            file.write(ans.response.to_text())
            print("Done.")
            file.close()
        else:
            print('Getting information..')
            ans = dns.resolver.query(domain, record)
            print(ans.response.to_text())

    def __init__(self, domain, record, filename):
        self.run(domain, record, filename)
        exit()
