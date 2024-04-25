from django.contrib import admin

from book.models import BookCategory,BookCode,BookData,BookLendRecord
# Register your models here.
class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ("category_id","category_name")
    list_filter = ("category_id","category_name")
    search_fields = ("category_name",)
    ordering = ("category_id",)
    
class BookCodeAdmin(admin.ModelAdmin):
    list_display = ("code_id","code_name")
    list_filter = ("code_id","code_name")
    search_fields = ("code_id",)
    ordering = ("code_id",)
    
class BookDataAdmin(admin.ModelAdmin):
    list_display = ("name","category","author","publisher","publish_date","summary","price","keeper_id","status")
    list_filter = ("name","category")
    search_fields = ("name",)
    ordering = ("name",)

class BookLendRecordAdmin(admin.ModelAdmin):
    list_display = ("book","borrower","borrow_date")
    list_filter = ("book","borrower","borrow_date")
    search_fields = ("book",)
    ordering = ("book",)

admin.site.register(BookCategory,BookCategoryAdmin)
admin.site.register(BookCode,BookCodeAdmin)
admin.site.register(BookData,BookDataAdmin)
admin.site.register(BookLendRecord,BookLendRecordAdmin)