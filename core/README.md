
''''
# pip install virtualenv
''''



''''
# virtualenv env
''''



''''
# env/Scripts/activate
''''


''''
# pip install Django
''''

''''
#  python manage.py startapp home
''''



''''
# python manage.py runserver
''''



''''
server port can change and run on port http://127.0.0.1:8000/
# python manage.py runserver 0.0.0.0:5000
''''



''''
it give index of forloop
# {{forloop.counter}}
''''



''''
# django template tags search from google and know more tags about template tags
''''




''''
# model filed explore from google
''''


''''
// run this command after making scgema model
# python manage.py makemigrations
''''



''''
// run this command after making scgema model
# python manage.py migrate
''''


''''

# python manage.py shell
''''







''''
1)
// data create and store in student variables
# student = Student(name='ankush',age=18,email='ankushgupta0510@gmail.com,address='gandhinagarbhopal')

// data save
# >>> student.save()



2)
// data create and store in student variables and direct saved data
# student = Student.objects.create(name='a',age=23,email='ankush@gmail.com',address='GKP')           
''''


''''
// Get data from dbsqlite
# Student.objects.all()[0].name   
# Student.objects.all()[0].age   
# Student.objects.all()[0].email   
# Student.objects.all()[0].address   



// get by for loop

>>> for i in car:
...    print(f"car name is {i.car_name} and the speed is {i.speed}") 
...

// outputs:-
car name is Nexin and the speed is 110
car name is neno and the speed is 150
car name is cys and the speed is 160
car name is cys and the speed is 160
'''''





''''
// it also give data which store insqlite  
# car = Car.objects.get(id=1)
# car.car_name
# car.speed

//  get genrate error if not data present in sqlite


// filter also find data but it not generat error in case of not present data in sqlite
# car = Car.objects.filter(id=1)
 '''''


// project vege
''''
//  download for imageField uploading
# python -m pip install Pillow
''''

''''
//  import it in form tag bcz it help to upload the image
# enctype="multipart/form-data"
''''

''''

// import in form verification
#  {% csrf_token %}
''''



''''
// this important so expolore from documentation
# login_required 

''''





''''
// update value in database
# car = Car.objects.get(id=1)
# car.car_name =  'sufaari'
# car.speed = 210
# car.save()


// directly update value in database
# Car.objects.get(id=1).update(car_name =  'sufaari',speed = 210)
''''



''''
// delete all data 

# Car.objects.all().delete()

''''



''''
// delete some data by this

# Car.objects.get(id=1).delete()

''''

##### some useful concepts



''''
it show only those characters which you mentioned 
# truncatechars
''''





/// videio  13 command

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








///  vidio 14 Generator admin panel password and username

1) 
'Faker class' is a liberary which genrates garbage  data or fake data and explore it from documentation 
# pip install django-faker



2)  // gerate random studentId using faker

>>> python manage.py shell
>>> pip install faker
>>>from vege.seed import *
>>> seed_db()
>>> seed_db()
>>> seed_db()









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


10) value() concept


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





14) 