from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import OrderForm
# Create your views here.

from .models import * # أستدعاء جميع الكلاسات داخل الموديول 

def home(request):
    customers=Customer.objects.all()
    orders=Order.objects.all()
    Total_Order=orders.count()
    Total_customer=customers.count()
    count_pending_order=orders.filter(status='Pending').count()
    context={'customers':customers,
             'orders':orders,
             'Total_Order':Total_Order,
             'Total_customer':Total_customer,
             'count_pending_order':count_pending_order

             
             } #بيشيل أكل من اوبجيكت 
    return render(request,'bookstore/dashboard.html',context)

def books(request):
    books=Book.objects.all() # أستدعاء جميع بيانات الكتب 
    return render(request,'bookstore/books.html',{'books':books}) 

def customer(request,pk):
    customer=Customer.objects.get(id=pk)
    orders=customer.order_set.all()
    number_order=orders.count()
    context={'customer':customer,
             'orders':orders,
             'number_order':number_order,
             
             } 
    return render(request,'bookstore/customer.html',context)

def profile(request):
    return render(request,'bookstore/profile.html')


def create(request):
    form = OrderForm()
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('/')
       
    context={'form':form}
    return render(request,'bookstore/my_order_form.html',context)

