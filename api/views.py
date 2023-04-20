from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
#import JsonResponse
from django.http import JsonResponse

import pickle
import cv2
import numpy as np
import cvzone

from api.parkingSpacePicker import Main
from api.main import CVLogic
# Create your views here.

class ApiOverview(APIView):
    def get(self, request):
        api_urls = {
            'List':'/parking-list/',
            'Detail View':'/parking-detail/<str:pk>/',
            'Create':'/parking-create/',
            'Update':'/parking-update/<str:pk>/',
            'Delete':'/parking-delete/<str:pk>/',
        }
        return Response(api_urls)
    
class ParkingDetection(APIView):
    def get(self, request,pk):
        # Main()
        ans = CVLogic(sec=pk)
        return JsonResponse({"ans":ans});