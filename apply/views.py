from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from apply.models import Recruitment
from apply.serializers import *
from swagger_response import *


from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

#TODO
@swagger_auto_schema(method="get",responses=get_recuit_session_response)
@api_view(['GET'])
def get_recuit_session(request):
    session = get_object_or_404(Recruitment)
    serializer = RecruitSerializer(session)
    return Response(serializer.data, status=200)

class ResumeAPI(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self,applicant):
        try:
            return Resume.objects.get(applicant=applicant)
        except Resume.DoesNotExist:
            return Http404
        
    @swagger_auto_schema(responses=get_resume_response)
    def get(self,request):
        resume = self.get_object(request.user)
        serializer = ResumeSerializer(resume)
        return Response(serializer.data, status=200)
    
    @swagger_auto_schema(request_body=ResumeSerializer,authentication_classes=[BasicAuthentication])
    def post(self,request):
        resume = Resume(applicant=request.user)
        serializer = ResumeSerializer(resume,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        else:
            return Response(serializer.errors,status=400) #지원서 수정하는데 잘못 save되면 응답 & status #


    @swagger_auto_schema(request_body=ResumeSerializer,authentication_classes=[BasicAuthentication])
    def put(self,request):
        resume = self.get_object(request.user)
        serializer = ResumeSerializer(resume,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        else:
            return Response(serializer.errors,status=400) #지원서 수정하는데 잘못 save되면 응답 & status #
    

