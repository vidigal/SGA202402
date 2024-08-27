from django.urls import path

from .views import IndexView
from rest_framework.routers import SimpleRouter


router = SimpleRouter()

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]