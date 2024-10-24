from django.urls import path

from .views import IndexView, TesteView, ContatoView, SobreView, CursoView, ProfessorView
from rest_framework.routers import SimpleRouter


router = SimpleRouter()

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('curso', CursoView.as_view(), name='curso'),
    path('professor', ProfessorView.as_view(), name='professor'),

    path('teste', TesteView.as_view(), name='teste'),
    path('sobre', SobreView .as_view(), name='sobre'),
    path('contato', ContatoView.as_view(), name='contato'),
]