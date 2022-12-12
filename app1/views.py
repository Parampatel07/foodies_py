from django.shortcuts import render
from django.http import HttpResponse
from .myform import checkout_form
from .models import shopkeeper
from .models import category as category_table

# <---=========================== start of my functions ============================================--->
def divide_parts(name_of_list, size_of_part):
    # looping till length l
    for i in range(0, len(name_of_list), size_of_part):
        yield name_of_list[i:i + size_of_part]
    # mylist= list(divide_parts(number,3))
    # print("this is my list ",mylist) 
    # return mylist


# <---=========================== end of  my functions ============================================--->


# Create your views here.
def home(req):
    return render(req,"index-2.html")
    # return HttpResponse("this is home page ")

def category(req):
    return render(req,"categories.html")

def categoryflow(req,hotelid):
    table = category_table.objects.filter(id=hotelid).values()
    print(table)
    
    return render(req,"categories.html",{"table":table})

def menu(req):
    # return HttpResponse("this is menu page")
    return render(req,"menu.html")

def product(req):
    return render(req,"product.html")

def cart(req):
    return render(req,"cart.html")    

def checkout(req):
    my_checkout_form = checkout_form
    return render(req,"checkout.html",{"my_checkout_form":my_checkout_form})

def blog(req):
    return render(req,"blog.html")

def aboutdetail(req):
    return render(req,"aboutdetail.html")

def contactus(req):
    return render(req,"contactus.html")

def hotel(req):
    table = shopkeeper.objects.filter().values()
    mytable = list(divide_parts(table,3))
    print("this is mytable ",mytable)
    return render(req,"hotel.html",{"table":mytable})