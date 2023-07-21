from django.db import models


# Create your models here.
# class Department(models.Model):
#     dep_name=models.CharField(max_length=100)
#     def __str__(self):
#         return self.dep_name
class Faculty(models.Model):
    f_name=models.CharField(max_length=100)
    f_post=models.TextField()
    f_image=models.ImageField(upload_to='faculty')
    
    def __str__(self):
        return self.f_name
    
class Services(models.Model):
    s_name=models.CharField(max_length=100)
    s_info=models.TextField()

    def __str__(self):
        return self.s_name
class BookService(models.Model):
    b_name=models.CharField(max_length=100)
    b_phone=models.CharField(max_length=10)
    b_email=models.EmailField()
    b_service=models.ForeignKey(Services,on_delete=models.CASCADE)
    b_date=models.DateField()
    booked_on=models.DateField(auto_now=True)

class Users(models.Model):
    username=models.CharField(max_length=50 )
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    
    def __str__(self):
        return self.username
    