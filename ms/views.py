from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404

from users.models import User, UserType, InterestType, Location
from ms.forms import Sample_Data_Form

def sample_gps_data(request):

  if request.method == "POST":
    form = Sample_Data_Form(request.POST)
    if form.is_valid():
      # process form
      print(form)
    else:
      print("not valid")
  else:
    form = Sample_Data_Form()

  c = {
      'form':form,
      }
  return render(request, 'pages/ms/sample_gps_data.html', c)
