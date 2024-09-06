

//  this code you can take from it's official documentation
```
# pip install virtualenv
```



```
# virtualenv env
```



```
# env/Scripts/activate
```


```
# pip install Django
```


```
# django-admin startproject core   
```


```
#  python manage.py startapp home
```



```
# python manage.py runserver
```



```
server port can change and run on port http://127.0.0.1:8000/
# python manage.py runserver 0.0.0.0:5000
```



// command for checking django installed or not
```
python 
import django
django.__version__ 
```


```
it give index of forloop
# {{forloop.counter}}
```



```
# django template tags search from google and know more tags about template tags
```




```
# model filed explore from google
```


```
// run this command after making scgema model
# python manage.py makemigrations
```


```
// run this command after making scgema model
# python manage.py migrate
```


```

# python manage.py shell
```







```
//  import models
>>> from home.models import *


1)
// data create and store in student variables
# student = Student(name='ankush',age=18,email='ankushgupta0510@gmail.com',address='gandhinagarbhopal')

// data save
# >>> student.save()



2)
// data create and store in student variables and direct saved data and [ objects is a model manager]
# student = Student.objects.create(name='a',age=23,email='ankush@gmail.com',address='GKP')           
```


```
// Get data from dbsqlite
# Student.objects.all()[0].name   
# Student.objects.all()[0].age   
# Student.objects.all()[0].email   
# Student.objects.all()[0].address   



// below code print all data store in Student
for i in range(0,4):
     print(Student.objects.all()[i].name)
     print(Student.objects.all()[i].age)
     print(Student.objects.all()[i].email)
     print(Student.objects.all()[i].address)


// get by for loop

>>> for i in car:
...    print(f"car name is {i.car_name} and the speed is {i.speed}") 
...

// outputs:-
car name is Nexin and the speed is 110
car name is neno and the speed is 150
car name is cys and the speed is 160
car name is cys and the speed is 160

```





```
// it also give data which store insqlite  
# car = Car.objects.get(id=1)
# car.car_name
# car.speed

//  get genrate error if not data present in sqlite


// filter also find data but it not generat error in case of not present data in sqlite
# car = Car.objects.filter(id=1)
 ```


// project vege
```
//  download for imageField uploading
# python -m pip install Pillow
```


```
//  import it in form tag bcz it help to upload the image
# enctype="multipart/form-data"
```



```

// import in form verification
#  {% csrf_token %}
```



```
// this important so expolore from documentation
# login_required 

```



```
#### immportant NOTE :-
// below code use karronge to existing data update honga 
Car.objects.get()

// below code use karronge to existing data update nahi honga 
Car.objects.filter()

```


```
#### immportant NOTE :-
// in below code if you use filter function then update keyword will be work and below code will be word successfully
Car.objects.filter(id=1).update(car_name='ankush_car')

// in below code if you use filter function then update keyword will be work and below code will be not word successfully
Car.objects.get(id=1).update(car_name='ankush_car')

```


```
// update value in database
# car = Car.objects.get(id=1)
# car.car_name =  'sufaari'
# car.speed = 210
# car.save()


// directly update value in database
# Car.objects.get(id=1).update(car_name =  'sufaari',speed = 210)
```



```
// delete all data 

# Car.objects.all().delete()

```



```
// delete some data by this

# Car.objects.get(id=1).delete()

```





```
### Media file importants

#### import bellow all code in settings.py of core apps
import os
STATIC_URL = '/static/'      // ye JavaScript CSS HTML ke liye hota hai 
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')     // ye django ki admin wali file hai

STATICFILES_DIR ={
    os.path.join(BASE_DIR, 'public/static')   //  if we upload photo then photo will be uploaded in 'public/static' directory
}

// below both line for media files example PDF, JPG etc.
MEDIA_ROOT = os.path.join(BASE_DIR, "public/static")    
MEDIA_URL = '/media/'



#### import bellow all code in urls.py of core apps


from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns  // import in header


// import in footer
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

```





#### some useful concepts
```
// it show only those characters which you mentioned 
 truncatechars
```

#### important request method
```
// it fetch data of post method
if request.method == "POST":
        data = request.POST


// it fetch data of Get method
request.GET.get('seach')
```


