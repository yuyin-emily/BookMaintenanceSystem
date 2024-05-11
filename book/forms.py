from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import BookData, BookCategory, BookCode, BookLendRecord
from django.forms import ModelForm

class BookDataForm(forms.ModelForm):
    
    publish_date = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
                                    label="出版日期",
                                    input_formats=['%Y-%m-%d'])

    class Meta:
        model = BookData
        fields = ['name', 'category', 'author', 'publisher', 'publish_date', 'summary', 'keeper_id', 'status']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'category': forms.Select(attrs={"class": "form-control"}),
            'author': forms.TextInput(attrs={"class": "form-control"}),
            'publisher': forms.TextInput(attrs={"class": "form-control"}),
            'summary': forms.Textarea(attrs={"class": "form-control"}),
            'keeper_id': forms.Select(attrs={"class": "form-control"}),
            'status': forms.Select(attrs={"class": "form-control"}),
        }
        labels = {
            'name': '書名*',
            'category': '書籍類別*',
            'author': '作者',
            'publisher': '出版社',
            'summary': '內容簡介',
            'keeper_id': '借閱人',
            'status': '借閱狀態*',
        }

    def clean_publish_date(self):
        publish_date = self.cleaned_data['publish_date']
        # if publish_date > timezone.now().date():
        #     raise ValidationError("出版日期不得超過今日")
        return publish_date
    
class BookDataSearchForm(forms.ModelForm):

    # category = forms.ModelChoiceField(queryset=BookCategory.objects.all(), widget=forms.Select(attrs={"class": "form-control"}))
    
    class Meta:
        model = BookData
        fields = ['name', 'category', 'keeper_id', 'status']
        
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'category': forms.Select(attrs={"class": "form-control"}),
            'keeper_id': forms.Select(attrs={"class": "form-control"}),
            'status': forms.Select(attrs={"class": "form-control"}),
        }
        labels = {
            'name': '書名',
            'category': '書籍類別',
            'keeper_id': '借閱人',
            'status': '借閱狀態',
        }
        
        
