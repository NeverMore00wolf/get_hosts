from scapy.all import *
import netifaces


def capture():
    # dpkt = sniff(iface = "Realtek PCIe GBE Family Controller", filter = 'icmp', count = 1000, prn = lambda x: x.summary())
    dpkt = sniff(iface="Realtek PCIe GBE Family Controller", filter='tcp', count=9999999)
    wrpcap("http.pcap", dpkt)