#### videio  13 command  advanced queries part 1
```

1) 
>>> from vege.models import *
>>> vege = Receipe.objects.all()
>>> vege
>>> import random
>>> for veg in vege:
>>>    veg.receipe_view_count = random.randint(10, 100)  
>>>    veg.save()


>>> vege[0].receipe_view_count
37
>>> vege[1].receipe_view_count
49
>>> vege[2].receipe_view_count
86


// do sort receipe_view_count by command in assending order

>>> vege = Receipe.objects.all().order_by('receipe_view_count')          // sort by assending order 
>>> vege[0].receipe_view_count                                       
37
>>> vege[1].receipe_view_count 
38
>>> vege[2].receipe_view_count 
41
>>> vege[3].receipe_view_count  
49



// do sort receipe_view_count by command in Dessending order
>>> vege = Receipe.objects.all().order_by('-receipe_view_count')          // sort by Dessending order 
>>> vege[0].receipe_view_count 
86
>>> vege[1].receipe_view_count                                       
49
>>> vege[2].receipe_view_count 
41
>>> vege[3].receipe_view_count 
38




//  apply limit 

>>> vege = Receipe.objects.all().order_by('receipe_view_count')[0:2]     // only 2 item assign in vege
>>> vege
<QuerySet [<Receipe: Receipe object (2)>, <Receipe: Receipe object (6)>]>
>>>




// filter concept

>>> Receipe.objects.filter(receipe_view_count = 55 )      
<QuerySet []>
>>> Receipe.objects.filter(receipe_view_count = 41 )      
<QuerySet [<Receipe: Receipe object (7)>]>




// filter with __gte and __lte concept

>>> Receipe.objects.filter(receipe_view_count__gte = 41 )      // more than 41 ke items output mai aa jayenge
<QuerySet [<Receipe: Receipe object (4)>, <Receipe: Receipe object (5)>, <Receipe: Receipe object (7)>]>
>>> Receipe.objects.filter(receipe_view_count__gte = 41 )[0].receipe_view_count      
49
>>> Receipe.objects.filter(receipe_view_count__gte = 41 )[1].receipe_view_count      
86



>>> Receipe.objects.filter(receipe_view_count__lte = 41 )     // less than 41 ke items output mai aa jayenge
<QuerySet [<Receipe: Receipe object (2)>, <Receipe: Receipe object (6)>, <Receipe: Receipe object (7)>]>
```




```
```
#### vidio 14 Generator admin panel password and username


1) 
#### 'Faker class' is a liberary which genrates garbage  data or fake data and explore it from documentation 
pip install django-faker



2)  // gerate random studentId using faker

>>> python manage.py shell
>>> pip install faker
>>>from vege.seed import *
>>> seed_db()
>>> seed_db()
>>> seed_db()



### Genrate admin panel

python manage.py createsuperuser

```









```
## ///   vidio no 15 advanced Queries

>>> python manage.py shell
>>> from vege.models import *


### 1) '__startswith' it find which name starts from 'ank' 

>>> queryset = Student.objects.filter(student_name__startswith = 'ank') 
>>> queryset
<QuerySet [<Student: ankush gupta>]>

queryset = Student.objects.filter(student_name__startswith = 'a')   
>>> queryset
<QuerySet [<Student: Aaron Oneill>, <Student: Alexis Vazquez>, <Student: ankush gupta>]>



### 2) '__endswith' it find which email or name end from  '.org' 

>>> queryset = Student.objects.filter(student_email__endswith = '.org') 
>>> queryset
<QuerySet [<Student: Brian Pham>, <Student: Eric Rose>, <Student: Jessica Pittman>, <Student: Mathew Bowen>, <Student: Mrs. Jamie Wheeler>, <Student: Patricia Long>, <Student: Ryan Miller>]>

// explore email by forloop

>>> for q in queryset:
...    print(q.student_email)
...
eriklarsen@example.org
roy69@example.org
kim55@example.org
robertscourtney@example.org
lisablevins@example.org
crossangela@example.org
jessica11@example.org


// explore email with name by forloop

>>> for q in queryset:        
...     print(q.student_email,q.student_name) 
...
eriklarsen@example.org Brian Pham
roy69@example.org Eric Rose
kim55@example.org Jessica Pittman
robertscourtney@example.org Mathew Bowen
lisablevins@example.org Mrs. Jamie Wheeler
crossangela@example.org Patricia Long
jessica11@example.org Ryan Miller




### 3) '__icontains' it find those name which contain 'An'  

>>> queryset = Student.objects.filter(student_name__icontains = 'An')  
>>> queryset
<QuerySet [<Student: Brian Contreras>, <Student: Brian Pham>, <Student: Daniel Lutz>, <Student: Eric Anderson>, <Student: Jessica Pittman>, <Student: Juan Prince>, <Student: Roger Vance>, <Student: Ryan Miller>, <Student: Samantha Ford>, <Student: Stanley Hill>, <Student: ankush gupta>]>




