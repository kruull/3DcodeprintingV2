from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Partners(models.Model):
    name = models.CharField(max_length=200, verbose_name="Título")
    content = RichTextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen", upload_to="Partnerts", null=True, blank=True)
    url = models.URLField(verbose_name="Enlace", max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = "enlace"
        verbose_name_plural = "enlaces"
        ordering = ['name']

    def __str__(self):
        return self.name