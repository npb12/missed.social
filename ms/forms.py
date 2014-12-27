from django import forms
from users.models import User

class Sample_Data_Form(forms.Form):
  HEADING_CHOICES = (
      ('N', 'North'),
      ('E', 'East'),
      ('S', 'South'),
      ('W', 'West'),
      )
  allUsers = User.objects.all()
  startLat = forms.DecimalField(max_digits = 10, decimal_places = 5, label = 'Starting Latitude')
  startLong = forms.DecimalField(max_digits = 10, decimal_places = 5, label = 'Starting Longitude')
  user = forms.ModelChoiceField(queryset=allUsers, label = 'User')
  makeStop = forms.BooleanField(label = 'Make a stop?', required = False)
  heading = forms.ChoiceField(label = 'Which general direction?', choices = HEADING_CHOICES)
  startDate = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}), label = 'Start Time/Date')


