from django import forms

class EventForm(forms.Form):

    name = forms.CharField(label="Name", max_length=25, required=True)
    venue = forms.CharField(label="Venue", max_length=25, required=True)
    description = forms.CharField(label="Description", max_length=100, help_text="Please provide a basic description of the event.", widget=forms.Textarea)
    start_time = forms.DateTimeField(label="Start Time", required=True)
    end_time = forms.DateTimeField(label="End Time", required=True)