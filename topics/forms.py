from django import forms
    
class CreateTopicForm(forms.Form):
    topic = forms.CharField(max_length=255, widget=forms.Textarea, help_text='255 characters max.')
