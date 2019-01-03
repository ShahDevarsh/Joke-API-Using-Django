import requests
import json


from django.shortcuts import render
from music.models import Student


def index(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')

        r = requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + lastname)
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')

        var = {'joke': joke}

        return render(request, 'music/index.html', var)
    else:
        return render(request, 'music/index.html')


def form(request):
        if request.method == 'POST':
            firstname_r = request.POST.get('firstname')
            lastname_r = request.POST.get('lastname')

            var = Student(first_name=firstname_r, last_name=lastname_r)
            var.save()
            return render(request, 'music/form.html')
        else:
            return render(request, 'music/form.html')
