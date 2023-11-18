from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from math import ceil
# Create your views here.
def index(request):
    # products = Product.objects.all()
    # n = len(products)
    # nSlides = n//4+ ceil((n/4)-(n//4)) 
    # # params = {'no_of_slides':nSlides, 'range':range(1,nSlides), 'product':products}
    # allprods = [
    #     [products, range(1,nSlides), nSlides],
    #     [products, range(1,nSlides), nSlides]
    products= Product.objects.all()
    allProds=[]
    catprods= Product.objects.values('category', 'id')
    cats= {item["category"] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

                
    params = {'allprods':allProds}
    return render(request,"shop/mainpage.html",params)    
def Home(request):
    return HttpResponse("This is home page")
def Contact(request):
    return HttpResponse("This is Contact page")
def About(request):
    return HttpResponse("This is about me ")

def post_list(request):
    posts = Product.objects.all()
    return render(request, 'shop/display.html', {'posts': posts})
