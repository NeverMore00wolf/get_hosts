from scapy.all import *
#import netifaces

#sniff source code    sendrecv.py

def capture():
    # dpkt = sniff(iface = "Realtek PCIe GBE Family Controller", filter = 'icmp', count = 1000, prn = lambda x: x.summary())
    dpkt = sniff(iface="en0", filter='tcp', count=3999)
    wrpcap("http.pcap", dpkt)