### 4) find department 

>>> queryset[0]
<Student: Brian Contreras>
>>> queryset[0].department
<Department: physics>
>>> queryset[1].department 
<Department: science>

>>> queryset[1].student_id
<StudentID: STU-0835>
>>> queryset[2].student_id
<StudentID: STU-0172>

>>> queryset[2].id
21
>>> queryset[2].pk   //  pk means primary key
21

>>> queryset[1].department      
<Department: science>
>>> queryset[1].department.department
'science'



5) 

>>> queryset = Student.objects.filter(department__department = 'science')   // __department means foreign key
>>> queryset
<QuerySet [<Student: Alexis Vazquez>, <Student: Brian Pham>, <Student: Casey Chambers>, <Student: Jesse Perez>, <Student: Madeline Lucas>, <Student: Robin Smith>, <Student: Ryan Miller>]>
>>> queryset = Student.objects.filter(department__department = 'scie')
>>> queryset
<QuerySet []>



>>> queryset = Student.objects.filter(department__department__icontains = 'scie')  
>>> queryset
<QuerySet [<Student: Alexis Vazquez>, <Student: Brian Pham>, <Student: Casey Chambers>, <Student: Jesse Perez>, <Student: Madeline Lucas>, <Student: Robin Smith>, <Student: Ryan Miller>]>




6) find student those belong to department['dbms','science']  using '__in'


d = ['dbms','science']
>>> d
['dbms', 'science']
>>> queryset = Student.objects.filter(department__department__in = d)             
>>> queryset
<QuerySet [<Student: Alexis Vazquez>, <Student: Brian Pham>, <Student: Casey Chambers>, <Student: Daniel Lutz>, <Student: Eric Anderson>, <Student: Jesse Perez>, <Student: Jessica Pittman>, <Student: Madeline Lucas>, <Student: Rebecca Todd>, <Student: Robin Smith>, <Student: Ryan Miller>, <Student: Sarah Conley>, <Student: Shawn Baker>, <Student: Stanley Hill>, <Student: ankush gupta>]>

>>> queryset.count()
15
>>>




6)  'exclude' keyword print all records  except you have specified

>>> queryset = Student.objects.exclude(department__department ='science')
>>> queryset.count()
24                       //  24 studend do not belong to science department




7) // find queries set from documentation of google.com




8)  exists() function check value present or not in anyy variables, and it return True if value is present otherwise false



>>> queryset = Student.objects.filter(student_name ='munnna')              
>>> queryset.count()      // this is not right way to check value present or not
0
>>> queryset.exists()     // this is  right way to check value present or not
False



>>> queryset = Student.objects.filter(student_name__icontains ='an') 
>>> queryset.count()  
11
>>> queryset.exists()
True





9) apply limit 


>>> queryset = Student.objects.all()                                           
>>> queryset 
<QuerySet [<Student: Aaron Oneill>, <Student: Alexis Vazquez>, <Student: Brian Contreras>, <Student: Brian Pham>, <Student: Casey Chambers>, <Student: Christopher Watkins>, <Student: Daniel Lutz>, <Student: Eric Anderson>, <Student: Eric Rose>, <Student: Jennifer Summers>, <Student: Jesse Perez>, <Student: Jessica Pittman>, <Student: Juan Prince>, <Student: Judith Barnett>, <Student: Leonard Harris>, <Student: Madeline Lucas>, <Student: Mathew Bowen>, <Student: Miss Regina Thornton PhD>, <Student: Mrs. Jamie Wheeler>, <Student: Patricia Long>, '...(remaining elements truncated)...']>

>>> queryset[0:5]    // it print onlt upto 5 elements
<QuerySet [<Student: Aaron Oneill>, <Student: Alexis Vazquez>, <Student: Brian Contreras>, <Student: Brian Pham>, <Student: Casey Chambers>]>


10) values() concept


>>> queryset = Student.objects.all()      // this give all value with describe
>>> queryset.values()



>>> queryset.values()[0]
{'id': 20, 'department_id': 2, 'student_id_id': 20, 'student_name': 'Aaron Oneill', 'student_email': 'logan38@example.net', 'student_age': 25, 'student_address': '3832 Smith Center Apt. 759\nLake Cynthia, MN 09954'}
>>>


>>> queryset.values()[0]['student_age']  
25





11) reverse()

