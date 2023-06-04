from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .models import Company, Device, Employee
from .serailizers import CompanySerializer, DeviceSerializer, EmployeeSerializer


class CompanyViewSet(ViewSet):
    queryset = Company.objects.all()

    def list(self, request):
        print("This is calling!!!!!")
        serializer = CompanySerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrive(self, request, pk=None):
        print("This is calling!!!!!")
        company = get_object_or_404(self.queryset, pk=pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def search(self, request):
        company_name = request.query_params.get("name", "")
        company = Company.objects.filter(name__icontains=company_name)
        serializer = CompanySerializer(company, many=True)
        return Response(serializer.data)


class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DeviceListCreateView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
