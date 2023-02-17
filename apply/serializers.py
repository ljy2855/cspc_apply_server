from rest_framework import serializers
from apply.models import *
from user.serializers import *
class RecruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruitment
        fields = '__all__'


class InterviewtimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewTime
        fields = '__all__'


class ResumeSerializer(serializers.ModelSerializer):
    interview_time_choice = InterviewtimeSerializer(many=True)
    class Meta:
        model = Resume
        fields = '__all__'

