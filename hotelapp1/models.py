from django.db import models

# Create your models here.

class guesttable(models.Model):
    
    genderchoice=[('male','Male'),('female','Female')]
    
    firstname=models.CharField(max_length=50,null=True)
    lastname=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    number=models.CharField(max_length=50,null=True)
    age=models.CharField(max_length=50,null=True)
    gender=models.CharField(max_length=50,choices=genderchoice)
    address=models.CharField(max_length=50,null=True)
    image = models.ImageField(null=True,blank=True,upload_to="images/")
    username=models.CharField(max_length=50,null=True)
    password=models.CharField(max_length=50,null=True)
    confirm_password=models.CharField(max_length=50,null=True)
    
    
    def __str__(self):
        return self.firstname
    
class staffprofile(models.Model):
    
    genderchoice=[('male','Male'),('female','Female')]
    
    firstname=models.CharField(max_length=50,null=True)
    lastname=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    number=models.CharField(max_length=50,null=True)
    age=models.CharField(max_length=50,null=True)
    gender=models.CharField(max_length=50,choices=genderchoice)
    address=models.CharField(max_length=50,null=True)
    image = models.ImageField(null=True,blank=True,upload_to="images/")
    username=models.CharField(max_length=50,null=True)
    password=models.CharField(max_length=50,null=True)
    confirm_password=models.CharField(max_length=50,null=True)
    staff_id=models.CharField(max_length=20,unique=True)
    approval=models.BooleanField(default=False)
    
    def __str__(self):
        return self.firstname
    
class roomtable(models.Model):
    room_number=models.CharField(max_length=20,null=True)
    room_type=models.CharField(max_length=50,null=True)
    room_price=models.CharField(max_length=50,null=True)
    availability=models.BooleanField(default=False)
    def __str__(self):
        return self.room_number
    
class bookingtable(models.Model):
    guest=models.ForeignKey(guesttable,on_delete=models.CASCADE)
    room = models.ForeignKey(roomtable, on_delete=models.CASCADE)
    checkindate=models.DateField()
    checkoutdate=models.DateField()
    approval=models.BooleanField(default=False)
    
    def __str__(self):
        return self.guest.firstname

class feedback(models.Model):
    email=models.CharField(max_length=50,null=True)
    topic= models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.email