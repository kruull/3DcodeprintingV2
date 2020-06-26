from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Comentario
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, TemplateView, CreateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Q, Max, Min
from django.core.paginator import Paginator


# Create your views here.
"""
def products(request):
    categoryList = Category.objects.all()
    Products = Product.objects.all()
    
    return render(request,'products/products.html', {'Products':Products,'categoryList':categoryList})

"""

def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    ProductList = category.get_posts.all()
    paginator = Paginator(ProductList, 12)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    Pages=[]
    for i in range(paginator.num_pages):
        Pages.append(i+1)
        print("meto {}".format(i))
    
    print(paginator.num_pages)
    print(Pages)
    return render(request, 'products/category.html', {'page_obj': page_obj,'Pages': Pages,'CategoriaProductos':category})



#Clase categoria--> Funciona
class CategoryView(ListView):
    model = Category
    template_name = 'products/products.html'
    paginate_by = 6

#Clase producto --> funciona
class ProductDetail(DetailView):
    template_name = 'products/detail.html'
    model = Product

class ComentarioProducto(CreateView):
    template_name = 'products/detail.html'
    model = Comentario
    fields = ('comentario','usuario','producto',)
    

    def get_success_url(self):
        
        return "/products/detalle_producto/{}/".format(self.object.producto.pk)



class ListadoProducto(ListView):
    template_name = 'products/buscador.html'
    model = Product
    paginate_by = 12
    

    def get_queryset(self):
        query = None
        
        if ('nombre' in self.request.GET) and self.request.GET['nombre'] != "":
            query = Q(title__icontains=self.request.GET["nombre"])
            

        """        
        if ('maximo' in self.request.GET) and self.request.GET['maximo'] != "":
            try:
                if query == None:
                    query = Q(price__lte=int(float(self.request.GET['maximo'])))
                else:
                    query = query & Q(price__lte=int(float(self.request.GET['maximo'])))
            except:
                pass


        if ('minimo' in self.request.GET) and self.request.GET['minimo'] != "":
            try:
                if query == None:
                    query = Q(price__lte=int(float(self.request.GET['minimo'])))
                else:
                    query = query & Q(price__lte=int(float(self.request.GET['minimo'])))
            except:
                pass
        
        """
        if query is not None:
            productos = Product.objects.filter(query)
            print(productos)
            
            print(query)
        else:
            productos = Product.objects.all()
            print(query)
            
        return productos
    
    def get_context_data(self, **kwargs):
        context = super(ListadoProducto, self).get_context_data(**kwargs)
        """
        context['maximo'] = Product.objects.all().aggregate(Max('price'))['price__max']
        context['minimo'] = Product.objects.all().aggregate(Min('price'))['price__min']
        """
        return context
    

