from django.db import models

from account.models import Student

# Create your models here.

class BookCategory(models.Model):
    category_id = models.CharField(max_length=10, primary_key=True)
    category_name = models.CharField(max_length=100)

class BookCode(models.Model):
    code_id = models.CharField(max_length=1, primary_key=True)
    code_name = models.CharField(max_length=100)

class BookData(models.Model):
    # id = models.AutoField(auto_created=True,primary_key=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)
    author = models.CharField(max_length=100, null=True, blank=True)
    publisher = models.CharField(max_length=100, null=True, blank=True)
    publish_date = models.DateField(null=True, blank=True)
    summary = models.CharField(max_length=255, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    keeper_id = models.IntegerField(null=True, blank=True)
    status = models.ForeignKey(BookCode, on_delete=models.CASCADE)
    
class BookLendRecord(models.Model):
    # id = models.AutoField(auto_created=True,primary_key=True)
    book = models.ForeignKey(BookData, on_delete=models.CASCADE)
    borrower = models.ForeignKey(Student, on_delete=models.CASCADE)
    borrow_date = models.DateField()