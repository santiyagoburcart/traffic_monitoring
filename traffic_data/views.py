# traffic_data/views.py

from django.shortcuts import render
from django.db.models import Q

from .forms import TrafficDataForm
from .models import TrafficData

def traffic_list(request):
    data = TrafficData.objects.all()
    return render(request, 'traffic_data/traffic_list.html', {'data': data})

def calculate_traffic(request):
    if request.method == 'POST':
        form = TrafficDataForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            ip_address_v4 = form.cleaned_data['ip_address_v4']
            ip_address_v6 = form.cleaned_data['ip_address_v6']

            # انجام محاسبات بر اساس تاریخ و ایپی
            traffic_data_v4 = TrafficData.objects.filter(
                timestamp__gte=start_date,
                timestamp__lte=end_date,
                source_ipv4=ip_address_v4
            ) | TrafficData.objects.filter(
                timestamp__gte=start_date,
                timestamp__lte=end_date,
                destination_ipv4=ip_address_v4
            )

            traffic_data_v6 = TrafficData.objects.filter(
                timestamp__gte=start_date,
                timestamp__lte=end_date,
                source_ipv6=ip_address_v6
            ) | TrafficData.objects.filter(
                timestamp__gte=start_date,
                timestamp__lte=end_date,
                destination_ipv6=ip_address_v6
            )

            total_traffic_v4 = sum([data.size for data in traffic_data_v4])
            print(f"total_traffic_v4 {total_traffic_v4}")
            total_traffic_v6 = sum([data.size for data in traffic_data_v6])
            print(f"total_traffic_v6 {total_traffic_v6}")

            return render(request, 'result.html', {'total_traffic_v4': total_traffic_v4, 'total_traffic_v6': total_traffic_v6})
    else:
        form = TrafficDataForm()

    return render(request, 'calculate_traffic.html', {'form': form})
