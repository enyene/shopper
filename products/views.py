from django.shortcuts import render
from .models import Product
from scraper import asos,ebay,jumia,payporte,konga
import random

# Create your views here.

def product_list(request):
    if request.GET.get('search'):
        q = request.GET.get('search')
        products = []
        #products.extend(asos.asos_scraper_bot(q))
        #products.extend(ebay.ebay_scraper_bot(q))
        products.extend(jumia.jumia_scraper_bot(q))
        products.extend(konga.konga_scraper_bot(q))
        #products.extend(payporte.payporte_scraper_bot(q))
        random.shuffle(products)

        objects = Product.objects.create(title=products[0]['title'], price=products[0]['price'], vendor=products[0]['from'])
        objects.save()
        return render(request, 'products/product_list.html', {'products': products})
    else:
        products = Product.objects.all()
        return render(request, 'products/product_list.html', {'products': products})
