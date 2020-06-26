from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView
from .models import Partners
# Create your views here.

class PartnersList(ListView):
    model = Partners
    template_name = 'relacionados/relacionados.html'
    paginate_by = 10