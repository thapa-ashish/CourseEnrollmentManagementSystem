from django.db import models




class Users(models.Model):
    id=models.AutoField(primary_key=True)
    username= models.CharField(max_length=50,blank=False, null=False)
    password=models.CharField(max_length=50,blank=False, null=False)
    userRole=models.CharField(max_length=20,blank=False, null=False)
 
 
 
    
class Instructor(models.Model):
    id=models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=50,blank=False, null=False)
    lastname=models.CharField(max_length=50,blank=False, null=False)
    address=models.CharField(max_length=50,blank=False, null=False)
    email=models.CharField(max_length=50,blank=False, null=False)
    contact_number=models.CharField(max_length=50,blank=False, null=False)
    user=models.ForeignKey(Users)
      
    
class Course(models.Model):
    id=models.AutoField(primary_key=True)
    course_name=models.CharField(max_length=50,blank=False, null=False)
    course_code=models.CharField(max_length=50,blank=False, null=False)
    course_fee=models.BigIntegerField(blank=False, null=False,default=0)
    instructor=models.ForeignKey(Instructor)
    
    
  
    
class Student(models.Model):
    id=models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    contact_number=models.CharField(max_length=50)
    user=models.ForeignKey(Users)
    fees_paid=models.BooleanField(blank=False, null=False,default=False)
    
    
class Course_Student(models.Model):
    id=models.AutoField(primary_key=True)
    course=models.ForeignKey(Course)
    student=models.ForeignKey(Student)
    

    
    
    

    
    
    

    
    
    






