from django.shortcuts import render, redirect
from .models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request, sort_type=None):
    template = 'catalog.html'
    sort = str(request.GET.get('sort'))
    if sort == 'name':
        sort_type = 'name'
        context = {
            'phones': Phone.objects.order_by(sort_type)
        }
        return render(request, template, context)
    elif sort == 'min_price':
        sort_type = 'price'
        context = {
            'phones': Phone.objects.order_by(sort_type)
        }
        return render(request, template, context)
    elif sort == 'max_price':
        sort_type = 'price'
        context = {
            'phones': reversed(Phone.objects.order_by(sort_type))
        }
        return render(request, template, context)
    else:
        context = {
        'phones': Phone.objects.all()
        }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
