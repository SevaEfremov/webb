from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Computer(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('reserved', 'Reserved'),
    ]

    name = models.CharField(max_length=100, unique=True, verbose_name="Computer Name")
    is_vip = models.BooleanField(default=False, verbose_name="VIP Status")
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2, default=0.00, verbose_name="Hourly Rate")
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='available',
        verbose_name="Reservation Status"
    )
    reserved_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name="reserved_computers",
        verbose_name="Reserved By"
    )
    reserved_from = models.DateTimeField(null=True, blank=True, verbose_name="Reservation Start Time")
    reserved_until = models.DateTimeField(null=True, blank=True, verbose_name="Reservation End Time")

    def __str__(self):
        return f"{self.name} ({'VIP' if self.is_vip else 'Standard'})"

    class Meta:
        verbose_name = "Computer"
        verbose_name_plural = "Computers"