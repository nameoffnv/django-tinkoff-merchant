import django.dispatch

payment_update = django.dispatch.Signal(providing_args=['payment'])
