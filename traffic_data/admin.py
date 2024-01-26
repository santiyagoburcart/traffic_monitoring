# traffic_data/admin.py
from django.contrib import admin

from .models import Person_IP, TrafficData


class PersonIPAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'source_ipv4', 'source_ipv6')
    search_fields = ['user__username', 'first_name', 'last_name']
    list_filter = ['source_ipv4', 'source_ipv6']

class TrafficDataAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'source_ipv4', 'destination_ipv4', 'source_ipv6', 'destination_ipv6', 'protocol', 'size', 'username_T', 'download_bytes', 'upload_bytes')
    search_fields = ['source_ipv4', 'destination_ipv4', 'source_ipv6', 'destination_ipv6', 'username_T']
    list_filter = ['timestamp', 'protocol']


admin.site.register(Person_IP, PersonIPAdmin)
admin.site.register(TrafficData, TrafficDataAdmin)
