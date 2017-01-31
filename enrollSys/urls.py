"""enrollSys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from enrollSys import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', views.loginPage),
    url(r'^login$',views.login),
    url(r'^signup$',views.signup),
    url(r'^admin/$',views.adminIndex),
    url(r'^admin/course$',views.newCourseForm),
    url(r'^admin/addcourse$',views.addCourse),
    url(r'^admin/allcourses$',views.allCourses),
    url(r'^admin/allstudents$',views.allStudents),
    url(r'^admin/editcourse/(?P<id>\d+)$',views.editcourse),
    url(r'^admin/deletecourse/(?P<id>\d+)$',views.deletecourse),
    url(r'^admin/editstudent/(?P<id>\d+)$',views.editstudent),
    url(r'^admin/deletestudent/(?P<id>\d+)$',views.deletestudent),
    
]
