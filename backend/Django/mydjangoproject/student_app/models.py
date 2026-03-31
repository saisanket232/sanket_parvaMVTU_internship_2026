from django.db import models

# Create your models here.

class Student(models.Model):
    GENDER_CHOICES=[('Male','Male'),('Female','Female'),('Other','Other')]
    STATE_CHOICES=[('Maharashtra','Maharashtra'),('Karnataka','Karnataka'),('Goa','Goa')]
    CITY_CHOICES=[('Mumbai','Mumbai'),('Pune','Pune'),('Bangalore','Bangalore')]
    BRANCH_CHOICES=[('CS','CS'),('IT','IT'),('ENTC','ENTC')]
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10,unique=True)
    address = models.TextField()
    gender=models.CharField(max_length=10,choices=GENDER_CHOICES)
    state=models.CharField(max_length=20,choices=STATE_CHOICES)
    city=models.CharField(max_length=20,choices=CITY_CHOICES)
    pincode=models.CharField(max_length=6)
    branch=models.CharField(max_length=4,choices=BRANCH_CHOICES)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
