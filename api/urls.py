from django.urls import path, include
from .views import ApplicationsViewSet, api_root

applications_list = ApplicationsViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
    path('', api_root),
    path('applications',applications_list, name="applications-list"),
]

