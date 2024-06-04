from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
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


