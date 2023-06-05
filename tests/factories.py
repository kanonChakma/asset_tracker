import factory

from assets.models import Company, Device, DeviceAllocation, Employee


class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company

    name = "company1"
    location = "location1"
    about = "This is company!!!"


class DeviceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Device

    name = "device1"
    identifier = "identifier-one"
    description = "This is device!!!!"


class EmployeeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Employee

    first_name = "company1"
    last_name = "company2"
    company = factory.SubFactory(CompanyFactory)
    email = "employee@gmail.com"


class DeviceAllocationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = DeviceAllocation

    device = factory.SubFactory(DeviceFactory)
    employee = factory.SubFactory(EmployeeFactory)
    start_date = "12-12-2022"
    end_date = "1-5-2-2023"
