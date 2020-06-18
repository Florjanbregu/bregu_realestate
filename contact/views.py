from django.shortcuts import render,redirect
from django.core.mail import send_mail

from .models import Contact

# CONTACT FUNCTION
def index(request):

    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        
    
        
        # nese cdo gje shkon ok atehere duhet te krijojme userin
        contact = Contact(name=name, phone=phone, email=email, message=message)
        # nese cdo gje shkone mire atehere e ruajm
        contact.save()


        # pasi cdo gje ka shkuar mire mund te dergojme nje email
        send_mail(
            'Pyetje për Pronën e listuar!',
            'Ktu eshte nje pyetje për ' + name + '. Logohu tek faqja e adminit për me shume info',
            'floribregu6@gmail.com',
            ['floribregu6@gmail.com'],
            fail_silently=False
        )


    return render(request, 'contact/contact.html')

