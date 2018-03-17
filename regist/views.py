from django.shortcuts import render
from regist.models import Person
from django.http import HttpResponse, HttpResponseNotFound
from regist.forms import PersonSave
from django.template import Context
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
# noinspection PyInterpreter

def index(request):
    try:
        context = Context({'name': 'forms',
                           'var1': 'var1',
                           'var2': 'var2',
                           'var3': 'var3',
                           'form': PersonSave()
                           })
        return render(request, 'regist/index.html', context)
    except:
        return HttpResponseNotFound

@csrf_exempt
def form(request):
    person = Person(
        name = request.POST.get('nameField', False),
        person_number = request.POST.get('person_number', False),
        mail = request.POST.get('mail', False),
        phone_number = request.POST.get('phone_number)', False),
        address = request.POST.get('address)', False),
        account = request.POST.get('account)', False),
        account_pw = request.POST.get('account_number)', False),
    )
    person.save()
    return render(request, 'regist/form.html')

def home(request):
    return render(request, 'regist/home.html')

def introduction(request):
    return render(request, 'regist/introduction.html')