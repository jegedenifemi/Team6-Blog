from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import BadHeaderError, send_mail
from django.db.models.query_utils import Q
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.http import HttpResponse,HttpResponseRedirect
from .token import account_activation_token
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from post.models import Post

# Create your views here.

@login_required
def bookmarks_Add(request, id):
    pass
    # post = get_object_or_404(Post, pk=id)
    # if post.bookmarks.filter(id=request.user.id).exists():
    #     post.bookmarks.remove(request.user)
    # else:
    #     post.bookmarks.add(request.user)
    return redirect('post:bookmarks')


    
# this view signs up a new writer to the database and sends a success message
def _sign_up(request):
    if request.user.is_authenticated:
        return redirect('post:index')
    else:
        form = CreateUserForm
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save(commit = False)
                user.is_active = False
                user.save()
                # getting the domain of the current site
                current = get_current_site(request)
                subject = "Activation link for your account with Tech Phantoms"
                email_template_name = "./accounts/user_confirmation.txt"
                c = {
                "email":user.email,
                'domain':current.domain,
                'site_name': 'Tech Phantoms',
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "user": user,
                'token': account_activation_token.make_token(user),
                'protocol': 'http',
                }
                email = render_to_string(email_template_name, c)
                to_email = form.cleaned_data.get('email')
                try:
                    send_mail(subject, email, 'afariogun.john2002@gmail.com' , [to_email], fail_silently=False)
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
					
                
                return redirect('login')
            
            
        else:
            form = CreateUserForm
        context = {'form': form}
        return render(request, 'accounts/signup_john.html', context)


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    
    if user is not None and account_activation_token.check_token(user,token):
        user.is_active = True
        user.save()
        return redirect('post:index')
    else:
        return HttpResponse('Activation link is invalid')



def _log_in(request):
    if request.user.is_authenticated:
        return redirect('post:index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('post:index')
            else:
                messages.info(request, "Username or Password is incorrect")
    
    context ={}

    return render(request, 'accounts/login_john.html', context)

# @login_required(login_url='login/')
def _log_out(request):
    logout(request)
    return redirect('login')


def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "./accounts/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Tech Phantoms',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'afariogun.john2002@gmail.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ('password_reset_done')#!

	password_reset_form = PasswordResetForm()
  
	return render(request=request, template_name="accounts/password_reset.html", context={"password_reset_form":password_reset_form},)


