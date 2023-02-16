from rest_framework import serializers
from apply.models import *

class RecruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruitment
        fields = '__all__'

class InterviewtimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewTime
        fields = '__all__'


class ResumeSerializer(serializers.ModelSerializer):
    Interviewtime = InterviewtimeSerializer()
    
    class Meta:
        model = Resume
        fields = '__all__'