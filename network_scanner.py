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
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    # print(answered_list.summary())

    print("IP\t\t\tMAC Address\n=========================================")
    for element in answered_list:
        print(element[1].psrc + "\t\t" + element[1].hwsrc)
      



scan("10.0.2.1/24")