from django.db import models
from django.contrib.auth.models import User
import uuid



class Person_IP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    source_ipv4 = models.GenericIPAddressField(protocol='IPv4', null=True)
    source_ipv6 = models.GenericIPAddressField(protocol='IPv6', null=True)

    def save(self, *args, **kwargs):
        # ایجاد یک شناسه یکتا برای user
        if not self.user_id:
            self.user_id = uuid.uuid4().int
        super().save(*args, **kwargs)




class TrafficData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    source_ipv4 = models.GenericIPAddressField(protocol='IPv4', null=True)
    destination_ipv4 = models.GenericIPAddressField(protocol='IPv4', null=True)
    source_ipv6 = models.GenericIPAddressField(protocol='IPv6', null=True)
    destination_ipv6 = models.GenericIPAddressField(protocol='IPv6', null=True)
    protocol = models.CharField(max_length=50)
    size = models.BigIntegerField()
    #sizev6 = models.BigIntegerField()
    username_T = models.CharField(max_length=100, null=True, default=None)
    download_bytes = models.BigIntegerField(default=0)
    upload_bytes = models.BigIntegerField(default=0)

    def __str__(self):
        return f"{self.source_ipv4} - {self.destination_ipv4} - {self.source_ipv6} - {self.destination_ipv6}"

    class Meta:
        ordering = ['-timestamp']