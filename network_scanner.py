#!/usr/bin/env python

import scapy.all as scapy
import optparse

# def get_ip():
#     parser = optparse.OptionParser()
#     parser.add_option("-i", "--ip_add", dest="ip_address", help="ip address in range to scan for MACs")
#     (option,arguments) = parser.parse_args()
#     if not options.ip_address:
#         parser.error("[-] Please specify an ip address in the range to scan for a MACs")
#     return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    client_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)       
    return client_list
      
def print_result(results_list):
        print("IP\t\t\tMAC Address\n=========================================")
        for client in results_list:
            print(client["ip"] +"\t\t"+ client["mac"])

# options.get_ip()
# scan_result = scan(options.ip_address)

scan_result = scan("10.0.2.1/24")
print_result(scan_result)