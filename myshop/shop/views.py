from unicodedata import category
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Category, Product
from cart.forms import CartAddProductForm
from .forms import SearchForm

def product_list(request):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})

def product_detail(request, id, slug):
    categories = Category.objects.all() 
    product = get_object_or_404(Product, id=id,
                                         slug=slug,
                                         )
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'categories': categories,
                   'cart_product_form': cart_product_form})

def search_view(request, category_slug=None):
    form = SearchForm()
    results = []
    query = ''
    categories = Category.objects.all()

    # Si hay un 'category_slug', filtrar los productos por esa categoría
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        results = Product.objects.filter(categoria=category)
    else:
        category = None  # Si no se pasa ninguna categoría

    # Si hay una consulta de búsqueda
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            # Filtrar productos por nombre, descripción o categoría
            results = Product.objects.filter(
                Q(nombre__icontains=query) | 
                Q(descripcion__icontains=query) | 
                Q(categoria__nombre__icontains=query)
            ).distinct()

    # Si no hay consulta de búsqueda ni categoría, redirigir a la lista de productos
    if not query and not category_slug:
        return redirect('shop:product_list')

    return render(request, 'shop/product/search.html', {
        'form': form,
        'query': query,
        'results': results,
        'categories': categories,
        'category': category  # Pasar la categoría seleccionada
    })

