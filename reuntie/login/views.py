from multiprocessing.spawn import import_main_path
from django.shortcuts import render
from .models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout
from reuntie import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage, send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from .forms import UpdateUserForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render (request,'login/index.html')

def signup(request):
    if request.method == "POST":
        # username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')
        myuser=User.objects.create_user(email=email,password=pass1,first_name=fname,last_name=lname)
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")

        return redirect('signin')  

    return render(request,'login/signup.html')

@receiver(signal=post_save,sender=User)
def mail_signal(sender,instance,created,**kwargs):
    if created:
        subject="Welcome to Reunite"
        message=f'Hello {instance.first_name} Welcome to reunite'
        from_email = settings.EMAIL_HOST_USER
        to_list = [instance.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

def signin(request):
    if request.method == 'POST':
        email= request.POST['email']
        pass1 = request.POST['pass1']
        user = authenticate(email=email, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('home')
    
    return render(request, "login/signin.html")

def signout(request):
    logout(request)
    messages.success(request,"Logged out Sucessfully")
    return redirect('home')

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            # profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('thanks')
    else:
        user_form = UpdateUserForm(instance=request.user)

    return render(request, 'login/profile.html', {'user_form': user_form})

def thanks(request):
    return render (request,'login/thanks.html')


@login_required
def create_post(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        pic = request.FILES.get('picture')
        try:
            post = Post.objects.create(creater=request.user, content_text=text, content_image=pic)
            return HttpResponseRedirect(reverse('index'))
        except Exception as e:
            return HttpResponse(e)
    else:
        return HttpResponse("Method must be 'POST'")    

