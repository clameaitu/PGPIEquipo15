import braintree
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from orders.models import Order
from payment.email import EmailService

#email = os.getenv('EMAIL')
#password = os.getenv('EMAIL_PASS')
email_service = EmailService("esotericagrupo15@gmail.com", "rfeu bnhl blpe gdai")

# instantiate Braintree payment gateway
gateway = braintree.BraintreeGateway(settings.BRAINTREE_CONF)
msg = "Prueba"

def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    total_cost = order.get_total_cost()
    if request.method == 'POST':
        # retrieve nonce
        nonce = request.POST.get('payment_method_nonce', None)
        # create and submit transaction
        result = gateway.transaction.sale({
            'amount': f'{total_cost:.2f}',
            'payment_method_nonce': nonce,
            'options': {
                'submit_for_settlement': True
            }
        })
        if result.is_success:
            # mark the order as paid
            order.paid = True
            # store the unique transaction id
            order.braintree_id = result.transaction.id
            order.save()
            email_service.send_mail(order.email, email_service.build_msg(order), "Compra Realizada")
            return redirect('payment:done')
        else:
            return redirect('payment:canceled')
    else:
        # generate token
        client_token = gateway.client_token.generate()
        return render(request,
                      'payment/process.html',
                      {'order': order,
                       'client_token': client_token})


def payment_done(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'payment/done.html', {'order': order})



def payment_canceled(request):
    return render(request, 'payment/canceled.html')


def payment_in_person(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    email_service.send_mail(order.email, email_service.build_msg(order), "Compra Realizada")
    return render(request, 'payment/done_no_card.html', {'order': order})