from django.shortcuts import render,redirect
from django.http import HttpResponse
from  vege.seed import *
from  home.utils import send_email_to_client,send_email_with_attachment
from django.conf import settings
from home.models import Car

# Create your views here.


def send_email(request):
    send_email_to_client()
    return redirect('/')

def send_email(request):
    subject = 'This email is from Django server with attachments' 
    message = "Hey please find this attach file with this email" 
    recipient_list = ['ankushguptagupta725@gmail.com']
    # 'BASE_DIR' is give path where django project is running  
    file_path = f'{settings.BASE_DIR}/main.xlsx'
    send_email_with_attachment(subject,message,recipient_list,file_path)
    return redirect('/')

def home(request):
    
    Car.objects.create(car_name= f"Nexon-{random.randint(0,100)}")

    # send_email_to_client()
    # seed_db(100)
    
    peoples =[
        {'name': 'ankush gupta','age':18},
        {'name': 'shyam sahu','age':19},
        {'name': 'monu kushwa','age':17},
        {'name': 'monu2 kushwa','age':14},
        {'name': 'monu3 kushwa','age':12},
    ]
    
    # for i in peoples:
    #     print(i['name'],i['age'])
    
    
    # for i,j in peoples:
    #     # print(i['name'],j['age'])
    #     print(i,j)
    
    vegetable = ['A','B','C','D','E','F','G','H']
    
    text = """ ankush is polite person and has enough information to complete the operation """
    
    

    
    return render(request,'home/index.html',context={'page':'Django Learning' , 'peoples':peoples, 'text':text, 'vegetable':vegetable})


    # return HttpResponse("I am django server")
    # return HttpResponse("<h1>I am django server</h1>")


def contact(request):
    context = {'page':'Contact'}
    return render(request,'home/contact.html',context)



def about(request):
    context = {'page':'About'}
    return render(request,'home/about.html',context)




def success_page(request):
    print("8" * 10)
    return HttpResponse("Success page")


