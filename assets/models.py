from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    about = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Device(models.Model):
    identifier = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"


class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    join_date = models.DateField()
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class DeviceCheck(models.Model):
    CHECKOUT = "CO"
    RETURN = "RT"
    NO_CHECKOUT = "NC"

    LOG_TYPE_CHOICES = [
        (CHECKOUT, "Check Out"),
        (RETURN, "Returned"),
        (NO_CHECKOUT, "Not Checked Out"),
    ]

    CONDITION_CHOICES = (
        ("Good", "Good"),
        ("Fair", "Fair"),
        ("Poor", "Poor"),
    )

    device = models.ForeignKey(
        Device, on_delete=models.CASCADE, related_name="device_checks"
    )
    log_type = models.CharField(
        max_length=2, choices=LOG_TYPE_CHOICES, default=NO_CHECKOUT
    )
    checked_out_date = models.DateTimeField()
    returned_date = models.DateTimeField(blank=True, null=True)
    condition_out = models.CharField(max_length=10, choices=CONDITION_CHOICES)
    condition_in = models.CharField(
        max_length=10, choices=CONDITION_CHOICES, default="Good"
    )

    def __str__(self):
        return f"{self.device.name} - {self.device.name}"


class DeviceAllocation(models.Model):
    device = models.ForeignKey(
        Device, on_delete=models.CASCADE, related_name="device_allocation"
    )
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="device_allocation"
    )
    start_date = models.DateField()
    end_date = models.DateField()
