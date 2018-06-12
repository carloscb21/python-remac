#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.http import Http404
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views import View

from remac_portal.form import RegistrationForm, EditProfileForm


class RegisterView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'portal/register.html', context={'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('user:login'))
        return render(request, 'portal/register.html', context={'form': form})


class ProfileView(View):
    def get(self, request):
        try:
            user = User.objects.get(id=request.user.id)
            return render(request, 'backoffice/profile/profile.html', context={'user': user})
        except User.DoesNotExist:
            raise Http404


class ProfileEditView(View):
    def get(self, request):
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'backoffice/profile/edit_profile.html', args)

    def post(self, request):
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('portal:profile'))


class ChangePasswordView(View):
    def get(self, request):
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'portal/single_sign_on/change_password.html', args)

    def post(self, request):
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('portal:profile'))
        return redirect(reverse('user:change_password'))


def login_redirect(request):
    return redirect('/user/login')