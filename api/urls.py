from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('applications',views.CreateListAppViewSet)

urlpatterns = [
    path('',include(router.urls))
]