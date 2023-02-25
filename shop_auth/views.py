from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .models import ShopUser
from .forms import ShopUserCreateForm


# Create your views here.

class CreateShopUser(CreateView):
    model = ShopUser
    form_class = ShopUserCreateForm    
    template_name = 'auth/user_create.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = ShopUserCreateForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            password_confirm = form.cleaned_data['password_confirm']
            if password != password_confirm:
                return render(request, self.template_name)
            else:
                return self.form_valid(form)
        else:
            return render(request, self.template_name)
    
    def form_valid(self, form):
        return super().form_valid(form)
    

class ShopLoginView(TemplateView):
    template_name = 'auth/login.html'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            context = {'error':'이메일주소와 비밀번호를 올바르게 입력하세요'}
            return render(request, self.template_name, context)
        

def shop_logout(request):
    logout(request)
    return redirect('/')