from django.urls import path
from . import views
from .views import PartnersList


urlpatterns = [

    #productos
    path('',PartnersList.as_view(),name='partners'),

]