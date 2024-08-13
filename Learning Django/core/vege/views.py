from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import *


from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.


@login_required(login_url="/login/")    # this line means without login username can not visit this web page tumko login page par send kar diya jayenga
def receipe(request):
    if request.method == 'POST':
        data = request.POST
        receipe_image =request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        print(receipe_image)
        print(receipe_name)
        print(receipe_description)


        Receipe.objects.create(
            receipe_image = receipe_image,
            receipe_name = receipe_name,
            receipe_description = receipe_description
        )
                
        return redirect('/receipe/')
    queryset = Receipe.objects.all()
    
    # find search value
    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains=request.GET.get('search'))
        # __icontain is a special keyword use to find elements
   
   # // below code is also run 
    # if request.method == 'GET':
    #     if request.GET.get('search') :
    #         queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))
    
    
    
    context = {'receipes':queryset}
    return render(request,'receipe.html',context)



@login_required(login_url="/login/")    # this line means without login username can not visit this web page tumko login page par send kar diya jayenga
def update_receipe(request,id):
    print(id)
    queryset = Receipe.objects.get(id=id)
    
    if request.method == 'POST':
        data = request.POST
        
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')
        
        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description
        
        if receipe_image:
            queryset.receipe_image = receipe_image
        
        queryset.save()
        return redirect('/receipe/')
    
    
    context = {'receipe':queryset}
    return render(request,'update_receipes.html',context)
    

    


@login_required(login_url="/login/")    # this line means without login username can not visit this web page tumko login page par send kar diya jayenga
def delete_receipe(request,id):
    print(id)
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/receipe/')

    # return HttpResponse("delete_receipe is on")





# vidio no.  12 advanced authentication
def login_page(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username=username).exists():  # exists() return True or False
            messages.error(request,'Invelid Credentials')
            return redirect('/login/')
        user = authenticate(username=username, password=password)     #  check username and passwords is correct or not
        
        if user is None:
            messages.error(request,'Invalid password')
            return redirect('/login/')
        else:
            login(request,user)   # user browser  ke session storage mai store ho jayenga.  if one time user login than again bar bar login nahi karenga util logout na kare users
            return redirect('/receipe/')
            
    return render(request, 'login.html')







def logout_page(request):
    logout(request)   # it take only 1 argument
    print('logout successful')
    return redirect('/login/')










# NOTE -: User models already create in db so that we can use directly User Models
def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request,'Username already exists')
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
        )
        user.set_password(password)    # Do encrption password means (password has converted into hash string)
        user.save()
        messages.info(request,'Account created successfully')
        
        
        return redirect('/register/')


    return render(request, 'register.html')




from django.db.models import Q,Sum

def get_students(request):
    queryset = Student.objects.all()
    
    
    if request.GET.get('search'):
        search = request.GET.get('search')
        
        queryset = queryset.filter(     # Hear  we are using or operator
            Q(student_name__icontains = search) |
            Q(department__department__icontains = search) |
            Q(student_id__student_id__icontains = search) |
            Q(student_email__icontains = search) |
            Q(student_age__icontains = search)  
        )
    
    paginator = Paginator(queryset, 10)   # show 25 contacts per page
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    
    
    return render(request,'report/student.html',{'queryset':page_obj})







from .seed import generate_report_card
def see_marks(request, student_id):
    # generate_report_card()
    queryset = SubjectMarks.objects.filter(student__student_id__student_id =  student_id)
    total_marks = queryset.aggregate(total_marks = Sum('marks'))
    
    return render(request,'report/see_marks.html',{'queryset':queryset, 'total_marks':total_marks})



