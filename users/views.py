from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django_facebook.decorators import FacebookRequired
from django_facebook.models import FacebookCustomUser
from open_facebook.api import *
from django_facebook.connect import connect_user
from users.models import Location
from django.utils import simplejson
from django.template.context import RequestContext
from datetime import datetime
from tastypie.models import ApiKey

rangeVal = 0.0002


def home(request):
  usr = FacebookCustomUser.objects.get(username = request.user.username)
  print(usr.raw_data)
  context = RequestContext(request, {'request':request, 'user':request.user, 'usr':usr.raw_data[7]})
  return render(request, 'pages/users/home.html', context)


# App registration
def app_registration(request):
  access_token = request.GET['access_token']
  #print(access_token)
  # This connects the user who is logged in via FB on their app
  # creates a new user record in the DB
  action, user = connect_user(request, access_token)
  #print("-----")
  #print (user.id)
  #print(user.username)
  # Create new API key for TastyPie for this new users. 
  # If the user already exists, then it just fetches the existing key
  newKey = ApiKey.objects.get_or_create(user=user)[0].key
  #print(newKey)
  #print("-----")
  newData = []
  data = {}
  data['userID'] = str(user.id)
  data['username'] = str(user.username)
  data['api_key'] = str(newKey)
  newData.append(data)
  print(data)

  return HttpResponse(simplejson.dumps(newData), mimetype="application/javascript")


#User Registration view
def register(request):
  #form = UserCreationForm()
  form = RegistrationForm()
  c = {
    'form': form,
  }

  return render(request, "registration/registration.html", c)

def all_users(request):

  users = User.objects.all()

  c = {
    'users': users,
    'page_title': "All Users",
    'page_subtitle': "",
  }
  return render(request, 'pages/users/all_users.html', c)


def user_details(request):
  # need to extend the user model to use request.user instead:wq

  userPK = 1

  user = User.objects.get(pk = userPK)
  locationData = Location.objects.filter(user = user).order_by('timeStamp')

  c = {
    'user': user,
    'locationData': locationData,
    'page_title': user.fName,
    'page_subtitle': "Location Data",
  }
  return render(request, 'pages/users/user_details.html', c)

"""
Simple function to capture the required user ID for creating a data map
"""
def plot_gps_points(request, userPK):

  c = {
    'userPK': userPK,
  }


  return render(request, 'pages/users/plot_gps_points.html', c)


"""
Takes in a user ID and generates all the JSON data required to plot
the points on a Google Map
"""
def gmap_user_data(request):

  locationList = []

  if request.method == 'GET':
    if request.GET.has_key('userPK'):
      userPK = int(request.GET['userPK'])
      dataPoints = Location.objects.filter(user__pk = userPK)

      for d in dataPoints:
        dItem = {}
        dItem['name'] = d.user.fName
        dItem['lat'] = str(d.latitude)
        dItem['lng'] = str(d.longitude)

        # Strip out just the time portion of the timeStamp
        strTime = datetime.strptime(str(d.timeStamp), "%Y-%m-%d %H:%M:%S+00:00")
        # ctime outputs a full string, such as "Thu Jan 1 20:42:00 2015"
        newStamp = strTime.ctime()
        dItem['timeStamp'] = newStamp
        locationList.append(dItem)
  return HttpResponse(simplejson.dumps(locationList), mimetype="application/javascript")

def delete_all_data_points(request):
  if request.method == "GET":
    if request.GET.has_key('userPK'):
      userPK = int(request.GET['userPK'])
      Location.objects.filter(user__pk = userPK).delete()
  return HttpResponseRedirect("/user/user-details/")



def sort_data_points(request):
  data = Location.objects.all()

  msg = "<h1>Longitude - Latitude</h1>"
  msg = "<table style='font-family: Tahoma; font-size: 10pt'><thead><th>Latitude</th><th>Longitude</th></thead><tbody>"


  # The timestamp of the first data point
  timeTracker = data[0].timeStamp


  for D in data:
    timeData = Location.objects.filter(timeStamp = D.timeStamp)
    prevLat = 0
    prevLong = 0
    msg += "<tr><td colspan=2><br><center>Timestamp: " + str(D.timeStamp) + "</center></td></tr>"
    for d in timeData:
      latClose = False
      longClose = False
      if (abs(d.latitude - prevLat) <= rangeVal): 
        latClose = True
      if (abs(d.longitude - prevLong) <= rangeVal): 
        longClose = True

        msg += "<td style='border-bottom: 1 solid #00CCCC;'>" + str(d.longitude) + "</td><tr>"
        msg += "<tr><td style='border-bottom:1px solid #D0D0D0;'>" + str(d.latitude) + "</td>"

      prevLat = d.latitude
      prevLong = d.longitude
  msg += "</tbody></table>"

    
  return HttpResponse(msg)
  


"""
Simply takes in a float and removes the trailing decimals, 
without doing any rounding
"""
def chop_decimals(val, numDecimals):
    # We turn the value into a string so we can chop off
    # everything after the first numDecimals decimals.
    val = str(val)
    lead, decimals = val.split(".")
    decimals = decimals[:numDecimals]
    return(float(lead + "." + decimals))


"""
Returns a dictionary of users, and time stamps, of encounters. 
An encounter is when a person is within a certain distance of the user,
and at the same time. 
"""
def get_encounters(request):
  user = User.objects.get(pk=1)
  userLocs = Location.objects.filter(user = user)

  for ul in userLocs:

    """
    First we must figure out our range for both lat and long. 4 decimal
    places is precision of 11 meters, so we'll go with that. If we have a
    lat value of 32.1234 then we should accept 32.1234 +/- 0.00005
    0.00005 is half the 4 decimal accuracy, so half higher and half lower
    of our target value gives us the full 11 meters of range.

    """

    # Lets get our ranges set up first
    latStart = float(ul.latitude) - rangeVal
    latEnd = float(ul.latitude) + rangeVal
    longStart = float(ul.longitude) - rangeVal
    longEnd = float(ul.longitude) + rangeVal

    latStart = chop_decimals(latStart, 4)
    latEnd = chop_decimals(latEnd, 4)
    longStart = chop_decimals(longStart, 4)
    longEnd = chop_decimals(longEnd, 4)

    """
    print("-----")
    print(ul.latitude)
    print(latStart)
    print(latEnd)
    if float(ul.latitude) > latStart and float(ul.latitude) < latEnd:
      print("Lat In range")
    print(ul.longitude)
    print(longStart)
    print(longEnd)
    if float(ul.longitude) > longStart and float(ul.longitude) < longEnd:
      print("Long In range")
    print("-----")
    """

    # This query gets all locations for all users excluding the current user, filtering
    # out GPS data points that are outside the range specified by rangeVal
    tmp = Location.objects.filter(timeStamp = ul.timeStamp).exclude(user = user).filter(latitude__gte = latStart).filter(latitude__lte = latEnd).filter(longitude__gte = longStart).filter(longitude__lte = longEnd)
    for t in tmp:
      print(t)
      print(ul)
      print("------")

      

    
  return HttpResponse(userLocs)


#------------- USER SPECIFIC FUNCTIONS ---------------#

def profile(request, userPK):
  user = User.objects.get(pk = userPK)

  c = {
    'user': user,
    'page_title': user.fName,
    'page_subtitle': "Profile",
  }

  return render(request, 'pages/users/profile.html', c)


