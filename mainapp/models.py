from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    name = models.CharField(max_length=200)
    # id for student
    rollno = models.IntegerField(primary_key=True)
    # refers cid from class
    Class= models.ForeignKey('Class',on_delete=models.CASCADE,default=1)
    def __str__(self):
        return str(self.rollno)+self.name

class Class(models.Model):
    cid = models.CharField(max_length=200,primary_key=True)
    def __str__(self):
        return self.cid

class Subject(models.Model):
    name = models.CharField(max_length=200)
    # id for subject
    sid = models.CharField(max_length=200,primary_key=True)
    # refers cid from class
    Class = models.ForeignKey(Class,on_delete=models.CASCADE,null=True,blank=True)
    prof = models.ForeignKey(User,null=True,blank=True,on_delete=models.SET_NULL)
    # partial or full selection
    partial = models.BooleanField(default=False)
    students= models.ManyToManyField(Student,blank=True)
    def __str__(self):
        return self.sid+self.name



class Attendance(models.Model):
    ATTENDANCE_STATUS = (
        ("P", "Present"),
        ("A", "Absent"),
        ("N", "Not applicable"),
    )
    sid = models.ForeignKey(Subject,on_delete=models.CASCADE)
    # refers rollno from student
    rollno = models.ForeignKey(Student,on_delete=models.CASCADE)
    # date of attendance
    date = models.DateField()
    classno = models.IntegerField(default=1)
    # 1 for present 0 for absent
    status = models.CharField(max_length=10,choices=ATTENDANCE_STATUS)

    def __str__(self):
        return str(self.rollno)+" "+str(self.date)+": " + self.status

class StudentList(models.Model):
    lid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=200,null=True,blank=True)
    is_classList=models.BooleanField(default=True)
    Class=models.ForeignKey(Class,on_delete=models.CASCADE,null=True,blank=True)
    student=models.ManyToManyField(Student,blank=True)
    subjects=models.ManyToManyField(Subject,blank=True)
    def __str__(self):
        return str(self.lid)+self.name