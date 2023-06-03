from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    locattion = models.CharField(max_length=150)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} {self.locattion}"


class Device(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_staff = models.BooleanField(default=False)
    devices = models.ManyToManyField(Device, through="DeviceAllocation")

    def __str__(self):
        return self.user.username


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

    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    log_type = models.CharField(
        max_length=2, choices=LOG_TYPE_CHOICES, default=NO_CHECKOUT
    )
    checked_out_date = models.DateTimeField()
    returned_date = models.DateTimeField(blank=True, null=True)
    condition_out = models.CharField(max_length=10, choices=CONDITION_CHOICES)
    condition_in = models.CharField(max_length=10, choices=CONDITION_CHOICES)

    def __str__(self):
        return f"{self.device.name} - {self.employee.user.username}"


class DeviceAllocation(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
