from django.shortcuts import render, get_object_or_404,HttpResponseRedirect,redirect,reverse

from django.db.models import Q

from book.models import BookCategory,BookCode,BookData,BookLendRecord
from account.models import Student

from book.forms import BookDataForm,BookDataSearchForm

from datetime import datetime

# Create your views here.
def search(request):
    try:
        if request.method == "POST":
            name = request.POST.get('name', None)
            category = request.POST.get('category', None)
            keeper_id = request.POST.get('keeper_id', None)
            status = request.POST.get('status', None)
            form = BookDataSearchForm(request.POST)
            condition = Q()
            if name:
                condition &= Q(name__icontains=name)
            if category:
                condition &= Q(category_id=category)
            if keeper_id:
                condition &= Q(keeper_id=keeper_id)
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
                keeper_id = Student.objects.get(id=book.keeper_id).username
                book.keeper_name = keeper_id
            else:
                book.keeper_name = "-"
    except:
        errormessage = "讀取錯誤"
        
    return render(request,"book/search.html",locals())

def detail(request, pk=None):
    edit = 2
    
    try:
        book = get_object_or_404(BookData, pk=pk)
        if book.publish_date:
            book.publish_date = book.publish_date.isoformat()
    except:
        return redirect(reverse('Book'))
    
    form = BookDataForm(instance=book, readonly=True)
    
    if request.method == "POST":
            return redirect(reverse('edit', kwargs={'pk': pk}))
    return render(request, 'book/bookdata.html', {'edit': edit, 'form': form, 'pk': pk})


def create(request):
    edit = 1
    if request.method == "POST":
        form = BookDataForm(request.POST)
        if form.is_valid():
            try:
                form.keeper_id = int(form.cleaned_data['keeper_id'])
            except:
                form.keeper_id = None
            form.save()
            return redirect(reverse('Book'))
    else:
        form = BookDataForm()
    return render(request, "book/bookdata.html", {'edit': edit, 'form': form})
    

def edit(request, pk=None):
    edit = 3
            
    try:
        book = get_object_or_404(BookData, pk=pk)
        if book.publish_date:
            book.publish_date = book.publish_date.isoformat()
    except:
        return redirect(reverse('Book'))
    
    if request.method == "POST":
        form = BookDataForm(request.POST,instance=book)
        if book.keeper_id:
            keeper_name = Student.objects.get(id=book.keeper_id).username
            book.keeper_name = keeper_name
        else:
            book.keeper_name = "-"
        if form.is_valid():
            try:
                form.keeper_id = int(form.cleaned_data['keeper_id'])
            except:
                form.keeper_id = None
            form.save()
            return redirect(reverse('detail', kwargs={'pk': pk}))
    else:
        form = BookDataForm(instance=book, readonly=False)
    return render(request, "book/bookdata.html", {'edit': edit, 'form': form, 'pk': pk,'book':book})
    
def delete(request, pk=None):
    book = get_object_or_404(BookData, pk=pk)
    book.delete()
    print("delete")
    return redirect(reverse('Book'))

def lend_record(request, pk=None):
    records = BookLendRecord.objects.filter(book=pk).order_by("-borrow_date").all()
    for record in records:
        record.borrower_id = Student.objects.get(username=record.borrower).id
    return render(request, "book/lend_record.html", locals())