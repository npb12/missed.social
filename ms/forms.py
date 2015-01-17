from django import forms
from users.models import User

class Sample_Data_Form(forms.Form):
  HEADING_CHOICES = (
      ('N', 'North'),
      ('E', 'East'),
      ('S', 'South'),
      ('W', 'West'),
      ('A', 'Wander'),
      )
  allUsers = User.objects.all()
  startLat = forms.DecimalField(max_digits = 10, decimal_places = 5, label = 'Starting Latitude')
  startLong = forms.DecimalField(max_digits = 10, decimal_places = 5, label = 'Starting Longitude')
  numMins = forms.DecimalField(max_digits = 4, decimal_places = 0, label = 'Trip duration in Minutes')
  user = forms.ModelChoiceField(queryset=allUsers, label = 'User')
  makeStop = forms.BooleanField(label = 'Make a stop?', required = False)
  heading = forms.ChoiceField(label = 'Which general direction?', choices = HEADING_CHOICES)
  startDate = forms.DateTimeField(widget=forms.TextInput(attrs={'class':'datepicker'}), label = 'Start Date/Time')


