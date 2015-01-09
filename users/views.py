from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404

from users.models import User, UserType, InterestType, Location

def all_users(request):

  users = User.objects.all()

  c = {
    'users': users,
  }
  return render(request, 'pages/users/all_users.html', c)


def user_details(request, userPK):

  user = User.objects.get(pk = userPK)
  locationData = Location.objects.filter(user = user).order_by('timeStamp')

  c = {
    'user': user,
    'locationData': locationData,
  }
  return render(request, 'pages/users/user_details.html', c)
