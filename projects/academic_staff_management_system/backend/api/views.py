from django.shortcuts import render
from rest_framework import permissions, viewsets
from django.contrib.auth.models import User

from . import serializers
from . import models


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class PersonViewSet(viewsets.ModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AddressViewSet(viewsets.ModelViewSet):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class EducationViewSet(viewsets.ModelViewSet):
    queryset = models.Education.objects.all()
    serializer_class = serializers.EducationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PhoneNumberViewSet(viewsets.ModelViewSet):
    queryset = models.PhoneNumber.objects.all()
    serializer_class = serializers.PhoneNumberSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BuildingViewSet(viewsets.ModelViewSet):
    queryset = models.Building.objects.all()
    serializer_class = serializers.BuildingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class FacultyViewSet(viewsets.ModelViewSet):
    queryset = models.Faculty.objects.all()
    serializer_class = serializers.FacultySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OfficeViewSet(viewsets.ModelViewSet):
    queryset = models.Office.objects.all()
    serializer_class = serializers.OfficeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class FieldViewSet(viewsets.ModelViewSet):
    queryset = models.Field.objects.all()
    serializer_class = serializers.FieldSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = models.Professor.objects.all()
    serializer_class = serializers.PersonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ResearcherViewSet(viewsets.ModelViewSet):
    queryset = models.Researcher.objects.all()
    serializer_class = serializers.ResearcherSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ResearchViewSet(viewsets.ModelViewSet):
    queryset = models.Research.objects.all()
    serializer_class = serializers.ResearcherSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ResearchMemberViewSet(viewsets.ModelViewSet):
    queryset = models.ResearchMember.objects.all()
    serializer_class = serializers.ResearchMemberSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = models.Schedule.objects.all()
    serializer_class = serializers.ScheduleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LaboratoryViewSet(viewsets.ModelViewSet):
    queryset = models.Laboratory.objects.all()
    serializer_class = serializers.LaboratorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = models.Library.objects.all()
    serializer_class = serializers.LibrarySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
