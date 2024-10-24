from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context

class CursoView(TemplateView):
    template_name = 'curso.html'

    def get_context_data(self, **kwargs):
        context = super(CursoView, self).get_context_data(**kwargs)
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