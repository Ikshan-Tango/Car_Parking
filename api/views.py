from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

#import JsonResponse
from django.http import JsonResponse

from api.openCv.parkingSpacePicker import Main
from api.openCv.main import CVLogic
# Create your views here.

from .serializers import *

class ApiOverview(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request):
        api_urls = {
            'List':'/parking-list/',
            'Detail View':'/parking-detail/<str:pk>/',
            'Create':'/parking-create/',
            'Update':'/parking-update/<str:pk>/',
            'Delete':'/parking-delete/<str:pk>/',
        }
        return Response(api_urls)
    
class HomeView(APIView):
     
   permission_classes = (IsAuthenticated, )
   def get(self, request):
        content = {'message': 'Welcome to the JWT Authentication page using React Js and Django!'}
        return Response(content)
    
class Register(APIView):
    def post(self,request):
        data = request.data
        user_serializer = UserSerializer(data = data)

        password = request.data['password']
        password = make_password(password=password) #it is used to hash the incoming password

        #if valid then make the user and assign a token
        if user_serializer.is_valid():
            user  = user_serializer.save(password=password)

        #else raise an error 
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        #return the response

        return Response({
            "user": user_serializer.data,
            "message":"user created successfully!"
        }, status=status.HTTP_201_CREATED)
    
class SignIn(APIView):
    def post(self, request):
        print(request.data)
        data = request.data
        #match if the corresponsding data exists already in the db then sign in and provide with a token
        return Response(request.data)
    
class LogoutView(APIView):
     permission_classes = (IsAuthenticated,)
     def post(self, request):
          
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message":"Token deleted successfully!"},status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error":e},status=status.HTTP_400_BAD_REQUEST)

    
class ParkingDetection(APIView):
    def get(self, request,pk):
        # Main()
        ans = CVLogic(sec=pk)
        return JsonResponse({"ans":ans});