>>> queryset.reverse()    //  element in reverse order
<QuerySet [<Student: ankush gupta>, <Student: Tyler Hayes>, <Student: Teresa Miller>, <Student: Stanley Hill>, <Student: Shawn Baker>, <Student: Sarah Conley>, <Student: Samantha Ford>, <Student: Ryan Miller>, <Student: Roger Vance>, <Student: Robin Smith>, <Student: Rebecca Todd>, <Student: Patricia Long>, <Student: Mrs. Jamie Wheeler>, <Student: Miss Regina Thornton PhD>, <Student: Mathew Bowen>, <Student: Madeline Lucas>, <Student: Leonard Harris>, <Student: Judith Barnett>, <Student: Juan Prince>, <Student: Jessica Pittman>, '...(remaining elements truncated)...']>



>>> queryset        // actual elements                     
<QuerySet [<Student: Aaron Oneill>, <Student: Alexis Vazquez>, <Student: Brian Contreras>, <Student: Brian Pham>, <Student: Casey Chambers>, <Student: Christopher Watkins>, <Student: Daniel Lutz>, <Student: Eric Anderson>, <Student: Eric Rose>, <Student: Jennifer Summers>, <Student: Jesse Perez>, <Student: Jessica Pittman>, <Student: Juan Prince>, <Student: Judith Barnett>, <Student: Leonard Harris>, <Student: Madeline Lucas>, <Student: Mathew Bowen>, <Student: Miss Regina Thornton PhD>, <Student: Mrs. Jamie Wheeler>, <Student: Patricia Long>, '...(remaining elements truncated)...']>
>>>




12)  values_list()  concept

>>> queryset = Student.objects.values_list('id','student_name')    //  it givve only needed elements
>>> queryset
<QuerySet [(20, 'Aaron Oneill'), (16, 'Alexis Vazquez'), (13, 'Brian Contreras'), (19, 'Brian Pham'), (22, 'Casey Chambers'), (15, 'Christopher Watkins'), (21, 'Daniel Lutz'), (29, 'Eric Anderson'), (27, 'Eric Rose'), (18, 'Jennifer Summers'), (26, 'Jesse Perez'), (10, 'Jessica Pittman'), (14, 'Juan Prince'), (8, 'Judith Barnett'), (2, 'Leonard Harris'), (30, 'Madeline Lucas'), (3, 'Mathew Bowen'), (11, 'Miss Regina Thornton PhD'), (28, 'Mrs. Jamie Wheeler'), (25, 'Patricia Long'), '...(remaining elements truncated)...']>
>>> 



13) NOTE :-

get() give the error  if element is not found
filter()  this not give error  if element is not found




## vidio 16 Aggregation and Annotations Advanced Queries 



from django.db.models import *   
from vege.models import *


###  aggregate function

1)
>>> Student.objects.aggregate(Avg('student_age')) 
{'student_age__avg': 24.419354838709676}

>>> Student.objects.aggregate(Max('student_age')) 
{'student_age__max': 30}

>>> Student.objects.aggregate(Min('student_age')) 
{'student_age__min': 18}

>>> Student.objects.aggregate(Sum('student_age'))  
{'student_age__sum': 757}




###  Annotations function

1) 
>>> student = Student.objects.values('student_age').annotate(Count('student_age'))  
>>> student
<QuerySet [{'student_age': 18, 'student_age__count': 1}, {'student_age': 20, 'student_age__count': 3}, {'student_age': 21, 'student_age__count': 4}, {'student_age': 22, 'student_age__count': 2}, {'student_age': 23, 'student_age__count': 1}, {'student_age': 24, 'student_age__count': 6}, {'student_age': 25, 'student_age__count': 4}, {'student_age': 26, 'student_age__count': 1}, {'student_age': 27, 'student_age__count': 2}, {'student_age': 28, 'student_age__count': 3}, {'student_age': 30, 'student_age__count': 4}]>




2) 
>>> student = Student.objects.values('student_name').annotate(Count('student_age') // this line and below line give same answer
>>> student = Student.objects.values('student_name').annotate(Count('student_age'))    
>>> student



3) 
>>> student = Student.objects.values('department').annotate(Count('department'))    
>>> student
<QuerySet [{'department': 1, 'department__count': 7}, {'department': 2, 'department__count': 6}, {'department': 3, 'department__count': 5}, {'department': 4, 'department__count': 5}, {'department': 5, 'department__count': 8}]>
>>>




