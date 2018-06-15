from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from features.models import Feature
 
@csrf_exempt
def paypal_return(request, feature):
    args = {'post': request.POST, 'get': request.GET, 'feature': feature}
    return render(request, 'paypal/paypal_return.html', args)
 
 
def paypal_cancel(request):
    args = {'post': request.POST, 'get': request.GET}
    return render(request, 'paypal/paypal_cancel.html', args)