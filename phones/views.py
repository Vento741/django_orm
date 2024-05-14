from django.shortcuts import render, redirect, get_object_or_404
from . models import Phone



def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_param = request.GET.get('sort', 'name')
    if sort_param == 'min_price':
        phones = Phone.objects.all().order_by('price')
    elif sort_param == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    else:  # 'name' или любой другой параметр
        phones = Phone.objects.all().order_by('name')
    return render(request, 'catalog.html', {'phones': phones})


def show_product(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    return render(request, 'product.html', {'phone': phone})