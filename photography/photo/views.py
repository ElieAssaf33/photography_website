from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.core.mail import send_mail
from django.contrib import messages
from . import models
from .forms import ContactForm

def index(request:HttpRequest):
    # Get one photo from each category
    portrait_photo = models.Photos.objects.filter(category='portrait').first()
    nature_photo = models.Photos.objects.filter(category='nature').first()
    wedding_photo = models.Photos.objects.filter(category='wedding').first()
    street_photo = models.Photos.objects.filter(category='street').first()

    context = {
        'portrait_photo': portrait_photo,
        'nature_photo': nature_photo,
        'wedding_photo': wedding_photo,
        'street_photo': street_photo,
    }
    return render(request,'photo/index.html', context)

def portfolio(request:HttpRequest):
    # Get one photo from each category for the portfolio cards
    portrait_photo = models.Photos.objects.filter(category='portrait').first()
    nature_photo = models.Photos.objects.filter(category='nature').first()
    wedding_photo = models.Photos.objects.filter(category='wedding').first()
    street_photo = models.Photos.objects.filter(category='street').first()

    context = {
        'portrait_photo': portrait_photo,
        'nature_photo': nature_photo,
        'wedding_photo': wedding_photo,
        'street_photo': street_photo,
    }
    return render(request,'photo/portfolio.html', context=context)

def prices(request:HttpRequest):
    return render(request,'photo/prices.html', context={})

def contacts(request:HttpRequest):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Prepare email content
            email_subject = f'New Contact Form Submission: {subject}'
            email_message = f'''New message from {name} ({email})

{message}'''
            
            # Send email
            try:
                send_mail(
                    email_subject,
                    email_message,
                    'eliesamazingphotography@gmail.com',  # From email
                    ['eliesamazingphotography@gmail.com'],  # To email
                    fail_silently=False,
                )
                messages.success(request, 'Your message has been sent successfully!')
                return redirect('contacts')
            except Exception as e:
                messages.error(request, 'There was an error sending your message. Please try again later.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    return render(request, 'photo/contacts.html', {'form': form})

def wedding(request:HttpRequest):
    wedding_photos = models.Photos.objects.filter(category='wedding')
    context = {
        'wedding_photos': wedding_photos,
        'section_title': 'Wedding Photography',
        'section_description': 'Preserving precious moments of your special day with elegance and style.'
    }
    return render(request,'photo/wedding.html', context=context)

def nature(request:HttpRequest):
    nature_photos = models.Photos.objects.filter(category='nature')
    context = {
        'nature_photos': nature_photos,
        'section_title': 'Nature Photography',
        'section_description': 'Exploring the beauty of landscapes and wildlife through the lens.'
    }
    return render(request,'photo/nature.html', context=context)

def portrait(request:HttpRequest):
    portrait_photos = models.Photos.objects.filter(category='portrait')
    context = {
        'portrait_photos': portrait_photos,
        'section_title': 'Portrait Photography',
        'section_description': 'Capturing personalities and moments in stunning detail'
    }
    return render(request,'photo/portrait.html', context=context)

def street(request:HttpRequest):
    street_photos = models.Photos.objects.filter(category='street')
    context = {
        'street_photos': street_photos,
        'section_title': 'Street Photography',
        'section_description': 'Documenting urban life and candid moments in their raw authenticity.'
    }
    return render(request,'photo/street.html', context=context)


