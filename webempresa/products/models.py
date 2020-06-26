from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    image = models.ImageField(verbose_name="Imagen", upload_to="products", null=True, blank=True)
    
    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
        ordering = ['-created']

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to="products", null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categorías", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")  
    price = models.CharField(max_length=20, verbose_name="Precio")  

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ['-created']

    def __str__(self):
        return self.title

class ImagenesProducto(models.Model):
    Product = models.ForeignKey(Product, related_name="producto_imagenes",on_delete=models.CASCADE)
    image = models.ImageField(upload_to='imagenes_producto')

    def __str__(self):
        return "Imagen de producto:{}".format(self.Product)

class Comentario(models.Model):
    comentario = models.CharField(max_length=300)
    usuario = models.CharField(max_length=300)
    fecha = models.DateTimeField(auto_now_add=True)
    producto = models.ForeignKey(Product, related_name="producto_comentarios",on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.comentario, self.producto)