from django.shortcuts import render
from django.http import HttpResponse
from .myform import checkout_form
from .models import shopkeeper
from .models import category as category_table
from .models import product as product_table
from .models import cart as cart_table
import mysql.connector as con
from django.shortcuts import render
from json import dumps

db = con.connect(host="localhost",user="root",passwd="",database='foodies',port=3306)
print("Connection established....")
mycursor = db.cursor()
USER_ID = 1
SERVER_URL = 'http://127.0.0.1:8000/'
mycursor = db.cursor(dictionary=True)
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

def cart(req,productid):
    sql = f"Select c.*,c.id as 'cart_id',p.* from app1_cart c,app1_product p where c.userid= '%s' and c.productid=p.id and billid=0" ;
    values = [USER_ID]
    mycursor.execute(sql,values)
    table = mycursor.fetchall()
    print(table)
    dataJSON = dumps(table)
    return render(req,"cart.html",{'table':dataJSON})

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

def quantity_plus(req,qid):
    # table =[1,2,3,4,5]
    print(qid)
    table = cart_table.objects.filter(id=qid)
    table = table.values()
    print("this is table  ",table)
    current_quantity = table[0]['quantity']
    new_quantity = current_quantity + 1 
    print("current quantity is ",current_quantity)
    print("new quantity is ",new_quantity)
    sql = f"Update app1_cart set quantity= %s where id = %s"
    data = [new_quantity,qid]
    mycursor.execute(sql,data)
    return HttpResponse("Quantity added successfully")

def quantity_minus(req,qid):
    # table =[1,2,3,4,5]
    print(qid)
    table = cart_table.objects.filter(id=qid)
    table = table.values()
    print("this is table  ",table)
    current_quantity = table[0]['quantity']
    new_quantity = current_quantity - 1 
    print("current quantity is ",current_quantity)
    print("new quantity is ",new_quantity)
    sql = f"Update app1_cart set quantity= %s where id = %s"
    data = [new_quantity,qid]
    mycursor.execute(sql,data)
    return HttpResponse("Quantity subbed successfully")

def delete_cart(req,pid):
    sql = "Delete from app1_cart where id = %s";
    values = [pid]
    mycursor.execute(sql,values)
    print("value deleted successfully ");
    return HttpResponse("Quantity subbed successfully")

def add_to_cart(req,pid):
    print("this is cart ")
    sql = "Insert into app1_cart (productid,billid,userid,quantity) values (%s,%s,%s,%s) ";
    values = [pid,0,USER_ID,1]
    mycursor.execute(sql,values)
    return HttpResponse("this is add to cart ")