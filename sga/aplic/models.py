import uuid

from django.db import models
from stdimage.models import StdImageField
from django.utils.translation import gettext_lazy as _

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

# Create your models here.
class Curso(models.Model):
    nome = models.CharField(_('Nome'), max_length=100)
    descricao = models.TextField(_('Descrição'), max_length=500)
    carga_horaria = models.IntegerField(_('Carga Horária'))
    imagem = StdImageField(_('Imagem'), null=True, blank=True, upload_to=get_file_path, variations={'thumb': {'width': 420, 'height': 260, 'crop': True}})


    class Meta:
        verbose_name = _('Curso')
        verbose_name_plural = _('Cursos')

    def __str__(self):
        return self.nome
