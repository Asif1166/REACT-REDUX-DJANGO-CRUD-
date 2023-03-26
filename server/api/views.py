from django.shortcuts import render, HttpResponse
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProjectSerializer
from rest_framework import viewsets
# Create your views here.
def home(request):
    return HttpResponse('this is home')



class getProjects(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
