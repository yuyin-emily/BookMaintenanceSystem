from django.shortcuts import render

from book.models import BookCategory,BookCode,BookData,BookLendRecord

# Create your views here.
def search(request):
    try:
        books = BookData.objects.all().order_by("id")
    except:
        errormessage = "讀取錯誤"
        
    return render(request,"book/search.html",locals())