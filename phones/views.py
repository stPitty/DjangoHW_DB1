from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort')
    template = 'catalog.html'
    phones = Phone.objects.all()
    if sort in phones[0].__dict__:
        phones = phones.order_by(sort)
    else:
        if sort == 'min_price':
            phones = phones.order_by('price')
        elif sort == 'max_price':
            phones = phones.order_by('-price')
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)
