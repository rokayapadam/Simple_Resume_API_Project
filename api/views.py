from django.shortcuts import render
from .models import Profile
from .serializer import ProfileSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class ProfileCreateView(APIView):
    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msz':'Resume Uploaded Successfully', 'status':'success', 
            'candidate':serializer.data}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, format=None):
        candidate =  Profile.objects.all()
        serializer = ProfileSerializer(candidate, many=True)
        return Response({'status':'success', 'candidate':serializer.data}, status=status.HTTP_200_OK)
            