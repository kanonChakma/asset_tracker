import pytest

pytestmark = pytest.mark.django_db


class TestCompanyModel:
    def test_str_method(self, company_factory):
        x = company_factory()
        assert x.__str__() == "company1"

    def test_company_property(self, company_factory):
        x = company_factory()
        assert x.name == "company1"
        assert x.location == "location1"
        assert x.about == "This is company!!!"


class TestDeviceModel:
    def test_str_method(self, device_factory):
        device = device_factory()
        assert device.__str__() == "device1"

    def test_device_property(self, device_factory):
        device = device_factory(
            name="device2", identifier="identifier2", description="This is device2!!"
        )
        assert device.__str__() == "device2"
        assert device.name == "device2"
        assert device.identifier == "identifier2"
        assert device.description == "This is device2!!"
