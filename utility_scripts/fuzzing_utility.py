#! /usr/bin/env python3

import sys
from scapy.all import (IP, ICMP, UDP, TCP, sr1, wrpcap, fuzz, RandString, RandIP)

class fuzzing_attack(object):

    def generator(self, ip_dst, n_generations, n_packets, selected_layer):
        # Select the final layer for randomize

        if selected_layer == "UDP":
            layer = UDP()
        elif selected_layer == "TCP":
            layer = TCP()
        else:
            layer = ICMP()

        for i in range(n_generations):
            print('Generating packets. (%s of %s)\n' % (i+1, n_generations))
            pkts_send = [fuzz(IP(dst=ip_dst, src=RandIP()))/fuzz(layer)/str(RandString()) for j in range(n_packets)]
            self.send_pkts(pkts_send)

    def send_pkts(self, pkts):

        print('Sending packets generated.\n')

        # Packet generated because if there isn't any response the value will be None

        no_response_pkt = IP(src="127.0.0.1", dst="127.0.0.1")/"No response received"

        for pkt in pkts:
            self.pkts_write.append(pkt)
            pkt_received = sr1(pkt, verbose=0, timeout=1)

            if pkt_received == None:
                self.pkts_write.append(no_response_pkt)
            else:
                self.pkts_write.append(pkt_received)

    def write_pcap(self, pkts_write, filename):

        print('Writing pcap file.\n')
        wrpcap(filename, pkts_write)

        print('Done, all packets generated.')

    def __init__(self, ip, ngenerations, npackets, layer, filename):
        self.pkts_write = []
        self.generator(ip, ngenerations, npackets, layer)
        self.write_pcap(self.pkts_write, filename)