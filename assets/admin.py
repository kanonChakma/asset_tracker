from django.contrib import admin

from . import models


@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "location")


@admin.register(models.Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ("name", "description")


@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("company", "user", "is_staff")


@admin.register(models.DeviceCheck)
class DeviceCheckAdmin(admin.ModelAdmin):
    list_display = (
        "device",
        "employee",
        "log_type",
        "checked_out_date",
        "returned_date",
        "condition_in",
        "condition_out",
    )


@admin.register(models.DeviceAllocation)
class DeviceAllocationAdmin(admin.ModelAdmin):
    list_display = ("device", "employee", "start_date", "end_date")
