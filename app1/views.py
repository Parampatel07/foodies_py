from django.shortcuts import render
from django.http import HttpResponse
from .myform import checkout_form
from .models import shopkeeper
from .models import category as category_table
from .models import product as product_table
import mysql.connector as con
db = con.connect(host="localhost",user="root",passwd="",database='foodies',port=3306)
print("Connection established....")

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
    count=1
    # mytables=[]
    # while count<=4:
    #     answer=category_table.objects.filter(shopkeeperid=hotelid,blds=count).values()
    #     mytables.append(answer[0])
    #     # print(answer[0]) 
    #     count+=1
    # # print(mytables)
    # breakfast_table = mytables.objects.filter(blds=1)
    # print(breakfast_table)
    # mytable= divide_parts(table,3)
    breakfast_table=category_table.objects.filter(shopkeeperid=hotelid,blds=1)
    lunch_table=category_table.objects.filter(shopkeeperid=hotelid,blds=2)
    dinner_table=category_table.objects.filter(shopkeeperid=hotelid,blds=3)
    snack_table=category_table.objects.filter(shopkeeperid=hotelid,blds=4)
    return render(req,"categories.html",{"breakfast_table":breakfast_table,"lunch_table":lunch_table,"snack_table":snack_table,"dinner_table":dinner_table})

def menu(req):
    # return HttpResponse("this is menu page")
    return render(req,"menu.html")

def menuflow(req,categoryid):
    # return HttpResponse("this is menu page")
    sql=f"SELECT p.*,c.blds from app1_product p,app1_category c where p.categoryid={categoryid} and c.id=p.categoryid ;"
    # table= {}
    # table = product_table.objects.raw(sql,translations=table)
    # print(table)
    mycursor = db.cursor(dictionary=True)
    mycursor.execute(sql)
    table = mycursor.fetchall()
    blds_name=""
    if table[0]['blds']==1:
        blds_name = "Breakfast"
    elif table[0]['blds']==2:
        blds_name="Lunch"
    elif table[0]['blds']==3:
        blds_name="Dinner"
    elif table[0]['blds']==4:
        blds_name="Snack"
    print(table)
    print(blds_name)
    
    return render(req,"menu.html",{'table':table,'blds_name':blds_name})

def product(req,productid):
    table=product_table.objects.filter(id=productid).values()
    mytable=[]
    for i in table:
        mytable.append(i)
    print(mytable)
    
    return render(req,"product.html",{'mytable':mytable});

def cart(req,cartid):
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
    # mytable = list(divide_parts(table,3))
    # print("this is mytable ",mytable)
    return render(req,"hotel.html",{"table":table})