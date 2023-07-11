from django import forms
from phonenumber_field.formfields import PhoneNumberField

class DriverForm(forms.Form):

    frist_name = forms.CharField(max_length=50,widget=forms.Textarea(attrs={
                                                                    'type':'text',
                                                                    'placeholder':" Имя Водителя",
                                                                     'name':"uid",
                                                                    "padding-right": "15px",
                                                                    "padding-left": "15px",
                                                                     'rows': 1, 
                                                                     'cols': 36.5,
                                                                     'style':'resize:none;'}))
    last_name = forms.CharField(max_length=50,widget=forms.Textarea(attrs={
                                                                    'type':'text',
                                                                    'placeholder':" Фамилия Водителя",
                                                                     'name':"uid",
                                                                    "padding-right": "15px",
                                                                    "padding-left": "15px",
                                                                     'rows': 1, 
                                                                     'cols': 36.5,
                                                                     'style':'resize:none;'}))
    phone_number = PhoneNumberField(max_length=50,widget=forms.Textarea(attrs={
                                                                    'type':'text',
                                                                    'placeholder':" Номер Телефона Водителя",
                                                                     'name':"uid",
                                                                    "padding-right": "15px",
                                                                    "padding-left": "15px",
                                                                     'rows': 1, 
                                                                     'cols': 36.5,
                                                                     'style':'resize:none;'}))


class TruckForm(forms.Form):

    driver = DriverForm()
    car_number = forms.CharField(max_length=50,widget=forms.Textarea(attrs={
                                                                    'type':'text',
                                                                    'placeholder':" Номер Машины",
                                                                     'name':"uid",
                                                                    "padding-right": "15px",
                                                                    "padding-left": "15px",
                                                                     'rows': 1, 
                                                                     'cols': 36.5,
                                                                     'style':'resize:none;'}))
    city_from = forms.CharField(max_length=50,widget=forms.Textarea(attrs={
                                                                    'type':'text',
                                                                    'placeholder':" Место Отправки",
                                                                     'name':"uid",
                                                                    "padding-right": "15px",
                                                                    "padding-left": "15px",
                                                                     'rows': 1, 
                                                                     'cols': 36.5,
                                                                     'style':'resize:none;'}))
    weight_in_kg = forms.IntegerField(widget=forms.Textarea(attrs={
                                                                    'type':'text',
                                                                    'placeholder':" Вес",
                                                                     'name':"uid",
                                                                    "padding-right": "15px",
                                                                    "padding-left": "15px",
                                                                     'rows': 1, 
                                                                     'cols': 36.5,
                                                                     'style':'resize:none;'}))
    arrival_timedate = forms.DateField(widget=forms.widgets.DateInput(attrs={
                                                                            'type': 'date',
    }))
