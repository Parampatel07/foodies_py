from django.urls import path
from .views import home,category,menu,product,cart,checkout,blog,aboutdetail,contactus,hotel,categoryflow,menuflow,quantity_plus,quantity_minus,delete_cart

urlpatterns = [
    path('',home,name="home"),
    path('category/',category,name="category"),
    path('category/<int:hotelid>',categoryflow,name="categoryflow"),
    path('menu/',menu,name="menu"),
    path('menu/<int:categoryid>',menuflow,name="menuflow"),
    path('product/<int:productid>',product,name="product"),
    path('cart/<int:productid>',cart,name="cart"),
    path('checkout/',checkout,name="checkout"),
    path('blog/',blog,name="blog"),
    path('aboutdetail/',aboutdetail,name="aboutdetail"),
    path('contactus/',contactus,name="contactus"),
    path('hotel',hotel,name="hotel"),
    path('update_quantity_plus/<int:qid>',quantity_plus,name="update_quantity_plus"),
    path('update_quantity_minus/<int:qid>',quantity_minus,name="update_quantity_minus"),
    path('delete_cart/<int:pid>',delete_cart,name="delete_cart"),
]