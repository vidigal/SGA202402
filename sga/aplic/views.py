from django.views.generic import TemplateView

from .models import Curso


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['cursos'] = Curso.objects.order_by('-nome').all()
        return context


class CursoView(TemplateView):
    template_name = 'curso.html'

    def get_context_data(self, **kwargs):
        context = super(CursoView, self).get_context_data(**kwargs)
        return context

class CursoDetalheView(TemplateView):
    template_name = 'curso_detalhe.html'

    def get_context_data(self, **kwargs):
        context = super(CursoDetalheView, self).get_context_data(**kwargs)
        id = self.kwargs['id']
        context['curso'] = Curso.objects.filter(id=id).first
        return context

class ProfessorView(TemplateView):
    template_name = 'professor.html'

    def get_context_data(self, **kwargs):
        context = super(ProfessorView, self).get_context_data(**kwargs)
        return context

class TesteView(TemplateView):
    template_name = 'teste.html'

    def get_context_data(self, **kwargs):
        context = super(TesteView, self).get_context_data(**kwargs)
        return context

class SobreView(TemplateView):
    template_name = 'sobre.html'

    def get_context_data(self, **kwargs):
        context = super(SobreView, self).get_context_data(**kwargs)
        return context

class ContatoView(TemplateView):
    template_name = 'contato.html'

    def get_context_data(self, **kwargs):
        context = super(ContatoView, self).get_context_data(**kwargs)
        return context