from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from apply.models import Recruitment

#TODO
@api_view(['GET'])
def get_recuit_session():
    session = get_object_or_404(Recruitment)

