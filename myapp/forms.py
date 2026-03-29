from django import forms


class CreateNewTask(forms.Form):
    title = forms.CharField(label="Task Title", max_length=200)
    description  = forms.CharField(label="Task Description", required=False, widget=forms.Textarea)


class CreateNewTaskForm(forms.Form):
    name = forms.CharField(label="Project Name", max_length=200)