from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
from .models import Finch, Photo
from .forms import LifestyleForm
S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'finches11'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def finches_index(request):
  finches = Finch.objects.filter(user=request.user)
  return render(request, 'finches/index.html', { 'finches': finches })

@login_required
def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  lifestyles_form = LifestyleForm()

  return render(request, 'finches/detail.html',
   { 'finch': finch, 'lifestyles_form': lifestyles_form })


@login_required
def add_lifestyle(request, finch_id):
  form = LifestyleForm(request.POST)
  if form.is_valid():
    new_lifestyle = form.save(commit=False)
    new_lifestyle.finch_id = finch_id
    new_lifestyle.save()
  return redirect('detail', finch_id=finch_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class FinchCreate(LoginRequiredMixin, CreateView):
  model = Finch
  fields = ['species', 'description']

  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)


class FinchUpdate(LoginRequiredMixin, UpdateView):
  model = Finch
  fields = ['species', 'description']

class FinchDelete(LoginRequiredMixin, DeleteView):
  model = Finch
  success_url = '/finches/' 

@login_required
def add_photo(request, finch_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, finch_id=finch_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', finch_id=finch_id)
