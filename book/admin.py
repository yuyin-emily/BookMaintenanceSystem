from django.contrib import admin

from book.models import BookCategory,BookCode,BookData,BookLendRecord

# Register your models here.
class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ['category_id', 'category_name']

class BookCodeAdmin(admin.ModelAdmin):
    list_display = ['code_id', 'code_name']

class BookDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'author', 'publisher', 'publish_date', 'price', 'keeper_id', 'status']
    list_filter = ['category', 'status']
    search_fields = ['name', 'author']

class BookLendRecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'borrower', 'borrow_date']
    list_filter = ['borrow_date']
    
admin.site.register(BookCategory,BookCategoryAdmin)
admin.site.register(BookCode,BookCodeAdmin)
admin.site.register(BookData,BookDataAdmin)
admin.site.register(BookLendRecord,BookLendRecordAdmin)