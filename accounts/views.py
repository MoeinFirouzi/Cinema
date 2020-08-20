from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # return HttpResponseRedirect(reverse('ticketing:showtime_list'))
            re
        else:
            # undefined user or wrong password
            context = {
                'username': username,
                'error': 'کاربری با این مشخصات یافت نشد'
            }
    else:
        context = {}

    return render(request, 'accounts/login.html', context=context)


"""
HttpResponseRedirect is a subclass of HttpResponse (source code) in the Django web framework 
that returns the HTTP 302 status code, indicating the URL resource was found but temporarily 
moved to a different URL. This class is most frequently used as a return object from a Django view.

Use the HttpResponsePermanentRedirect response object if you instead want to return a 301 permanent 
redirect to a new URL.
https://www.fullstackpython.com/django-http-httpresponseredirect-examples.html
also
https://realpython.com/django-redirects/
"""
