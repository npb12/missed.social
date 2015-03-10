from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from users.models import Location
from django.contrib.auth.models import User
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
      numMins = form.cleaned_data['numMins']
      makeStop = form.cleaned_data['makeStop']
      heading = form.cleaned_data['heading']
      startDate = form.cleaned_data['startDate']
      generate_sample_gps_data(startLat, startLong, user.pk, numMins, makeStop, heading, startDate)
  else:
    form = Sample_Data_Form()

  c = {
      'form':form,
      'page_title': "Sample Data",
      'page_subtitle': "Generate GPS data points",
      }
  return render(request, 'pages/ms/sample_gps_data.html', c)


# Takes in a set of arguments and produces sample GPS data attached to the user provided.
# These data will be used for testing purposes, this won't be a production function
def generate_sample_gps_data(lat, lng, userPK, numMins, makeStop, heading, timeStamp):

  # Number of minute intervals to generate data. Initially set at every 1 minute generate a data point
  # This should be 1, normally. Changed to 0 to generate a LOT of data points at one time stamp
  timeInterval = 0
  
  # A maxDisctanceInterval of 0.0001 is roughly 11 meters. 
  # So, we're saying this data can't move faster than 11 meters/interval (initially set at 11m/minute)
  # This could change with car rides, etc. 
  maxDistanceInterval = 0.0001

  user = User.objects.get(pk = userPK)

  # If we need to make a stop (makeStop = True) then we need a boolean flag to keep track of whether
  # we've made that stop yet. We only want one stop per trip.
  stopMade = False
  # The stop will be anywhere from 10-60 minutes long
  stopLength = random.randint(10,60)

  while (numMins > 0):
    tmpLat = random.uniform(0.0, maxDistanceInterval)
    tmpLat = ceil(tmpLat*1000000)/1000000
    lat = round(lat, 6)
    tmpLng = random.uniform(0.0, maxDistanceInterval)
    tmpLng = ceil(tmpLng*1000000)/1000000
    lng = round(lng , 6)

    # Make next data point in the general direction of the heading chosen
    # The 'adjustInt' will be -1, 0 or 1. That will make the long/lat increase,
    # decrease or not change. 
    if heading == 'N':
      lat = float(lat) + tmpLat
      adjustInt = random.randint(-1,1)
      lng = float(lng) - (adjustInt * tmpLng)
    elif heading == 'E':
      lng = float(lng) + tmpLng
      adjustInt = random.randint(-1,1)
      lat = float(lat) + (adjustInt * tmpLat)
    elif heading == 'S':
      lat = float(lat) - tmpLat
      adjustInt = random.randint(-1,1)
      lng = float(lng) - (adjustInt * tmpLng)
    elif heading == 'W':
      lng = float(lng) - tmpLng
      adjustInt = random.randint(-1,1)
      lat = float(lat) + (adjustInt * tmpLat)
    elif heading == 'A':
      adjustInt = random.randint(-1,1)
      lng = float(lng) + (adjustInt * tmpLng)
      lat = float(lat) + (adjustInt * tmpLat)

    timeStamp = timeStamp + datetime.timedelta(minutes = timeInterval)

    newLoc = Location(user = user, latitude = lat, longitude = lng, timeStamp = timeStamp)
    newLoc.save()
    
    numMins -= 1

  return 0
