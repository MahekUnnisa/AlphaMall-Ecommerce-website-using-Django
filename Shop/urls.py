from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Home"),
    path("about", views.about, name="AboutUs"),
    path("contact", views.contact, name="ContactUs"),
     path("register", views.handleRegister, name="handlerRegister"),
    path("login",views.handleLogin, name='handleLogin' ),
    path("logout",views.handleLogout, name='handleLogout' ),
    path("search", views.search, name="Search"),
    path("tracker", views.tracker, name="Tracker"),
    path("product", views.productView, name="ProductView")
]