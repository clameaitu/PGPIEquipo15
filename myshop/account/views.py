from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from orders.models import Order
from shop.models import Category
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required

def user_login(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                email=cd['email'],
                password=cd['contraseña']
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    return HttpResponse('Cuenta deshabilitada')
            else:
                return HttpResponse('Inicio de sesión incorrecto')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form, 'categories': categories,})

@login_required
def dashboard(request):
    categories = Category.objects.all()
    codigo = request.GET.get('codigo', '')
    order = None
    mensaje_error = None

    if codigo:
        try:
            # Verificar si el código existe
            order = Order.objects.get(codigo=codigo)
            # Redirigir a la página de detalles del pedido si el código es correcto
            return redirect(reverse('orders:detalles_pedido', kwargs={'codigo': order.codigo}))
        except Order.DoesNotExist:
            # Si el código no existe, mostrar un mensaje de error
            mensaje_error = "El código no es correcto, por favor, introduzca un código válido."

    return render(request, 'account/dashboard.html', {
        'mensaje_error': mensaje_error, 'categories': categories,
    })


def register(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            # Save the User object
            new_user.save()
            return render(
               request,
               'account/register_done.html',
               {'new_user': new_user, 'categories': categories,}
           )
    else:
        user_form = UserRegistrationForm()
    return render(
        request,
        'account/register.html',
        {'user_form': user_form, 'categories': categories,}
    )