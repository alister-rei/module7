from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class MainPage(TemplateView):
    template_name = 'main/main.html'
    extra_context = {
        'title': 'Sky-Pro'
    }


class ContactsPageView(View):
    def get(self, request):
        context = {'title': 'Контакты'}
        return render(request, 'main/contacts.html', context)

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"name:{name}, phone:{phone}, message:{message}")
        context = {'title': 'Контакты'}
        return render(request, 'catalog/contacts.html', context)
