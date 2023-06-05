from assets.views import (
    CompanyViewSet,
    DeviceListByEmployeeAPIView,
    DeviceListCreateView,
    DeviceRetrieveUpdateDestroyView,
    EmployeeListCreateView,
    EmployeeRetrieveUpdateDestroyView,
)
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"companies", CompanyViewSet, basename="company")

urlpatterns = [
    # admin
    path("admin/", admin.site.urls),
    # device
    path("devices/", DeviceListCreateView.as_view(), name="device-list"),
    path(
        "devices/<int:pk>/",
        DeviceRetrieveUpdateDestroyView.as_view(),
        name="device-detail",
    ),
    # employee
    path("employees/", EmployeeListCreateView.as_view(), name="employee-list"),
    path(
        "employees/<int:pk>/",
        EmployeeRetrieveUpdateDestroyView.as_view(),
        name="employee-detail",
    ),
    path(
        "employees/<int:emp_id>/devices/",
        DeviceListByEmployeeAPIView.as_view(),
        name="employee-devices",
    ),
    # company
    path("", include(router.urls)),
    # api schema
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]
