from rest_framework import serializers
from apply.models import *

class RecruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruitment
        fields = '__all__'
