from pytest_factoryboy import register

from .factories import (
    CompanyFactory,
    DeviceAllocationFactory,
    DeviceFactory,
    EmployeeFactory,
)

register(CompanyFactory)
register(EmployeeFactory)
register(DeviceFactory)
register(DeviceAllocationFactory)
