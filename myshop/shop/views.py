from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Category, Product
from cart.forms import CartAddProductForm
from .forms import SearchForm

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(categoria=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id,
                                         slug=slug,
                                         )
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})

def search_view(request):
    form = SearchForm()
    results = []
    query = ''

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            # Filtrar productos por nombre, categoría (relacionada) y descripción
            results = Product.objects.filter(
                Q(nombre__icontains=query) | 
                Q(descripcion__icontains=query) | 
                Q(categoria__nombre__icontains=query)
            ).distinct()  # .distinct() para evitar duplicados si un producto coincide en varias categorías
    if not query:  # If no query, redirect to product list view
        return redirect('shop:product_list')

    return render(request, 'shop/product/search.html', {
        'form': form,
        'query': query,
        'results': results
    })