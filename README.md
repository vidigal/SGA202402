# SGA202402
Sistema de gerenciamento acadêmico desenvolvido utilizando framework Django


# temp

# Estrutura do projeto:
# mensagens_projeto/
#   └── mensagens/
#       ├── __init__.py
#       ├── models.py
#       ├── forms.py
#       ├── views.py
#       ├── urls.py
#       └── templates/
#           └── mensagens/
#               ├── enviar_mensagem.html
#               └── lista_mensagens.html

# models.py
from django.db import models
from django.utils import timezone

class Mensagem(models.Model):
    texto = models.TextField()
    data_envio = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-data_envio']
    
    def __str__(self):
        return f"Mensagem de {self.data_envio.strftime('%d/%m/%Y %H:%M')}"

# forms.py
from django import forms
from .models import Mensagem

class MensagemForm(forms.ModelForm):
    class Meta:
        model = Mensagem
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'})
        }

# views.py
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import MensagemForm
from .models import Mensagem

def enviar_mensagem(request):
    if request.method == 'POST':
        form = MensagemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_mensagens')
    else:
        form = MensagemForm()
    return render(request, 'mensagens/enviar_mensagem.html', {'form': form})

def lista_mensagens(request):
    mensagens = Mensagem.objects.all()
    return render(request, 'mensagens/lista_mensagens.html', {'mensagens': mensagens})

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('enviar/', views.enviar_mensagem, name='enviar_mensagem'),
    path('', views.lista_mensagens, name='lista_mensagens'),
]

# templates/mensagens/enviar_mensagem.html
<!DOCTYPE html>
<html>
<head>
    <title>Enviar Mensagem</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <h1>Enviar Mensagem</h1>
        <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit" class="btn btn-primary">Enviar</button>
        </form>
        <a href="{% url 'lista_mensagens' %}" class="btn btn-secondary mt-3">Ver todas as mensagens</a>
    </div>
</body>
</html>

# templates/mensagens/lista_mensagens.html
<!DOCTYPE html>
<html>
<head>
    <title>Lista de Mensagens</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <h1>Mensagens</h1>
        <a href="{% url 'enviar_mensagem' %}" class="btn btn-primary mb-3">Nova Mensagem</a>
        
        {% for mensagem in mensagens %}
            <div class="card mb-3">
                <div class="card-body">
                    <p class="card-text">{{ mensagem.texto }}</p>
                    <small class="text-muted">{{ mensagem.data_envio|date:"d/m/Y H:i" }}</small>
                </div>
            </div>
        {% empty %}
            <p>Nenhuma mensagem ainda.</p>
        {% endfor %}
    </div>
</body>
</html>
