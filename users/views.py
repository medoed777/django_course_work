from django.contrib import auth, messages
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.defaults import permission_denied

from users.models import User
from users.services import generate_token, send_activation_email


def logout_user(request):
    logout(request)
    return redirect(reverse("main:home"))


def chk_token(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("main:home"))


def registration(request):
    if request.method == "POST":
        email = request.POST.get("email-username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if not email or not password or not password2:
            messages.error(request, "Все поля обязательны для заполнения")
            return redirect(reverse("main:home"))

        if password != password2:
            messages.error(request, "Пароли не совпадают")
            return redirect(reverse("main:home"))

        if User.objects.filter(email=email).exists():
            messages.error(request, "Пользователь с таким email уже существует")
            return redirect(reverse("main:home"))

        try:
            token = generate_token()
            user = User.objects.create(
                email=email,
                token=token,
                password=make_password(password),
                is_active=False,
            )
            send_activation_email(request.get_host(), user, token)
            messages.success(request, "Регистрация прошла успешно, подтвердите почту!")
            return redirect(reverse("main:home"))
        except Exception as e:
            messages.error(request, f"Ошибка при регистрации: {str(e)}")
            return redirect(reverse("main:home"))
    return redirect(reverse("main:home"))


def form_auth(request):
    return render(request, "auth.html")


def form_reg(request):
    return render(request, "reg.html")


def login_user(request: HttpRequest):
    chk_post = request.POST
    if chk_post:
        email = chk_post.get("email-username")
        password = chk_post.get("password")
        user = auth.authenticate(request, email=email, password=password)
        if user:
            auth.login(request, user)
        else:
            messages.error(request, "Пользователь не найден!")
            return redirect(reverse("main:home"))
    return redirect(reverse("main:home"))
