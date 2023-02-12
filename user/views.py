from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from models import Applicant
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

@api_view(['POST'])
def check_applicant(request):
    try:
        #request에서 이름, 패스워드 추출
        name = request.data['name']
        password = request.data['password']


        applicant = Applicant.objects.get(name=name,password=password)
        # 기존 지원자 로그인 성공
        return Response(status=201)

    # request에서 이름, 패스워드 추출 실패 시
    except AttributeError: 
        return Response(status=404)
    
    # 이름, 패스워드로 검색 실패 시
    except ObjectDoesNotExist:
        # 기존 지원자가 로그인 실패
        if Applicant.objects.filter(name=name):
            return Response(status=500)
        # 새로운 지원자
        else:
            Applicant.objects.create(name=name,password=password)
            return Response(status=200)

# Create your views here.
