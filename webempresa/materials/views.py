from django.shortcuts import render
from .models import Material


# Create your views here.


def materials(request):
    materials = Material.objects.all()
    return render(request, "materials/materials.html", {'materials':materials})