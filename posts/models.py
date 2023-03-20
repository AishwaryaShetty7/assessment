from django import db
from django.db import models
from django.db.models import deletion
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Post(models.Model):
    class Meta(object):
        db_table = 'post'

    name = models.CharField(
        'Name', blank=False, null=False, max_length=14, db_index=True, default='Anonymus'
    )
    adhar_num = models.CharField(
        'Adhar Number', blank=False,null=False, max_length=255
    )
    dob = models.CharField(
        'Date of Birth', blank=False,null=False, max_length=255
    )
    identification_mark = models.CharField(
        'Identification Mark', blank=False, null=False, max_length=255
    )
    category = models.CharField(
        'Category', blank=False, null=False, max_length=25
    )
    height = models.CharField(
        'Height', blank=False, null=False, max_length=255
    )
    weight = models.CharField(
        'Weight', blank=False, null=False, max_length=255
    )
    email = models.CharField(
        'Email', blank=False, null=False, max_length=255
    )
    phone_num = models.CharField(
        'Phone Number', blank= False, null= False, max_length=255
    )
    address = models.CharField(
        'Address', blank=False, null=False, max_length=550
    )
    father_name = models.CharField(
        'Father Name', blank=False, null=False, max_length=255
    )
    father_adhar_num = models.CharField(
        'Father Adhar Number', blank=False,null=False, max_length=255
    )
    father_phone_num = models.CharField(
        'Father Phone Number', blank= False, null= False, max_length=255
    )
    father_qualification = models.CharField(
        'Father Qualification', blank=False, null=False, max_length=255
    )
    father_profession =models.CharField(
        'Father Profession', blank=False, null=False, max_length=255
    )
    father_designation =models.CharField(
        'Father Designation', blank=False, null=False, max_length=255
    )
    father_email = models.CharField(
        'Father Email', blank=False, null=False, max_length=255
    )
    mother_name = models.CharField(
        'Mother Name', blank=False, null=False, max_length=255
    )
    mother_adhar_num = models.CharField(
        'Mother Adhar Number', blank=False,null=False, max_length=255
    )
    mother_phone_num = models.CharField(
        'Mother Phone Number', blank= False, null= False, max_length=255
    )
    mother_qualification = models.CharField(
        'Mother Qualification', blank=False, null=False, max_length=255
    )
    mother_profession =models.CharField(
        'Mother Profession', blank=False, null=False, max_length=255
    )
    mother_designation =models.CharField(
        'Mother Designation', blank=False, null=False, max_length=255
    )
    mother_email = models.CharField(
        'Mother Email', blank=False, null=False, max_length=255
    )
    random_num = models.AutoField(
        'Random Number', primary_key=True
    )
    Student_class = models.CharField(
        'Class', blank=False, null=False, max_length=12
    )
    section =models.CharField(
        'Section', blank=False, null=False, max_length=12
    )
    doj = models.CharField(
        'Date of Join', blank=False, null=False, max_length=255
    )
    document = CloudinaryField(
        'Documents', blank= True, db_index=True
    )
   
    created_at = models.DateTimeField(
        'Creation Date', blank=True, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Update Date', blank=True, auto_now=True
    )

    def __str__(self):
        return self.name