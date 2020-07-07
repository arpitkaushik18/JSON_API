from jsonapi.models import User, ActivityPeriod
from jsonapi.serializers import UserSerializer, ActivityPeriodSerializer
from rest_framework import viewsets
from drf_multiple_model.views import ObjectMultipleModelAPIView


from drf_multiple_model.viewsets import ObjectMultipleModelAPIViewSet

class TextAPIView(ObjectMultipleModelAPIViewSet):
    querylist = (
        {'queryset': User.objects.all(), 'serializer_class': UserSerializer},
        {'queryset': ActivityPeriod.objects.all(), 'serializer_class': ActivityPeriodSerializer},
    )
    serializer_class = UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ActivityPeriodViewSet(viewsets.ModelViewSet):
    queryset = ActivityPeriod.objects.all()
    serializer_class = ActivityPeriodSerializer