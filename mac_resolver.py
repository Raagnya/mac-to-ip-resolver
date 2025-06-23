

from scapy.all import ARP, Ether, srp

def get_ip_from_mac(target_mac, ip_range="192.168.1.1/24", interface="eth0"):
    """
    Scan the local network to find the IP for a given MAC address.
    """
    target_mac = target_mac.lower()
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    result = srp(packet, timeout=2, iface=interface, verbose=0)[0]

    for sent, received in result:
        if received.hwsrc.lower() == target_mac:
            return received.psrc  
    return None
