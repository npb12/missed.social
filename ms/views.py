from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404

from users.models import User, UserType, InterestType, Location
from ms.forms import Sample_Data_Form
import datetime
import random
from math import ceil

# Simple form view to collect arguments that will be passed on
# to the generate_sample_gps_data function below
def sample_gps_data(request):

  if request.method == "POST":
    form = Sample_Data_Form(request.POST)
    if form.is_valid():
      # process form
      startLat = form.cleaned_data['startLat']
      startLong = form.cleaned_data['startLong']
      user = form.cleaned_data['user']
      makeStop = form.cleaned_data['makeStop']
      heading = form.cleaned_data['heading']
      startDate = form.cleaned_data['startDate']
      generate_sample_gps_data(startLat, startLong, user.pk, makeStop, heading, startDate)
    else:
      return HttpResponse("Invalid Form data")
  else:
    form = Sample_Data_Form()

  c = {
      'form':form,
      }
  return render(request, 'pages/ms/sample_gps_data.html', c)


# Takes in a set of arguments and produces sample GPS data attached to the user provided.
# These data will be used for testing purposes, this won't be a production function
def generate_sample_gps_data(lat, lng, userPK, makeStop, heading, timeStamp):

  # Number of minute intervals to generate data. Initially set at every 1 minute generate a data point
  timeInterval = 1
  # A maxDisctanceInterval of 0.0001 is roughly 11 meters. 
  # So, we're saying this data can't move faster than 11 meters/interval (initially set at 11m/minute)
  # This could change with car rides, etc. 
  maxDistanceInterval = 0.0001
  # How much data to generate = 60 minutes worth? 120 minutes worth? 
  length = 60
  user = User.objects.get(pk = userPK)

  while (length > 0):
    tmp = random.uniform(0.0, maxDistanceInterval)
    tmp = ceil(tmp*1000000)/1000000
    lat = float(lat) + tmp
    tmp = random.uniform(0.0, maxDistanceInterval)
    tmp = ceil(tmp*1000000)/1000000
    lng = float(lng) + tmp

    timeStamp = timeStamp + datetime.timedelta(minutes = timeInterval)

    newLoc = Location(user = user, latitude = lat, longitude = lng, timeStamp = timeStamp)
    newLoc.save()
    
    length -= 1


  return 0
