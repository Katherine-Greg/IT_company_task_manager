from django import forms
from django.contrib.auth.forms import UserCreationForm

from task_manager.models import Task, Position, Worker


class RegisterForm(UserCreationForm):
    class Meta:
        model = Worker
        fields = ("first_name", "last_name", "position", "username", "password1", "password2")


class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "assignees": forms.CheckboxSelectMultiple(),
            "deadline": forms.DateInput(attrs={"type": "date"}),
        }


class TaskSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name"
            }
        )
    )


class WorkerSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by username"
            }
        )
    )


class WorkerUpdateForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ("first_name", "last_name", "position", "username")


class PositionCreationForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = "__all__"


class PositionSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name"
            }
        )
    )
