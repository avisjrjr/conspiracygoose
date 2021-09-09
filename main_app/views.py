from main_app.models import Conspiracy, Pic
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from datetime import date
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'something-about-birds'

class Home(LoginView):
  template_name = 'home.html'

class List(ListView):
  model= Conspiracy

class Login(LoginView):
  template_name = 'login.html'
  redirect_field_name='home'
  redirect_authenticated_user=True

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('about')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
  
def about(request):
  return render(request, 'about.html')

def conspiracy_detail(request, pk):
  conspiracy = Conspiracy.objects.get(id = pk)
  return render(request, 'conspiracy/conspiracy_detail.html', 
  {'conspiracy': conspiracy})

@login_required
def add_pic(request, pk):
  pic_file = request.FILES.get('pic-file', None)
  if pic_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex + pic_file.name[pic_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(pic_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      conspiracy = Conspiracy.objects.get(id = pk)
      pic = Pic(url=url, conspiracy=conspiracy)
      conspiracy_pic = Pic.objects.filter(conspiracy=pk)
      if conspiracy_pic.first():
        conspiracy_pic.first().delete()
      pic.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('conspiracy_detail', pk=pk)

class ConspiracyCreate(LoginRequiredMixin, CreateView):
  model = Conspiracy
  fields=['title', 'description' ]

  def form_valid(self, form):
    form.instance.author = self.request.user
    form.instance.date = date.today()
    return super().form_valid(form)

class ConspiracyUpdate(LoginRequiredMixin, UpdateView):
  model = Conspiracy
  fields = ['title', 'description']

class ConspiracyDelete(LoginRequiredMixin, DeleteView):
  model = Conspiracy
  success_url = '/'

# nothin