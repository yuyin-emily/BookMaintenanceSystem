from django.shortcuts import render, get_object_or_404,HttpResponseRedirect

from django.db.models import Q

from book.models import BookCategory,BookCode,BookData,BookLendRecord
from account.models import Student

from book.forms import BookDataForm,BookDataSearchForm

# Create your views here.
def search(request):
    try:
        if request.method == "POST":
            name = request.POST.get('name', None)
            category = request.POST.get('category', None)
            keeper_name = request.POST.get('keeper_name', None)
            status = request.POST.get('status', None)
            form = BookDataSearchForm(request.POST)
            condition = Q()
            if name:
                condition &= Q(name__icontains=name)
            if category:
                condition &= Q(category_id=category)
            if keeper_name:
                condition &= Q(keeper_id=keeper_name)
            if status:
                condition &= Q(status_id=status)
            books = BookData.objects.filter(condition).order_by("id")
        else:
            form = BookDataSearchForm()
            books = BookData.objects.all().order_by("id")
            
        for book in books:
            category = BookCategory.objects.get(category_id=book.category_id)
            book.category_name = category.category_name
            status = BookCode.objects.get(code_id=book.status_id)
            book.status_name = status.code_name
            if book.keeper_id:
                keeper_name = Student.objects.get(id=book.keeper_id).username
                book.keeper_name = keeper_name
            else:
                book.keeper_name = "-"
    except:
        errormessage = "讀取錯誤"
        
    return render(request,"book/search.html",locals())

def detail(request, pk=None):
    edit = 2
    book = get_object_or_404(BookData, id=pk)
    form = BookDataForm(instance=book, readonly=True)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("book/edit/"+str(pk)+"/")
    return render(request, 'book/bookdata.html', {'edit': edit, 'form': form, 'pk': pk})

def create(request):
    edit = 1
    if request.method == "POST":
        form = BookDataForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("Book")
    else:
        form = BookDataForm(readonly=False)
    return render(request, "book/bookdata.html", {'edit': edit, 'form': form})
    
    

def edit(request, pk=None):
    edit = 3
    book = get_object_or_404(BookData, pk=pk)
    if book.keeper_id:
        keeper_name = Student.objects.get(id=book.keeper_id).username
        book.keeper_name = keeper_name
    else:
        book.keeper_name = "-"
    if request.method == "POST":
        form = BookDataForm(request.POST, instance=book, readonly=False)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("book/detail/"+str(pk)+"/")
    else:
        form = BookDataForm(instance=book, readonly=False)
    return render(request, "book/bookdata.html", {'edit': edit, 'form': form, 'pk': pk,'book':book})
    
def delete(request, pk=None):
    book = get_object_or_404(BookData, pk=pk)
    book.delete()
    return render(request, "", locals())

def lend_record(request, pk=None):
    records = BookLendRecord.objects.filter(book=pk).order_by("-borrow_date").all()
    for record in records:
        record.borrower_id = Student.objects.get(username=record.borrower).id
    return render(request, "book/lend_record.html", locals())

