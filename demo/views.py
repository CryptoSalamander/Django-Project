from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from demo.models import Item, User
from django.views.decorators.csrf import csrf_exempt
import random


# Create your views here.
def index(request):
    items = Item.objects.all( )
    context = {'items': items}
    return render( request, 'demo/index.html', context )


def showitem(request, number):
    item = Item.objects.get( item_number=number )
    item.viewnum += 1
    item.save( )
    return HttpResponseRedirect( "/items/{}/info".format( item.item_number ) )


def info(request, number):
    items = Item.objects.get( item_number=number )
    context = {'items': items}
    return render( request, 'demo/info.html', context )


def buy(request, number):
    items = Item.objects.get( item_number=number )
    context = {'items': items}
    return render( request, 'demo/buy.html', context )


def done(request, number):
    items = Item.objects.get( item_number=number )
    items.buynum += 1
    items.save( )
    items.parcelnum = random.randint( 100000, 999999 )
    context = {'items': items}
    return render( request, 'demo/done.html', context )


def pay(request, number):
    items = Item.objects.get( item_number=number )
    context = {'items': items}
    return render( request, 'demo/pay.html', context )


def card(request, number):
    items = Item.objects.get( item_number=number )
    context = {'items': items}
    return render( request, 'demo/card.html', context )


def cash(request, number):
    items = Item.objects.get( item_number=number )
    context = {'items': items}
    return render( request, 'demo/cash.html', context )


def register(request):
    users = User.objects.all()
    context = {'users' : users}
    return render( request, 'demo/register.html',context )


def loginpage(request):
    return render( request, 'demo/loginpage.html' )


def login(request):
    return render(request, 'demo/loginpage.html')

def select(request):
    return render(request, 'demo/selectpage.html')

def registerdone(request):
        user = User(
            username=request.POST.get( 'ID', False ),
            last_name=request.POST.get( 'NAME', False ),
            email=request.POST.get( 'EMAIL', False )
        )
        user.set_password(request.POST.get('PWD',False))
        user.save()
        return render(request,'demo/registerdone.html')

