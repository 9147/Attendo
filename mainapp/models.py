from django.db import models

class Class(models.Model):
    name = models.CharField(max_length=200)
    # id for class
    cid = models.CharField(max_length=200,primary_key=True)
    def __str__(self):
        return self.cid+self.name

class Subject(models.Model):
    name = models.CharField(max_length=200)
    # id for subject
    sid = models.CharField(max_length=200,primary_key=True)
    # refers cid from class
    cid = models.ForeignKey(Class,on_delete=models.CASCADE)
    # partial or full selection
    partial = models.BooleanField(default=False)
    def __str__(self):
        return self.sid+self.name

class Student(models.Model):
    name = models.CharField(max_length=200)
    # id for student
    rollno = models.IntegerField(primary_key=True)
    # refers cid from class
    cid = models.ForeignKey(Class,on_delete=models.CASCADE)
    def __str__(self):
        return self.rollno+self.name

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

