from django.shortcuts import render
from .models import Product
from scraper import asos,ebay,jumia,payporte,konga
from .forms import comment,UserForm
from django.http import HttpResponse
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

def UserView(request):
    registered=False
    if request.method=='POST':
        form=UserForm(data=request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponse('You have Succefully Registered')
           
        else:
            print(form.errors)
    else:
        form=UserForm()       
    return render(request,'products/signup.html',{'show':form,'registered':registered})
