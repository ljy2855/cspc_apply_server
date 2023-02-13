from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from apply.models import Recruitment
from apply.serializers import *
from swagger_response import *

#TODO
@swagger_auto_schema(method="get",responses=get_recuit_session_response)
@api_view(['GET'])
def get_recuit_session(request):
    session = get_object_or_404(Recruitment)
    serializer = RecruitSerializer(session)
    return Response(serializer.data, status=200)

