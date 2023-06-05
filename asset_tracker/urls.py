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
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r"companies", CompanyViewSet, basename="company")

urlpatterns = [
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    # admin
    path("admin/", admin.site.urls),
    # jwt
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # device
    path("api/devices/", DeviceListCreateView.as_view(), name="device-list"),
    path(
        "api/devices/<int:pk>/",
        DeviceRetrieveUpdateDestroyView.as_view(),
        name="device-detail",
    ),
    # employee
    path("api/employees/", EmployeeListCreateView.as_view(), name="employee-list"),
    path(
        "api/employees/<int:pk>/",
        EmployeeRetrieveUpdateDestroyView.as_view(),
        name="employee-detail",
    ),
    path(
        "api/employees/<int:emp_id>/devices/",
        DeviceListByEmployeeAPIView.as_view(),
        name="employee-devices",
    ),
    # company
    path("api/", include(router.urls)),
    # api schema
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]
