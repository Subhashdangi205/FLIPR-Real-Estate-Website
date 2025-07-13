from django.shortcuts import render, redirect
from .models import Project, Client, Contact, Subscriber
from django.contrib import messages


# ----------------------------
# Landing Page View
# ----------------------------
def home(request):
    projects = Project.objects.all().order_by('name')[:3]  
    clients = Client.objects.all()
    return render(request, 'home.html', {
        'projects': projects,
        'clients': clients
    })


# ----------------------------
# Contact Form Submission
# ----------------------------
def submit_contact(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        city = request.POST.get('city')

        if full_name and email and mobile and city:
            Contact.objects.create(
                full_name=full_name,
                email=email,
                mobile=mobile,
                city=city
            )
            messages.success(request, "Contact form submitted successfully!")
        else:
            messages.error(request, "Please fill all the fields.")

        return redirect('/')  

    return redirect('/')  


# ----------------------------
# Newsletter Subscribe
# ----------------------------
def subscribe_newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if email:
            if not Subscriber.objects.filter(email=email).exists():
                Subscriber.objects.create(email=email)
                messages.success(request, "Subscribed successfully!")
            else:
                messages.info(request, "You are already subscribed.")
        else:
            messages.error(request, "Please enter a valid email.")

        return redirect('/')  

    return redirect('/')
