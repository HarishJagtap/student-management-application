from django.db import models


class School(models.Model):

    region_id = models.PositiveIntegerField()
    name = models.CharField(max_length=100, primary_key=True)
    email = models.EmailField()
    principal = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)


class Book(models.Model):

    title = models.CharField(max_length=100, primary_key=True)
    author = models.CharField(max_length=100, blank=True)
    publication_date = models.DateField(blank=True, null=True)
    no_of_pages = models.PositiveSmallIntegerField()


class Student(models.Model):
    
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
    ]

    id = models.BigAutoField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, 
                              blank=True, default="")
    school = models.ForeignKey(School, on_delete=models.CASCADE, 
                               blank=True, null=True)
    books = models.ManyToManyField(Book, blank=True)
