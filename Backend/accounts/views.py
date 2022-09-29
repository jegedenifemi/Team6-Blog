from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import BadHeaderError, send_mail
from django.db.models.query_utils import Q
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.http import HttpResponse
# Create your views here.

# this view signs up a new writer to the database and sends a success message
def _sign_up(request):
    if request.user.is_authenticated:
        return redirect('post:index')
    else:
        form = CreateUserForm
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                # This gets sent to the admin login page, debug later
                messages.success(request, "Account was created successfully for " + username)
            
                return redirect('login')
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)


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

    return render(request, 'accounts/login.html', context)


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

