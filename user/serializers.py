from rest_framework import serializers

from user.models import LabMaster

class LabMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabMaster
        fields = ('name','email','phone')
