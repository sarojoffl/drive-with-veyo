from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Job, Blog, ContactMessage, TeamMember
from .forms import ContactForm, UserForm
from django.core.paginator import Paginator
from django.conf import settings
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout

def index(request):
    blogs = Blog.objects.order_by('-created_at')[:3]
    return render(request, 'main/index.html', {'blogs': blogs})

def about(request):
    return render(request, 'main/about.html')

def faq(request):
    return render(request, 'main/faq.html')

def team(request):
    team_members = TeamMember.objects.all()
    return render(request, 'main/team.html', {'team_members': team_members})

def career(request):
    jobs = Job.objects.all()
    return render(request, 'main/career.html', {'jobs': jobs})

def blog(request):
    blogs = Blog.objects.all().order_by('-created_at')

    paginator = Paginator(blogs, 3)  # Show 3 blogs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'main/blog.html', {'page_obj': page_obj})

def blog_details(request, id):
    blog = get_object_or_404(Blog, id=id)
    latest_blogs = Blog.objects.exclude(id=id).order_by('-created_at')[:4]
    return render(request, 'main/blog_details.html', {'blog': blog, 'latest_blogs': latest_blogs})

def contact(request):
    context = {
        'RECAPTCHA_PUBLIC_KEY': settings.RECAPTCHA_PUBLIC_KEY
    }

    if request.method == 'POST':
        form = ContactForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            context['success'] = True
        else:
            # Check if the error is related to reCAPTCHA
            captcha_errors = form.errors.get('captcha')
            if captcha_errors:
                error_text = str(captcha_errors[0])
                if 'This field is required' in error_text:
                    context['error'] = "Please complete the reCAPTCHA."
                else:
                    context['error'] = "Invalid reCAPTCHA. Please try again."
            else:
                context['error'] = "There was an error with your submission. Please check the form."
    else:
        context['form'] = ContactForm()

    return render(request, 'main/contact.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup_success')
    else:
        form = UserForm()

    return render(request, 'main/signup.html', {'form': form})

def signup_success(request):
    return render(request, 'main/signup_success.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            return render(request, 'main/login.html', {'error': 'Invalid username or password.'})
    else:
        if request.user.is_authenticated:
            return redirect('index')
        return render(request, 'main/login.html')
    
def user_logout(request):
    auth_logout(request)
    return redirect('index')