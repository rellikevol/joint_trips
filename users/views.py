from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from users.forms import RegistrationForm
from django.forms.utils import ErrorDict


# Create your views here.
def profile(request):
    queryset = User.objects.all()

    if request.user in queryset:
        print("Catch")
    return render(request, 'users/profile.html')


def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)

        context = {'form': user_form,
                   'username': request.POST.get('username'),
                   'email': request.POST.get('email')}

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password2'])
            new_user.save()
            return redirect('register-done')
        else:
            errors = []
            for i in user_form.errors:
                for x in user_form.errors[i]:
                    errors.append(x)

            context['errors'] = errors
            return render(request, 'registration/register_page.html', context)
    else:
        user_form = RegistrationForm()
        return render(request, 'registration/register_page.html', {'form': user_form})


def register_done(request):
    return render(request, 'registration/register_done.html')