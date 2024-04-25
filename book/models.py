from django.db import models

from account.models import Student

# Create your models here.

class BookCategory(models.Model):
    category_id = models.CharField(max_length=10,null=False)
    category_name = models.CharField(max_length=100,null=False)
    
class BookCode(models.Model):
    code_id = models.CharField(max_length=1,null=False)
    code_name = models.CharField(max_length=100,null=False)
    
class BookData(models.Model):
    name = models.CharField(max_length=100,null=False)
    category_id = models.ForeignKey(BookCategory,on_delete=models.CASCADE)
    author = models.CharField(max_length=100,null=True)
    publisher = models.CharField(max_length=100,null=True)
    publish_date = models.DateField(null=True)
    summary = models.CharField(max_length=40,null=True)
    price = models.IntegerField(null=False)
    keeper_id = models.IntegerField(null=False)
    status = models.ForeignKey(BookCode,on_delete=models.CASCADE,max_length=24,null=False)
    
class BookLendRecord(models.Model):
    book = models.ForeignKey(BookData,on_delete=models.CASCADE,null=False)
    borrower = models.ForeignKey(Student,on_delete=models.CASCADE,null=False)
    borrow_date = models.DateField(null=True)