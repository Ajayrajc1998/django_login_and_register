from django import forms
from django.forms import ModelForm
from .models import BookService,Users


# class ContactForm(ModelForm):
#     class Meta:
#         model=Contact
#         fields='__all__'
class Dateinput(forms.DateInput):
    input_type='date'

class BookingForm(forms.ModelForm):
    class Meta:
        model=BookService
        fields='__all__'

        widgets={
            'b_date':Dateinput(),

        }

        labels={'b_name':'Name',
                'b_phone':'Phone',
                'b_email':'email',
                'b_service':'service required',
                'b_date':'Date of Booking'}

class UpdationForm(forms.ModelForm):
        class Meta:
            model = Users
            fields = ['username','email']
            widgets = {
                'username'   : forms.TextInput(attrs={'class' : 'form-control col-3'}),
                'email' : forms.TextInput(attrs={'class' : 'form-control col-3'}),                
            }