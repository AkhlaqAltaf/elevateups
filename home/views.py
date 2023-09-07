from django.shortcuts import render
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives

from twisted.mail.smtp import sendmail
# Create your views here.
from home.models import Contact
def home(request):
    # return HttpResponse('home')
    # messages.success(request,'Welcome to my website nice to see you!!')
    return render(request,'home/index.html')

import string  
    
# Storing the sets of punctuation in variable result  
punc = string.punctuation  
def contact(request):
    # return HttpResponse('contact')
    if request.method=="POST":
        print('post')
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        content = request.POST['content']
        print(name,email,content,number)
        if len(name) >1 and len(name) < 30:
            pass
        else:
            messages.error(request,'length of Name should be greater than 2 and less than 30')
            return render(request,'home/contact.html')

        if len(email) >1 and len(email) < 30:
            pass
        else:
            messages.error(request,'email is not correct try again!!')
            return render(request,'home/contact.html')
        print(len(number))
        if len(number) > 9 and len(number) < 13:
            pass
        else:
            messages.error(request,'number not correct try again!!')
            return render(request,'home/contact.html')
        ins = Contact(name=name,email=email,content=content,number=number)
        ins.save()
        send_package_details_email(email , content , name)
        messages.success(request,'Thank You for contacting me!! Your message has been saved ')
        print('data has been saved to database')
    else:
        print('not post')
    return render(request,'home/contact.html')

def portfolio(request):
    # return HttpResponse('projects')
    return render(request,'home/portfolio.html')
def worksample(request):
    # return HttpResponse('projects')
    return render(request,'home/worksample.html')

def djangoProjects(request):
    return render(request,'home/django.html')





  
def send_package_details_email(recipient_email,message , name):
        # Create an EmailMultiAlternatives object

        messages = "WeCanDo Lab user Want to Contact With You          name : "+name+"   email : "+recipient_email+ "      Message : "+message 
        email = EmailMultiAlternatives(
            "We Can Do Lab ",
            messages,
            "jongleship@gmail.com",
            ['akhlaqaltaf4@gmail.com' ,'merndeveloper123@gmail.com', 'rimshamuneer126@gmail.com'],
        )


        # Send the email
        email.send()