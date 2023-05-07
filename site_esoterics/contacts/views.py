from django.shortcuts import render

from contacts.models import Contact
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.forms import BlogForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import django
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

class  ContactListView(ListView):
    model = Contact
    
   # template_name = 'contacts/contat_list.html'

# Функция формы обратной связи
'''
def contactform(reguest):
    if reguest.method == 'POST':
        form = ContactForm(reguest.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            copy = form.cleaned_data['copy']

            recepients = ['myemail@gmail.com']
            # Если пользователь захотел получить копию себе, добавляем его в список получателей
            if copy:
                recepients.append(sender)
            try:
                send_mail(subject, message, 'myemail@gmail.com', recepients)
            except BadHeaderError: #Защита от уязвимости
                return HttpResponse('Invalid header found')
            # Переходим на другую страницу, если сообщение отправлено
            return HttpResponseRedirect('/blog/thanks/')

    else:
        form = ContactForm()
    # Выводим форму в шаблон
    return render(reguest, 'contact.html', {'form': form, 'username': auth.get_user(reguest).username})'''

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


def contact(request):
    errors = []
    form = {}
    contact = Contact()

    if request.POST:
         
        form['name'] = request.POST.get('name')
        form['email'] = request.POST.get('email')
        form['phone'] = request.POST.get('phone')
        form['message'] = request.POST.get('message')
         
        if not form['name']:
            errors.append('Заполните имя')
        if '@' not in form['email']:
            errors.append('Введите корректный e-mail')
        if not form['message']:
            errors.append('Введите сообщение')
             

        contact.name = request.POST.get('name')
        contact.email = request.POST.get('email')
        contact.phone = request.POST.get('phone')
        contact.message = request.POST.get('message')
           

        contact.save()
        messages.success(request, "New sample is added successfully!")
        return render(request, 'contacts/contacts_list.html', {'errors': errors, 'name': form.name}, {'email': form.email},{'phone': form.phone},{'message':form.message})
        if not errors:
            # ... сохранение данных в базу
           # return HttpResponse('Спасибо за ваше сообщение!')
         
            return render(request, 'contacts_list.html', {'errors': errors, 'form':form})
        



def postuser(request):
    # получаем из данных запроса POST отправленные через форму данные
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
    #return HttpResponse(f"<h2>Name: {name}  Age: {email} phone: {phone} message:{message}</h2>")
    return render(request, 'contacts/success.html')



class ContactCreateView(UserPassesTestMixin, CreateView):
    model = Contact
    
    success_url = '/news'

    def test_func(self):
        return self.request.user.is_staff