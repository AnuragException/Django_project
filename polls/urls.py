from django.urls import path,include

from . import views
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('join_api/<int:pk>/',views.join_api)

urlpatterns = [
    # path('', include(router.urls)),
    path('join_api/',views.join_api.as_view()),
    path('join_api/<int:pk>/',views.join_api.as_view()),
]

