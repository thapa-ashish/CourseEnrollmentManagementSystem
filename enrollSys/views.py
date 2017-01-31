from django.shortcuts import render, render_to_response, redirect
from enrollSys.settings import ADMIN_USERNAME, ADMIN_PASSWORD
from django.template.context import RequestContext
import logging
from enrollSys.forms import CourseForm, UserForm, StudentForm, InstructorForm
from enrollSys.models import Course, Student, Users, Instructor
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.template.context_processors import request




logger = logging.getLogger(__name__)


def loginPage(request):
    return render(request, "templates/login.html")


def login(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            print username
            print password
            user = Users.objects.filter(username=username, password=password)
            print user
            
            if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
                logger.info('Username: ' + username + ' Password: ' + password)
                return redirect('/admin/allcourses')
            elif not user:
                print "no user found"
                return render(request, "templates/login.html", {"message":"invalid credentials"})
            elif user[0].userRole== 'student':
                return render(request, "templates/student/index.html")
            elif user[0].userRole == 'instructor':
                return render(request,"templates/instructor/index.html")
            else:
                print "inside else"
                return render(request, "templates/login.html", {"message":"invalid credentials"})
          
      

  
 
 
 
def signup(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        user = Users.objects.filter(username=username)
        if not user:
            role = request.POST.get("userRole")
            print role
            if role == "student":
                user = UserForm(request.POST)
                user_model = user.save()
                saveStudent(request, user_model)
                return render(request, "templates/login.html")
            elif role == "instructor":
                
                user = UserForm(request.POST)   
                user_model = user.save() 
                saveInstructor(request, user_model)
                return render(request, "templates/login.html")
                
        
        else:
            print username + " username is already taken"
            return render(request, "templates/signup.html", {"message":"Username is already taken"})
            
    else:
        return render(request, "templates/signup.html")
          
        
        
        
def saveStudent(request, user):
    studentForm = StudentForm(request.POST)
    student = Student(firstname=studentForm["firstname"].value(), lastname=studentForm["lastname"].value(), address=studentForm["address"].value(), email=studentForm["email"].value(), contact_number=studentForm["contact_number"].value(), user=user)
    student.save()
    
    
def saveInstructor(request, user):
    instructorForm = InstructorForm(request.POST)
    instructor = Instructor(firstname=instructorForm["firstname"].value(), lastname=instructorForm["lastname"].value(), address=instructorForm["address"].value(), email=instructorForm["email"].value(), contact_number=instructorForm["contact_number"].value(), user=user)
    instructor.save()
    
  
def adminIndex(request):  
    return render(request, "templates/admin/allcourses.html") 

def newCourseForm(request):
    instructor=Instructor.objects.all()
    return render(request, "templates/admin/addnewCourse.html",{"instructor":instructor})


def addCourse(request):
    if request.method == 'POST':
        course = CourseForm(request.POST)
        course.save()
        return redirect('/admin/allcourses')
    
  
      
def allCourses(request): 
    courses = Course.objects.all().order_by('id')

    paginator = Paginator(courses, 10)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        courses = paginator.page(page)
    except(EmptyPage, InvalidPage):
        courses = paginator.page(paginator.num_pages)

    return render_to_response("templates/admin/allcourses.html",
        { 'courses' : courses },
        context_instance=RequestContext(request))
    
    
    
def allStudents(request):
    students=Student.objects.all()
    
    paginator = Paginator(students, 10)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        students = paginator.page(page)
    except(EmptyPage, InvalidPage):
        students = paginator.page(paginator.num_pages)

    return render_to_response("templates/admin/allstudents.html",
        { 'students' : students },
        context_instance=RequestContext(request))
    
 
 
 
   
def editcourse(request,id): 
    if request.method=='GET':
        course=Course.objects.get(pk=id)
        instructor=Instructor.objects.all()
        return render_to_response("templates/admin/editcourse.html",
        { 'course' : course,'instructor':instructor},
        context_instance=RequestContext(request))
        
    if request.method=='POST':
        print request.POST.get('course_name')
        course=Course.objects.get(pk=id)
        course.course_name=request.POST.get('course_name')
        course.course_code=request.POST.get('course_code')
        course.course_fee=request.POST.get('course_fee')
        ins_id=request.POST.get('instructor')
        instructor=Instructor.objects.get(pk=ins_id)
        course.instructor=instructor
        course.save()
        return redirect('/admin/allcourses')

def deletecourse(request,id):
    if request.method=='GET':
        course=Course.objects.get(pk=id)  
        course.delete()
        return redirect('/admin/allcourses')
    
def editstudent(request,id):
    if request.method=='GET':
        student=Student.objects.get(pk=id)
        return render_to_response("templates/admin/editstudent.html",
        { 'student' : student},
        context_instance=RequestContext(request))
        
    if request.method=='POST':
        print request.POST.get('firstname')
        student=Student.objects.get(pk=id)
        student.firstname=request.POST.get('firstname')
        student.lastname=request.POST.get('lastname')
        student.contact_number=request.POST.get('contact_number')
        student.email=request.POST.get('email')
        student.address=request.POST.get('address')
        student.save()
        return redirect('/admin/allstudents')
    
def deletestudent(request,id):
    if request.method=='GET':
        student=Student.objects.get(pk=id)
        student.delete()
        return redirect('/admin/allstudents')
    
