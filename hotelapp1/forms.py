from django import forms
from .models import guesttable
from .models import staffprofile
from .models import roomtable
from .models import bookingtable
from .models import feedback

class GuestForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=guesttable.genderchoice, widget=forms.RadioSelect)
    class Meta:
        model = guesttable
        
        fields= ('firstname','lastname','email','number','age','gender','address','image','username','password','confirm_password')
        
        widgets ={
            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'number':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
            'confirm_password':forms.TextInput(attrs={'class':'form-control'}),
        }

class StaffForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=staffprofile.genderchoice, widget=forms.RadioSelect)
    class Meta:
        model = staffprofile
        
        fields= ('firstname','lastname','email','number','age','gender','address','image','username','password','confirm_password','staff_id','approval')
        
        widgets ={
            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'number':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
            'confirm_password':forms.TextInput(attrs={'class':'form-control'}),
        }
        
class RoomForm(forms.ModelForm):
    class Meta:
        model=roomtable
        fields=('room_number','room_type','room_price','availability')
        widgets={
            'room_number':forms.TextInput(attrs={'class':'form-control'}),
            'room_type':forms.TextInput(attrs={'class':'form-control'}),
            'room_price':forms.TextInput(attrs={'class':'form-control'}),
        }
        
class BookingForm(forms.ModelForm):
    class Meta:
        model=bookingtable
        fields=('guest','room','checkindate','checkoutdate','approval')
        
class FeedbackForm(forms.ModelForm):
    class Meta:
        model=feedback
        fields=('email','topic')