from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

# Create your views here.
def load_home(request):
    return render(request,'home.html')

def category_page(request):
    return render(request,'add_category.html')

def add_categorypage(request):
    if request.method == 'POST':
        crt_name= request.POST['cat_name']
        data = Category(Category_Name=crt_name)
        data.save()
        return redirect('load_home')
    
def product_page(request):
    cgt=Category.objects.all()
    ct={'cgts':cgt}
    return render(request,'add_products.html',ct)

def add_product(request):
    if request.method == 'POST':
        pname=request.POST['p_name']
        des=request.POST['p_des']  
        quality=request.POST['p_qutly'] 
        price=request.POST['p_price'] 
        cat=request.POST['select']
        cate=Category.objects.get(id=cat)
        datas=product_model(Product_Name=pname,Description=des, Quality=quality, price=price,Category=cate)
        datas.save()
        return redirect('load_home')


 
def show_details(request):
    products=product_model.objects.all()
    return render(request,'shows_details.html',{'prd':products})

def show_table(request):
    cate=Category.objects.all()
    prd=product_model.objects.all()
    return render(request,'show_table.html',{'cdata':cate,'pdata':prd})




