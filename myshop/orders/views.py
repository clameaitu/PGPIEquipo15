from django.urls import reverse
from django.shortcuts import render, redirect
from shop.models import Category, Product
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.shortcuts import render, get_object_or_404
from orders.models import Order
from django.http import Http404 


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save() # aquí se guarda el pedido
            for item in cart:
                OrderItem.objects.create(order=order,
                                        producto=item['product'],
                                        precio=item['price'],
                                        cantidad=item['quantity'])
            # clear the cart
            cart.clear()
            
            # set the order in the session
            request.session['order_id'] = order.id
            
            # redirect for payment
            action = request.POST.get('payment_action')
            if action == "Pagar ahora":
                return redirect(reverse('payment:process'))
            elif action == "Pagar al recibir":
                return redirect(reverse('payment:in_person'))
            
    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})


def buscar_pedido(request):
    codigo = request.GET.get('codigo')  # Obtener el código de la query string

    # Obtener productos y categorías para renderizar en la plantilla
    categories = Category.objects.all()
    products = Product.objects.all()

    if codigo:
        try:
            # Intentamos obtener el pedido por el código
            order = Order.objects.get(codigo=codigo)
            items = order.items.all()

            # Calcular el total por producto
            for item in items:
                item.total = item.precio * item.cantidad

            # Redirigir a la página de detalles del pedido si el código es válido
            return render(request, 'shop/detalles_pedido.html', {
                'order': order,
                'items': items
            })
        except Order.DoesNotExist:
            # Si no se encuentra el pedido, mostramos la página list.html con un mensaje de error
            error_message = "El código no es correcto, por favor, introduzca un código válido."
            return render(request, 'shop/product/list.html', {
                'categories': categories,
                'products': products,
                'mensaje_error': error_message
            })
    else:
        # Si no se ha introducido ningún código, mostramos la página list.html sin mensaje de error
        return render(request, 'shop/product/list.html', {
            'categories': categories,
            'products': products
        })


def detalles_pedido(request, codigo):
    try:
        # Obtener el pedido por el código
        order = Order.objects.get(codigo=codigo)
        
        # Obtener los items del pedido
        items = order.items.all()

        # Calcular el total por producto
        for item in items:
            item.total = item.precio * item.cantidad
        
        # Calcular el total para el pedido completo
        total = sum(item.total for item in items)

        return render(request, 'shop/detalles_pedido.html', {
            'order': order,
            'items': items,
            'total': total  # Pasamos el total al template
        })
    except Order.DoesNotExist:
        # Si el pedido no existe, redirigir a la página de perfil con un mensaje de error
        return redirect('account:dashboard', mensaje_error="El código no es correcto, por favor, introduzca un código válido.")
