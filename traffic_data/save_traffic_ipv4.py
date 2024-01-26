# traffic_data/save_traffic_ipv4.py
from traffic_data.models import TrafficData
from scapy.all import *

def save_traffic_ipv4(source_ipv4, destination_ipv4, protocol, size):
    TrafficData.objects.create(
        source_ipv4=source_ipv4,
        destination_ipv4=destination_ipv4,
        protocol=protocol,
        size=size
    )

def packet_callback_ipv4(packet):
    if IP in packet and packet[IP].version == 4:
        source_ipv4 = packet[IP].src
        destination_ipv4 = packet[IP].dst
        protocol = packet[IP].proto
        size = len(packet)

        # ذخیره اطلاعات IPv4 در دیتابیس جنگو
        save_traffic_ipv4(source_ipv4, destination_ipv4, protocol, size)
