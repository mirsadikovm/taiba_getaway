from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


WORKER_LIST = (
    ("Управляющий", "Управляющий"),
    ("Отправитель", "Отправитель"),
    ("Принимающий", "Принимающий"),
)

class EmployeeRegisterForm(forms.Form):

    uid = forms.CharField(max_length=50,widget=forms.Textarea(attrs={
                                                                    'type':'text',
                                                                    'placeholder':"Логин ID для сотрудника",
                                                                     'name':"uid",
                                                                    "padding-right": "15px",
                                                                    "padding-left": "15px",
                                                                     'rows': 1, 
                                                                     'cols': 36.5,
                                                                     'class':"search__input",
                                                                     'style':'resize:none;'})) # type: ignore
    frist_name = forms.CharField(max_length=50,widget=forms.Textarea(attrs={
                                                                    'type':'text',
                                                                    'placeholder':"Имя сотрудника",
                                                                     'name':"frist_name",
                                                                    "padding-right": "15px",
                                                                    "padding-left": "15px",
                                                                    'rows': 1, 
                                                                     'cols': 36.5,
                                                                    'class':"search__input",
                                                                     'style':'resize:none;'}))
    last_name = forms.CharField(max_length=50,widget=forms.Textarea(attrs={
                                                                    'type':'text',
                                                                    'placeholder':"Фамилия сотрудника",
                                                                     'name':"last_name",
                                                                     'rows': 1, 
                                                                     'cols': 36.5,
                                                                     'class':"search__input",
                                                                     'style':'resize:none;'}))
    phone_number = PhoneNumberField(widget=forms.NumberInput(attrs={
                                                                    'type':'tel',
                                                                    'placeholder':"Номер Телефона",
                                                                     'name':"phone_number",
                                                                    "padding-right": "15px",
                                                                    "padding-left": "15px",
                                                                    'class':"search__input",
                                                                    'autocomplete':'off',
                                                                     'style':'resize:none;'}))
    password = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={
                                                                    'type':'password',
                                                                    'placeholder':"Пароль для сотрудника",
                                                                    'name':"password",
                                                                    "padding-right": "15px",
                                                                    'class':"search__input",
                                                                    'style':'resize:none;'}))
    profession = forms.ChoiceField(choices = WORKER_LIST)
    