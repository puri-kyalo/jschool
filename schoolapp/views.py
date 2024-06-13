from django.shortcuts import render, redirect

from schoolapp.forms import  ContactForm


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def programmes(request):
    return render(request,'programmes.html')

def facts(request):
    return render(request,'facts.html')

def faciities(request):
    return render(request,'facilities.html')

def team(request):
    return render(request,'team.html')

def testimonials(request):
    return render(request,'testimonials.html')



def gallery(request):
    return render(request,'gallery.html')

def sports(request):
    return render(request,'sports.html')

def appointment(request):
    return render(request,'appointment.html')

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/contact")
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