4) 
>>> student = Student.objects.values('department','student_age').annotate(Count('department'),Count('student_age')) 
>>> student
<QuerySet [{'department': 1, 'student_age': 20, 'department__count': 2, 'student_age__count': 2}, {'department': 1, 'student_age': 21, 'department__count': 2, 'student_age__count': 2}, {'department': 1, 'student_age': 24, 'department__count': 2, 'student_age__count': 2}, {'department': 1, 'student_age': 30, 'department__count': 1, 'student_age__count': 1}, {'department': 2, 'student_age': 21, 'department__count': 1, 'student_age__count': 1}, {'department': 2, 'student_age': 22, 'department__count': 1, 'student_age__count': 1}, {'department': 2, 'student_age': 24, 'department__count': 1, 'student_age__count': 1}, {'department': 2, 'student_age': 25, 'department__count': 1, 'student_age__count': 1}, {'department': 2, 'student_age': 26, 'department__count': 1, 'student_age__count': 1}, {'department': 2, 'student_age': 30, 'department__count': 1, 'student_age__count': 1}, {'department': 3, 'student_age': 20, 'department__count': 1, 'student_age__count': 1}, {'department': 3, 'student_age': 23, 'department__count': 1, 'student_age__count': 1}, {'department': 3, 'student_age': 25, 'department__count': 1, 'student_age__count': 1}, {'department': 3, 'student_age': 27, 'department__count': 1, 'student_age__count': 1}, {'department': 3, 'student_age': 30, 'department__count': 1, 'student_age__count': 1}, {'department': 4, 'student_age': 22, 'department__count': 1, 'student_age__count': 1}, {'department': 4, 'student_age': 25, 'department__count': 1, 'student_age__count': 1}, {'department': 4, 'student_age': 27, 'department__count': 1, 'student_age__count': 1}, {'department': 4, 'student_age': 28, 'department__count': 2, 'student_age__count': 2}, {'department': 5, 'student_age': 18, 'department__count': 1, 'student_age__count': 1}, '...(remaining elements truncated)...']>
>>>







2)

>>> student =Student.objects.annotate(Count('student_name'), Count('student_age')).values_list()
>>> student
<QuerySet [(1, 5, 1, 'ankush gupta', 'ankushgupta0510@gmail.com', 18, 'GN Bhopal', 1, 1), (2, 3, 2, 'Leonard Harris', 'monique43@example.net', 20, '66809 Wilson Land\nLake Natasha, PW 39181', 1, 1), (3, 4, 3, 'Mathew Bowen', 'robertscourtney@example.org', 25, 'Unit 7616 Box 0168\nDPO AE 52939', 1, 1), (4, 5, 4, 'Stanley Hill', 'jessicaortiz@example.com', 24, '0362 Medina Radial Apt. 323\nMillermouth, SC 91983', 1, 1), (5, 4, 5, 'Roger Vance', 'imacdonald@example.com', 28, '98671 Cindy Roads Suite 938\nEast Jack, NM 38934', 1, 1), (6, 2, 6, 'Samantha Ford', 'austintaylor@example.com', 21, '93211 Steven Glen\nLake Ashley, CO 09033', 1, 1), (7, 5, 7, 'Shawn Baker', 'bobby24@example.net', 28, '04957 Matthew Flats\nWest Tiffany, NY 00915', 1, 1), (8, 3, 8, 'Judith Barnett', 'shannon18@example.com', 25, '14175 Santos River Suite 049\nLake Kennethmouth, FL 32290', 1, 1), (9, 1, 9, 'Ryan Miller', 'jessica11@example.org', 24, '3192 Jones Circles Apt. 693\nNew Tammymouth, AZ 30374', 1, 1), (10, 5, 10, 'Jessica Pittman', 'kim55@example.org', 30, '76639 Morgan Flats\nParkerview, HI 06792', 1, 1), (11, 2, 11, 'Miss Regina Thornton PhD', 'russellchristina@example.com', 30, '94959 Nguyen View Suite 734\nLongmouth, IL 17432', 1, 1), (12, 3, 12, 'Tyler Hayes', 'tdaugherty@example.net', 23, '94239 Billy Stravenue Apt. 629\nPort Lesliemouth, PA 83561', 1, 1), (13, 3, 13, 'Brian Contreras', 'dcunningham@example.com', 27, '897 Bradley Mountain\nElizabethbury, NE 30269', 1, 1), (14, 3, 14, 'Juan Prince', 'pvaldez@example.net', 30, '940 Jessica Springs Suite 088\nPort Brandonberg, KS 44018', 1, 1), (15, 4, 15, 'Christopher Watkins', 'deleonamanda@example.net', 27, '0524 Scott River\nPort Tylerton, VT 79765', 1, 1), (16, 1, 16, 'Alexis Vazquez', 'deborahjohnson@example.net', 21, '868 Nicole Place\nPort Nicoleside, MN 02544', 1, 1), (17, 1, 17, 'Robin Smith', 'jenniferrobbins@example.com', 21, '01457 Hoover Roads\nNorth Lisa, NH 55221', 1, 1), (18, 2, 18, 'Jennifer Summers', 'sarahjordan@example.com', 22, '62326 Mercer River Apt. 138\nJamesborough, WA 36461', 1, 1), (19, 1, 19, 'Brian Pham', 'eriklarsen@example.org', 20, '73853 Stephen Inlet Apt. 656\nNorth Shelby, IL 67675', 1, 1), (20, 2, 20, 'Aaron Oneill', 'logan38@example.net', 25, '3832 Smith Center Apt. 759\nLake Cynthia, MN 09954', 1, 1), '...(remaining elements truncated)...']>
>>>

