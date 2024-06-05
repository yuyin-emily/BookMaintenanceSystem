from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import BookData, BookCategory, BookCode, BookLendRecord
from account.models import Student
from django.forms import ModelForm

from django.utils import timezone
from django.core.exceptions import ValidationError


class BookDataForm(forms.ModelForm):
    
    publish_date = forms.DateField(required=False,widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
                                    label="出版日期",
                                    input_formats=['%Y-%m-%d'])
    

    class Meta:
        model = BookData
        exclude = ['id']
        fields = ['name', 'category', 'author', 'publisher', 'publish_date', 'summary', 'price','keeper_id', 'status']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'category': forms.Select(attrs={"class": "form-control"}),
            'author': forms.TextInput(attrs={"class": "form-control"}),
            'publisher': forms.TextInput(attrs={"class": "form-control"}),
            'summary': forms.Textarea(attrs={"class": "form-control"}),
            'price': forms.NumberInput(attrs={"class": "form-control"}),
            'keeper_id': forms.Select(attrs={"class": "form-control"}),
            'status': forms.Select(attrs={"class": "form-control"}),
        }
        labels = {
            'name': '書名*',
            'category': '書籍類別*',
            'author': '作者',
            'publisher': '出版社',
            'summary': '內容簡介',
            'price': '價格',
            'keeper_id': '借閱人',
            'status': '借閱狀態*',
        }

    def clean_publish_date(self):
        publish_date = self.cleaned_data['publish_date']
        if publish_date:
            if publish_date > timezone.now().date():
                raise ValidationError("出版日期不得超過今日")
        return publish_date
    
    def clean(self):
        cleaned_data = super().clean()
        status = cleaned_data.get('status')
        keeper_id = cleaned_data.get('keeper_id')
        
        if status == '已借出' and not keeper_id:
            raise ValidationError("當借閱狀態為已借出時，借閱人不能為空")
    
    def __init__(self, *args, **kwargs):
        readonly = kwargs.pop('readonly', False)
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['readonly'] = readonly
        self.fields['category'].widget.attrs['disabled'] = readonly
        self.fields['author'].widget.attrs['readonly'] = readonly
        self.fields['publisher'].widget.attrs['readonly'] = readonly
        self.fields['summary'].widget.attrs['readonly'] = readonly
        self.fields['keeper_id'].widget.attrs['disabled'] = readonly
        self.fields['status'].widget.attrs['disabled'] = readonly
        self.fields['publish_date'].widget.attrs['disabled'] = readonly
        self.fields['category'].choices = [('', '請選擇')] + [(category.category_id, category.category_name) for category in BookCategory.objects.all()]
        self.fields['keeper_id'].choices = [('', '請選擇')] + [(student.id, student.username) for student in Student.objects.all()]
        self.fields['status'].choices = [('', '請選擇')] + [(code.code_id, code.code_name) for code in BookCode.objects.all()]
        
    def save(self, commit=True):
        book = super().save(commit=False)
        if commit:
            book.save()
        return book
        
        
    
class BookDataSearchForm(forms.ModelForm):
    
    category = forms.ChoiceField(
        label="書籍類別",
        choices=[('', '請選擇')] + [(category.category_id, category.category_name) for category in BookCategory.objects.all()],
        required=False,
        widget=forms.Select(attrs={"class": "form-control", "id": "category"})
    )
    
    keeper_id = forms.ChoiceField(
        label="借閱人",
        choices=[('', '請選擇')] + [(student.id, student.username) for student in Student.objects.all()],
        required=False,
        widget=forms.Select(attrs={"class": "form-control", "id": "keeper_id"})
    )
    
    status = forms.ChoiceField(
        label="借閱狀態",
        choices=[('', '請選擇')] + [(code.code_id, code.code_name) for code in BookCode.objects.all()],
        required=False,
        widget=forms.Select(attrs={"class": "form-control", "id": "status"})
    )
    
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
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['category'].required = False
        self.fields['status'].required = False
        self.fields['category'].null = True
        self.fields['name'].null = True
        self.fields['status'].null = True
        self.fields["keeper_id"].null = True
        
        
