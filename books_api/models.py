from django.db import models

# Create your models here.
class Author(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    dob=models.DateField()
    bio= models.TextField()

    def __str__(self):
        return self.name 

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books',null=True,blank=True)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.title
    
