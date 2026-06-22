from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from account.forms import CustomUserCreationForm

def register_view(request):
    if request.user.is_authenticated:
        # Если пользователь уже авторизован, перенаправляем его
        return redirect('profile')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Автоматически авторизуем пользователя после регистрации
            login(request, user)
            messages.success(
                request,
                f'Добро пожаловать, {user.get_full_name()}! Ваш аккаунт успешно создан.'
            )
            return redirect('profile')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме')
    else:
        form = CustomUserCreationForm()

    return render(request, 'account/register.html', {'form': form})

# @login_required
# def profile_view(request):
#     return render(request, 'account/profile.html', {'user': request.user})