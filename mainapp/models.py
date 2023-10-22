from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    name = models.CharField(max_length=200)
    # id for student
    rollno = models.IntegerField(primary_key=True)
    # refers cid from class
    def __str__(self):
        return str(self.rollno)+self.name

class Class(models.Model):
    name = models.CharField(max_length=200)
    # id for class
    cid = models.CharField(max_length=200,primary_key=True)
    # refers to user
    students= models.ManyToManyField(Student,null=True,blank=True)
    def __str__(self):
        return self.cid+self.name

class Subject(models.Model):
    name = models.CharField(max_length=200)
    # id for subject
    sid = models.CharField(max_length=200,primary_key=True)
    # refers cid from class
    cid = models.ManyToManyField(Class)
    prof = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    # partial or full selection
    partial = models.BooleanField(default=False)
    students= models.ManyToManyField(Student,null=True,blank=True)
    def __str__(self):
        return self.sid+self.name



class Attendance(models.Model):
    ATTENDANCE_STATUS   = (
        ("P", "Present"),
        ("A", "Absent"),
        ("N", "Not applicable"),
    )
    sid = models.ForeignKey(Subject,on_delete=models.CASCADE)
    # refers rollno from student
    rollno = models.ForeignKey(Student,on_delete=models.CASCADE)
    # date of attendance
    date = models.DateField()
    # 1 for present 0 for absent
    status = models.CharField(max_length=10,choices=ATTENDANCE_STATUS)

    def __str__(self):
        return self.sid+self.rollno+self.date

