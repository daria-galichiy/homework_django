from django.shortcuts import render, HttpResponseRedirect, render_to_response
from django.views.generic import ListView, DetailView
from lab6.apps.db_app.models import *
from django.contrib.auth.models import User
from lab6.apps.db_app.registration import *
from django.contrib import auth
from django.contrib.auth import authenticate
from django.views.generic.edit import CreateView
from django.forms.models import ModelForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.paginator import Paginator

# Create your views here.


def main(request, page_number=1):
    films_all = Films.objects.all()
    current_page = Paginator(films_all, 2)
    return render_to_response('main_page.html', {'films': current_page.page(page_number)})


class FilmDetailView(DetailView):
    model = Films
    context_object_name = 'film'
    template_name = 'film.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comments.objects.all()
        return context

    def get_object(self):
        object = super(FilmDetailView, self).get_object()
        return object


def film(request, film_id=1):
    return render(request, 'film.html', {'film': Films.objects.get(film_id=film_id), 'comments': Comments.objects.filter(comment_film_id=film_id)})


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        exclude = ['comment_id']


class CommentCreate(CreateView):
    form_class = CommentForm
    template_name = 'film.html'

    def post(self, request):
        print(request.FILES)
        return super().post(request)

    def get(self, request):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect('/hw_app/main/')
        return super().get(request)



def registration2(request):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = User.objects.create_user(username=request.POST.get('username'),
                                            email=request.POST.get('email'),
                                            password=request.POST.get('password'),
                                            last_name=request.POST.get('surname'),
                                            first_name=request.POST.get('firstname'))
            return HttpResponseRedirect('/hw_app/login/')
        else:
            form = RegistrationForm()
    return render(request, 'registration2.html', {'form': form})


def login(request):
    error = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect('/hw_app/main/')
        else:
            error = "Неверный логин или пароль."
    return render(request, 'login.html', locals())


def account(request):
    return render(request, 'account.html')


def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')