```

```





```
```
####  django messages  learn from Internet
```


```
### vidio no. 18
Django Pagination
https://docs.djangoproject.com/en/5.0/topics/pagination/

// import Pagination
from django.core.paginator import Paginator



// impoort in view and manipulated it
contact_list = Contact.objects.all()
    paginator = Paginator(contact_list, 25)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)


// import in fronted side and have manipulated it according our project Scenario.

    <nav aria-label="Page navigation example">

        <ul class="pagination">
            {% if queryset.has_previous %}
            <li class="page-item"><a class="page-link" href="?page=1">&laquo; first</a></li>
            <li class="page-item"><a class="page-link" href="?page={{ queryset.previous_page_number }}">previous</a>
            </li>
            {% endif %}

            <span class="current">
                Page {{ queryset.number }} of {{ queryset.paginator.num_pages }}.
            </span>

            {% if queryset.has_next %}
            <li class="page-item"><a class="page-link" href="?page={{ queryset.next_page_number }}">next</a></li>
            <li class="page-item"><a class="page-link" href="?page={{ queryset.paginator.num_pages }}">last
                    &raquo;</a></li>
            {% endif %}
        </ul>

    </nav>



// object_list is use to print all data in one page



// import Q in view page  ( to use or operator )

from django.db.models import Q

// one example
 queryset = queryset.filter(     # Hear  we are using or operator
            Q(student_name__icontains = search) |
            Q(department__department__icontains = search) |
            Q(student_id__student_id__icontains = search) |
            Q(student_email__icontains = search) |
            Q(student_age__icontains = search)  
        )

```


```
#### 19 vidio

// various method  to control url in Django
<a href="/see-marks/{{student.student_id}}">{{student.student_id}}</a>
<a href="{% url 'see_marks' %}">{{student.student_id}}</a>  // it run when any perameter is not accept and hear 'see_marks is a url parameter name'
<a href="{% url 'see_marks' student.student_id %}">{{student.student_id}}</a>  // hear peramter accept then code will be like this



```






```
#### 20 vidio completed successfully
```


```
#### vidio 21 Making custome admin profile
```

```



####  vidio 23 model manager (objects)
```


>>> from vege.models import *
>>> for s in Student.objects.all()[1:10]:
...   s.is_deleted = True
...   s.save()


>>> students = Student.objects.all()
>>> students.count()
90


// it give which student deleted 
>>> Student.admin_objects.all()     
<QuerySet [<Student: Alyssa Lewis>, <Student: Amanda Thomas>, <Student: Amanda Williamson>, <Student: Ana Powell>, <Student: Andrea Lopez>, <Student: Angel Shaw>, <Student: Angela Dixon>, <Student: Angela White>, <Student: Anna Davis>, <Student: Anthony Rivera>, <Student: Brandon Jackson>, <Student: Brian Baker>, <Student: Brooke Murray>, <Student: Bryan James>, <Student: Carla Chang>, <Student: Casey Bird>, <Student: Charles Larson>, <Student: Charles Townsend>, <Student: Christine Potter>, <Student: Cynthia Mason>, '...(remaining elements truncated)...']>
>>>




//
>>> Student.admin_objects.all().count()  
99
```



#### vidio 24 sending email

```
// add below code in 'core/settings.py' 

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""

```


#### vidio 25 sending email with attachments
```

```


#### vidio 26  all about django signal
```
// signal type 
1) pre_save   2) post_save 3) pre_delete 4) post_delete 

```