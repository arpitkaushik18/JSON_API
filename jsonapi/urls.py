from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()

router.register('User',views.UserViewSet,basename='User')
router.register('texts', views.TextAPIView, basename='texts')
router.register('ActivityPeriod',views.ActivityPeriodViewSet)

urlpatterns = [

  url(r'',include(router.urls))
]