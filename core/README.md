
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






