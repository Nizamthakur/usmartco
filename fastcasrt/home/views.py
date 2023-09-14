from django.shortcuts import render
from home import models
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    products_objects= models.product.objects.all()
    item_name = request.GET.get('item_name')
    if(item_name!=''and item_name is not None):
        products_objects = products_objects.filter(title__icontains = item_name)
    return render(request,'index.html',{'products_objects':products_objects})

@login_required
def shop(request):
    shopProduct = models.product.objects.all()
    return render(request,'shop.html',{"shopProduct":shopProduct})
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def blog(request):
    blog_objects = models.blog.objects.all()
    return render(request,'blog.html',{"blog_objects":blog_objects})
def contact(request):
    return render(request,'contact.html')
def user(request):
    return render(request,'user.html')
def cart(request):
    return render(request,'cart.html')
def viewProduct(request,pk):
    product = models.product.objects.get(id = pk)
    return render(request,'viewProduct.html',{"product":product})
def purchase(request):
    return render(request,'purchase reply.html')
def contactReply(request):
    return render(request,'thankyou.html')
def blogDetails(request,pk):
    blogDetails = models.blog.objects.get(id = pk)
    return render(request,'blogDetails.html',{"blogDetails":blogDetails})