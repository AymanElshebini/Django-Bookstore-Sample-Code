from django.urls import path
from . import views
urlpatterns = [
   path('', views.home,name="home"),
   path('books/', views.books,name="books"),
   path('customer/<str:pk>',views.customer,name="customer"),
   path('create/',views.create,name="create"),
   path('profile/',views.profile)
]