from django.shortcuts import render

from contacts.models import Contact
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.forms import BlogForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
# Create your views here.

from django.http import HttpResponse
import django
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

class  ContactListView(ListView):
    model = Contact
    
   # template_name = 'contacts/contat_list.html'

# Функция формы обратной связи


def success(request):
    email = request.POST.get('email', '')
    data = """
Hello there!

I wanted to personally write an email in order to welcome you to our platform.\
 We have worked day and night to ensure that you get the best service. I hope \
that you will continue to use our service. We send out a newsletter once a \
week. Make sure that you read it. It is usually very informative.

Cheers!
~ Yasoob
    """
    send_mail('Welcome!', data, "Yasoob",
              [email], fail_silently=False)
    return render(request, 'success.html')



        



def postuser(request):
    # получаем из данных запроса POST отправленные через форму данные
    if request.method == "POST":

        contact = Contact()
        contact.name = request.POST.get("name", "Undefined")
        contact.email = request.POST.get("email", 1)
        contact.phone = request.POST.get("phone", 1)
        contact.message = request.POST.get("message", 1)
            
        contact.save()
        

    '''
     id = request.data['id'],    
    name = request.POST.get("name", "Undefined")
    email = request.POST.get("email", 1)
    phone = request.POST.get("phone", 1)
    message = request.POST.get("message", 1)
    send_mail('Вы отпраили сообщение',[name],[email],[phone],[message])
    contact = Contact()
    
    contact.name = request.POST.get('name')
    contact.email = request.POST.get('email')
    contact.phone = request.POST.get('phone')
    contact.message = request.POST.get('message')
    '''  
    #return HttpResponse(f"<h2>Name: {name}  Age: {email} phone: {phone} message:{message}</h2>")
    return render(request, 'contacts/success.html')



class ContactView(UserPassesTestMixin, ListView):
    model = Contact
    post = Contact.objects.all()
    #template_name = 'smContact.html'
    success_url = 'viewContact/'
    def test_func(self):
        return self.request.user.is_staff
    


def view (request):
    
    contact =  Contact.objects.all()
    print(contact)
    
    return render(request, 'contacts/smContact.html',{'contact':contact})

