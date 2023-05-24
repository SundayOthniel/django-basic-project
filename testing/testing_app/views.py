from django.shortcuts import render

def home(request):
    names = {'surename':'Sunday', 'name':'Othniel'}
    return render(request, 'index.html', names)

def contact(request):
    my_contact = {'number': '09061296934'}
    return render(request, 'contact.html', my_contact)