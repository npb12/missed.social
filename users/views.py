from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from users.models import UserProfile, UserType, InterestType, Location
from django.utils import simplejson

from datetime import datetime


def logout_user(request):
  logout(request)
  return HttpResponseRedirect("/") 
  


# @login_required
def all_users(request):

  users = UserProfile.objects.all()

  c = {
    'users': users,
    'page_title': "All Users",
    'page_subtitle': "",
  }
  return render(request, 'pages/users/all_users.html', c)


def user_details(request):
  # need to extend the user model to use request.user instead:wq

  userPK = 1

  user = UserProfile.objects.get(pk = userPK)
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
  return HttpResponseRedirect("/user/user-details/" + str(userPK))

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
  user = UserProfile.objects.get(pk=1)
  userLocs = Location.objects.filter(user = user)

  for ul in userLocs:

    """
    First we must figure out our range for both lat and long. 4 decimal
    places is precision of 11 meters, so we'll go with that. If we have a
    lat value of 32.1234 then we should accept 32.1234 +/- 0.00005
    0.00005 is half the 4 decimal accuracy, so half higher and half lower
    of our target value gives us the full 11 meters of range.

    """
    rangeVal = 0.0002

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
    print(ul.latitude)
    print(latStart)
    print(latEnd)
    print(ul.longitude)
    print(longStart)
    print(longEnd)
    print("-----")
    """

    tmp = Location.objects.filter(timeStamp = ul.timeStamp).exclude(user = user).filter(latitude__gte = latStart).filter(latitude__lte = latEnd).filter(longitude__gte = longStart).filter(longitude__lte = longEnd)
    for t in tmp:
      print(t)
      print(ul)
      print("------")

      

    
  return HttpResponse(userLocs)


#------------- USER SPECIFIC FUNCTIONS ---------------#

def profile(request, userPK):
  user = UserProfile.objects.get(pk = userPK)

  c = {
    'user': user,
    'page_title': user.fName,
    'page_subtitle': "Profile",
  }

  return render(request, 'pages/users/profile.html', c)


