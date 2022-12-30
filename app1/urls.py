from django.urls import path
from .views import home,category,menu,product,cart,checkout,blog,aboutdetail,contactus,hotel,categoryflow,menuflow

urlpatterns = [
    path('',home,name="home"),
    path('category/',category,name="category"),
    path('category/<int:hotelid>',categoryflow,name="categoryflow"),
    path('menu/',menu,name="menu"),
    path('menu/<int:categoryid>',menuflow,name="menuflow"),
    path('product/<int:productid>',product,name="product"),
    path('cart/<int:cartid>',cart,name="cart"),
    path('checkout/',checkout,name="checkout"),
    path('blog/',blog,name="blog"),
    path('aboutdetail/',aboutdetail,name="aboutdetail"),
    path('contactus/',contactus,name="contactus"),
    path('hotel',hotel,name="hotel"),
]