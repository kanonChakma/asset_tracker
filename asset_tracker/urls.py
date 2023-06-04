from assets.views import (
    CompanyViewSet,
    DeviceListCreateView,
    DeviceRetrieveUpdateDestroyView,
    EmployeeListCreateView,
    EmployeeRetrieveUpdateDestroyView,
)
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"companies", CompanyViewSet, basename="company")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("employees/", EmployeeListCreateView.as_view(), name="employee-list"),
    path(
        "employees/<int:pk>/",
        EmployeeRetrieveUpdateDestroyView.as_view(),
        name="employee-detail",
    ),
    path("devices/", DeviceListCreateView.as_view(), name="device-list"),
    path(
        "devices/<int:pk>/",
        DeviceRetrieveUpdateDestroyView.as_view(),
        name="device-detail",
    ),
    path("", include(router.urls)),
]
