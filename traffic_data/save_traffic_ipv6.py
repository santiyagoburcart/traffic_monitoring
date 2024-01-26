# traffic_data/save_traffic_ipv6.py
from traffic_data.models import TrafficData
from scapy.all import *

def save_traffic_ipv6(source_ipv6, destination_ipv6, protocol, size):
    TrafficData.objects.create(
        source_ipv6=source_ipv6,
        destination_ipv6=destination_ipv6,
        protocol=protocol,
        size=size
    )

def packet_callback_ipv6(packet):
    if IPv6 in packet:
        source_ipv6 = packet[IPv6].src
        destination_ipv6 = packet[IPv6].dst
        protocol = packet[IPv6].nh
        size = len(packet)

        # ذخیره اطلاعات IPv6 در دیتابیس جنگو
        save_traffic_ipv6(source_ipv6, destination_ipv6, protocol, size)
