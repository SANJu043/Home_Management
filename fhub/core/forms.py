from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    first_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date','class': 'form-input'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'date_of_birth', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

#expenses part
from django.utils.timezone import now
from .models import Expense, Budget

class ExpenseForm(forms.ModelForm):
    date = forms.DateField(
        initial=now().date,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )
    class Meta:
        model = Expense
        fields = ['description', 'amount', 'category', 'date', 'paid_by']

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['year', 'month', 'amount']

#todo part
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text', 'priority', 'status', 'member']
        widgets = {
            'text': forms.TextInput(attrs={'placeholder': 'Add new task...', 'class': 'add-task-input'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'member': forms.TextInput(attrs={'placeholder': 'You can use this for date or any tag', 'class': 'add-task-input'}),
        }


#notes part
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'pinned', 'is_favorite', 'color']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Write your note here...'}),
            'color': forms.Select(choices=[('red', 'Red'), ('blue', 'Blue'), ('yellow', 'Yellow'), ('green', 'Green')]),
        }


#invertory part
from .models import InventoryItem

class ItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['name', 'category', 'quantity',]
        widgets = {
            'category': forms.TextInput(attrs={'placeholder': 'Enter tag or category of item (YOUR CHOICE)'})
        }