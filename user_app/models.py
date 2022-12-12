from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email_address = models.CharField(max_length=60)
    age =  models.IntegerField()
    
def create_User(request):
    first_name= request.POST['first_name']
    last_name = request.POST['last_name']
    email_address = request.POST['email']
    age = request.POST['age']
    data = User.objects.create(first_name = first_name,last_name= last_name,email_address=email_address,age=age)
    return data

def get_Users(request):
   return User.objects.all()
    
