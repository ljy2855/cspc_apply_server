from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from apply.models import Recruitment, Resume
from apply.serializers import *
from swagger_response import *
from django.core.exceptions import ObjectDoesNotExist

#TODO
@swagger_auto_schema(method="get",responses=get_recuit_session_response)
@api_view(['GET'])
def get_recuit_session(request):
    session = get_object_or_404(Recruitment)
    serializer = RecruitSerializer(session)
    return Response(serializer.data, status=200)
 

@api_view(['GET','POST','PUT'])
def api_resume(request):
    try:
        #request에서 이름, 패스워드 추출
        name = request.data['name']
        password = request.data['password']
        applicant = Applicant.objects.get(name=name,password=password)
        resume = Resume.objects.get(applicant=applicant) #id/pw에 맞는 지원서
    
    except AttributeError: #request에서 이름, 패스워드 추출 실패 시
        return Response(status=400)
    
    except ObjectDoesNotExist: #api POST 부분 , 새 지원서 작성
        if request.method == 'POST':
            serializer = ResumeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = 200)
            else :
                return Response(serializer.errors,status=400) # serializer가 문제 있으면 status? #


    if request.method == 'GET': #기존 지원서 조회
        serializer = ResumeSerializer(resume)
        return Response(serializer.data, status=200)


    elif request.method == 'PUT': #기존 지원서 불러온 뒤 수정
        serializer = ResumeSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        else:
            return Response(serializer.errors,status=400) #지원서 수정하는데 잘못 save되면 응답 & status #



