from rest_framework_json_api import serializers
from jsonapi.models import User,ActivityPeriod

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('real_name','tz',)

class ActivityPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ('start_time','end_time','user_id')



