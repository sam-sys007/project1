from django import forms
from multiselectfield import MultiSelectFormField

class feedbackform(forms.Form):
    name = forms.CharField(
        label="Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )
    feedback = forms.CharField(
        label="Enter Your Feedback",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Feedback'
            }
        )
    )
    rating = forms.IntegerField(
        label="Enter Your Rating",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Rating'
            }
        )
    )

class EnquiryForm(forms.Form):
    name=forms.CharField(
        label="Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )
    email = forms.EmailField(
        label="Enter Your Email",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Email'
            }
        )
    )
    mobile = forms.IntegerField(
        label="Enter Your Mobile",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Mobile'
            }
        )
    )
    GENDER_CHOICES=(
        ('F', 'Female'),
        ('M', 'Male')
    )
    gender = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=GENDER_CHOICES,
        label="Select Your Gender:"
    )
    COUESES_CHOICES = (
        ('py', 'Python'),
        ('dj', 'Django'),
        ('Fl', 'Flask')
    )
    courses = MultiSelectFormField(choices=COUESES_CHOICES)
    SHIFTS_CHOICES = (
        ('Morning', 'Morning Shigt'),
        ('Afternon', 'Afternon Shigt'),
        ('Evening', 'Evening Shigt')
    )
    shifts = MultiSelectFormField(choices=SHIFTS_CHOICES)

    y = range(2018, 2022)

    start_date = forms.DateField(
        label="Enter Your Starting Date",
        widget=forms.SelectDateWidget(years=y)
    )