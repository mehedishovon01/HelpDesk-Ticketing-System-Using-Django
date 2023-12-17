from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

# All views functions are beow.
def registration(request):
    """
    This function handles user registration by processing the registration form.
    If the user's http method is POST then it will create a new user otherwise it will show a registration from.
    HTTP Method: POST
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'auth/registration.html', {'form': form})

@login_required
def change_password(request):
    """
    This function allows a logged-in user to change their password.
    If the form is valid then save the form to update the user's password. Update the session authentication hash. Display a success message.
    And redirect the user back to the 'change_password' page. Otherwise, display an error message.
    HTTP Method: POST
    """
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'auth/change-password.html', {
        'form': form
    })

@login_required
# @permission_required('user.add_profile')
def dashboard(request):
    """
    This function renders the dashboard page for a logged-in user.
    It must needed to login user.
    HTTP Method: GET
    """
    return render(request, 'dashboard.html')

@login_required
def profile(request):
    """
    This function allows a logged-in user to update their profile information.
    If method is POST then Validate the submitted user update form (UserUpdateForm) and profile update form (ProfileUpdateForm).
    If both forms are valid save the user update form to update user details. Save the profile update form to update profile details.
    Redirect the user back to the 'profile' page. 
    And If not POST: Create instances of UserUpdateForm and ProfileUpdateForm for rendering the profile update form.
    It must needed to login user.
    HTTP Method: POST
    """
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profiledetails)
        if u_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profiledetails)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)