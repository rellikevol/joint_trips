from django.shortcuts import render, redirect
from users.models import Profile
from users.forms import RegistrationForm, ProfileForm, ChangeUserForm
from django.contrib.auth.forms import UserChangeForm


# Create your views here.
def profile(request):
    if not request.user.is_authenticated:
        return redirect('not-register')
    context = {}
    try:
        user_profile = Profile.objects.get(base_user=request.user.id)
        context = {'is_login': True,
                   'user_profile': user_profile,
                   'prefer_conversations': user_profile.get_prefer_conversations_display(),
                   'prefer_music': user_profile.get_prefer_music_display(),
                   'prefer_smoke': user_profile.get_prefer_smoke_display(),
                   'prefer_animals': user_profile.get_prefer_animals_display()}
    except Exception:
        context['is_login'] = False

    return render(request, 'users/profile.html', context=context)


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
            new_profile = Profile.objects.create(base_user=new_user)
            new_profile.save()
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


def not_register(request):
    return render(request, 'registration/not_register.html')


def edit_profile(request):

    if not request.user.is_authenticated:
        return redirect('not-register')

    if request.method == 'POST':
        user_form = ChangeUserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=Profile.objects.get(base_user=request.user.id))
        context = {'user_form': user_form, 'profile_form': profile_form}

        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
        else:
            errors = []

            for i in user_form.errors:
                for x in user_form.errors[i]:
                    errors.append(x)

            for i in profile_form.errors:
                for x in profile_form.errors[i]:
                    errors.append(x)

            context['errors'] = errors
            return render(request, 'users/edit_profile.html', context=context)

    user_form = ChangeUserForm(instance=request.user)
    profile_form = ProfileForm(instance=Profile.objects.get(base_user=request.user.id))

    context = {'user_form': user_form, 'profile_form': profile_form}

    return render(request, 'users/edit_profile.html', context=context)
