from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Material(models.Model):
    title = models.CharField(max_length=200, verbose_name="Material")
    Description = RichTextField(verbose_name="Descipción")
    image = models.ImageField(verbose_name="Imagen", upload_to="materials")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")



    class Meta:
        verbose_name = "material"
        verbose_name_plural = "materiales"
        ordering = ['order','title']


    def __str__(self):
        return self.title
