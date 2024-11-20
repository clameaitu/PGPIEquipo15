from django.urls import reverse
from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
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