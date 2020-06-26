from django.urls import path
from . import views
from .views import ListadoProducto, CategoryView, ProductDetail, ComentarioProducto


urlpatterns = [

    #productos
    path('',CategoryView.as_view(),name='products'),

    path('detalle_producto/<int:pk>/',ProductDetail.as_view(),name='detalle_productos'),

    
    path('category/<int:category_id>/', views.category, name="category"),

    path('crear_comentario/',ComentarioProducto.as_view(),name='crear_comentario'),
    path('buscador/',ListadoProducto.as_view(),name='buscador'),


]