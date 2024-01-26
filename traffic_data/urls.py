# traffic_data/urls.py
from django.urls import path
from .views import traffic_list, calculate_traffic

urlpatterns = [
    path('list/', traffic_list, name='traffic-list'),
    path('calculate/', calculate_traffic, name='calculate-traffic'),  # مسیر برای محاسبه ترافیک

    # مسیرهای دیگر اگر وجود دارد
]