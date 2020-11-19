from django.shortcuts import render
from django.http import HttpResponse

from math import ceil

from .models import Product

# Create your views here.
def home(request):
    products = Product.objects.all()

    n = len(products)
    nSlide = n//4 + ceil( (n/4) - (n//4) )

    allProds = []
    catProds = Product.objects.values('category' , 'id')
    cats = { item['category'] for item in catProds}

    for cat in cats:
        prod = Product.objects.filter(category = cat)
        allProds.append([ prod , range(1, nSlide) , nSlide ])

    # 1) params = {'no_of_slides' : nSlide , 'range':range(nSlide) , 'product':products}
    # allProds = [ [products ,range(1,nSlide) , nSlide] ,  [products ,range(1,nSlide) , nSlide] ]
    params = {'allProds' : allProds}
    # print(allProds)
    # print(allProds[1])
    #  print('nslide :', nSlide , 'n :',n)

    return render(request,'shop/home.html',params)


def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return HttpResponse('this s shop contact ')

def tracker(request):
    return HttpResponse('this s shop tracker')

def search(request):
    return HttpResponse('this s shop search')

def productview(request):
    return HttpResponse('this s shop productview')

def checkout(request):
    return HttpResponse('this s shop checkout')


