from django.shortcuts import render, redirect
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST

from users.models import Profile, Chat, Message
from users.forms import RegistrationForm, ProfileForm, ChangeUserForm
from django.contrib.auth.forms import UserChangeForm
from django.http import JsonResponse
import json


# Create your views here.
def profile(request, pk):
    if not request.user.is_authenticated:
        return redirect('not-register')

    user_profile = Profile.objects.get(pk=pk)

    return render(request, 'users/profile.html', context={'profile': user_profile})


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
            return redirect('profile', request.user.user_profile.id)
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


def chat(request, pk):

    if not request.user.is_authenticated:
        return redirect('not-register')

    chat = Chat.objects.get(pk=pk)
    user_profile = Profile.objects.get(base_user=request.user)
    riciver = 0

    messages = chat.messages.filter(recipient=user_profile, is_read=False)

    for i in messages:
        i.is_read = True
        i.save()

    for i in chat.members.all():
        if i.id != request.user.id:
            riciver = i

    if user_profile in chat.members.all():
        return render(request, 'users/chat.html', context={'id': pk, 'riciver': riciver,
                                                           'who': request.user.id})
    else:
        return redirect('profile', user_profile.id)


def get_chat(request, pk):
    chat = Chat.objects.get(pk=pk).messages.all()

    data = []
    for i in chat.order_by('pk'):
        data.append({'sender': i.sender.base_user.username,
                     'sender_id': i.sender.base_user.id,
                     'recipient': i.recipient.base_user.username,
                     'date': i.date, 'time': i.time, 'message': i.text})
    return JsonResponse(data, safe=False)


@ensure_csrf_cookie
@require_POST
def append_message(request, pk):
    try:
        data = json.loads(request.body)
        message = data.get('user_message', None)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Ошибка в данных JSON.'}, status=400)

    if message is None:
        return JsonResponse({'error': 'Ошибка в данных JSON.'}, status=400)

    chat = Chat.objects.get(pk=pk)
    queryset = chat.members.all()
    recipient = 0
    for i in queryset:
        if i.base_user.id != request.user.id:
            recipient = i
    message = Message.objects.create(sender=Profile.objects.get(base_user=request.user.id), recipient=recipient,
                                     text=message)
    message.save()
    chat.messages.add(message)
    chat.save()
    return JsonResponse({'message': 'Сообщение доставлено.'}, status=200)


def create_chat(request):
    riciver_id = request.POST.get('riciver_id')
    chats = Chat.objects.all()
    riciver = Profile.objects.get(pk=riciver_id)
    user_profile = Profile.objects.get(base_user=request.user)

    for i in chats:
        if riciver in i.members.all() and user_profile in i.members.all():
            return redirect('chat', i.id)

    new = Chat.objects.create()
    new.members.add(riciver)
    new.members.add(user_profile)
    new.save()

    return redirect('chat', new.id)


def my_messages(request):
    if not request.user.is_authenticated:
        return redirect('not-register')

    chats = Chat.objects.all()
    profile = Profile.objects.get(base_user=request.user)
    my_chats = []
    for i in chats:
        profiles = i.members.all()
        if profile in profiles:
            reciver = 0
            for x in profiles:
                if x.base_user != request.user:
                    reciver = x
            chat_user = {'chat': i.id, 'reciver': reciver,
                         'unread': len(i.messages.filter(recipient=profile, is_read=False))}
            my_chats.append(chat_user)

    return render(request, 'users/my_messages.html', {'my_chats': my_chats})
