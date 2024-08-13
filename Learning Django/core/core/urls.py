"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import *      # import views of home app
from vege.views import *      # import views of vege app

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    
    # home routes
    path('',home, name="home" ),
    path('send_email/',send_email, name="send_email" ),
    path('contact/',contact, name="contact" ),
    path('about/',about, name="about" ),


    # vege routes
    path('delete-receipe/<id>/',delete_receipe, name="delete_receipe"),
    path('update-receipe/<id>/',update_receipe, name="update_receipe"),
    path('login/',login_page, name="login_page"),
    path('logout/',logout_page, name="logout_page"),
    path('register/',register, name="register"),
    path('receipe/',receipe, name="receipe"),
    
    
    path('success-page/',success_page, name="success_page" ),
    path('students/',get_students, name="get_students" ),
    path('see-marks/<student_id>/',see_marks, name="see_marks" ),   # here 'see_marks' not give any problem bcz we use special method url controll of Django
    


    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()