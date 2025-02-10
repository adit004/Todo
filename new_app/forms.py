from django import forms

from new_app.models import Todo

class DateInput(forms.DateInput):
    input_type = 'date'

class TodoForms(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = Todo
        fields = ('event_name','discription','date')
        # exclude = ('date',)
