# traffic_data/save_traffic.py
from traffic_data.models import TrafficData
from scapy.all import *

from django.core.management.base import BaseCommand

from scapy.all import *

def save_traffic(source_ipv4, destination_ipv4, source_ipv6, destination_ipv6, protocol, size, ):
    # تبدیل به مگابایت
    #size_in_mbv4 = size / (1024 * 1024)
    #print(f"size before save: {size_in_mbv4} MB")

    TrafficData.objects.create(
        source_ipv4=source_ipv4,
        destination_ipv4=destination_ipv4,
        source_ipv6=source_ipv6,
        destination_ipv6=destination_ipv6,
        protocol=protocol,
        size=size ,# ذخیره اندازه در مگابایت
    )
    print("size saved successfully!")

def packet_callback(packet):
    if IP in packet and packet[IP].version == 4:
        source_ipv4 = packet[IP].src
        destination_ipv4 = packet[IP].dst
        protocol = packet[IP].proto
        size = len(packet)

        source_ipv6 = destination_ipv6  = None  # مقداردهی پیش‌فرض برای IPv6

        # ذخیره اطلاعات IPv4 در دیتابیس جنگو
        save_traffic(source_ipv4, destination_ipv4, source_ipv6, destination_ipv6, protocol, size,)

    elif IPv6 in packet:
        source_ipv6 = packet[IPv6].src
        destination_ipv6 = packet[IPv6].dst
        protocol = packet[IPv6].nh
        size = len(packet)
        source_ipv4 = destination_ipv4 =  None  # مقداردهی پیش‌فرض برای IPv4

        # ذخیره اطلاعات IPv6 در دیتابیس جنگو
        save_traffic(source_ipv4, destination_ipv4, source_ipv6, destination_ipv6, protocol, size,)

# شروع گوش دادن به ترافیک
sniff(prn=packet_callback, store=0)
