import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

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


@pytest.fixture
def api_client():
    return APIClient
