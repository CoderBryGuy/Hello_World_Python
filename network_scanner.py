#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    # print(arp_request.summary()) 
    # scapy.ls(scapy.ARP())
    # arp_request.show()
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # scapy.ls(scapy.Ether())
    # print(broadcast.summary())
    # broadcast.show()
    arp_request_broadcast = broadcast/arp_request
    # print(arp_request_broadcast.summary())
    # arp_request_broadcast.show()
    answered_list, unaswered_list = scapy.srp(arp_request_broadcast, timeout=1)
    print(answered_list.summary())

# scan("192.168.1.1/24")
numbers = [4,3,2,6,775,433,23]


