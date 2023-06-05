from rest_framework import serializers

from .models import Company, Device, DeviceAllocation, DeviceCheck, Employee


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class DeviceCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceCheck
        fields = [
            "log_type",
            "checked_out_date",
            "returned_date",
            "condition_out",
            "condition_in",
        ]


class DeviceSerializer(serializers.ModelSerializer):
    device_checks = DeviceCheckSerializer(many=True, read_only=True)

    class Meta:
        model = Device
        fields = ["name", "description", "device_checks"]


class DeviceAllocationSerializer(serializers.ModelSerializer):
    device = DeviceSerializer()

    class Meta:
        model = DeviceAllocation
        fields = "__all__"
