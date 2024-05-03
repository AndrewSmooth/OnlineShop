from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required

from users.forms import UserRegisterForm, UserLoginForm, UserProfileForm


def account(request):
    return render(request, 'users/account.html', {"register_form": UserRegisterForm(), "login_form": UserLoginForm()})


def login(request):
    if request.method == 'POST':
        
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            # session_key = request.session.session_key

            if user:
                auth.login(request, user)

                # if session_key:
                    # Cart.objects.filter(session_key=session_key).update(user=user)
                    
                return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserLoginForm()
        print("Не POST login")

    context = {
        'title': 'Home - Авторизация',
        'form': form
    }
    return render(request, 'users/account.html', context)
    # return HttpResponseRedirect(reverse('main:index'))


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)

        if form.is_valid():
            form.save()

            # session_key = request.session.session_key

            user = form.instance
            auth.login(request, user)

            # if session_key:
            #     Cart.objects.filter(session_key=session_key).update(user=user)
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserRegisterForm()
        print('Не POST')

    context = {
        'title': 'Onlineshop - Регистрация',
        'form': form
    }
    return render(request, 'users/account.html', context)
        
    # return HttpResponseRedirect(reverse_lazy('main:index'))

# @login_required
# def profile(request):
#     user = request.user
#     context = {
#         "user": user,
#         }
#     return render(request, 'users/profile.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = UserProfileForm(instance=request.user)

    # orders = Order.objects.filter(user=request.user).prefetch_related(
            #     Prefetch(
            #         "orderitem_set",
            #         queryset=OrderItem.objects.select_related("product"),
            #     )
            # ).order_by("-id")
        

    context = {
        'title': 'Home - Кабинет',
        'form': form,
        # 'orders': orders,
    }
    return render(request, 'users/profile.html', context)

# def users_cart(request):
#     return render(request, 'users/users_cart.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))