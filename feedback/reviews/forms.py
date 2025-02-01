from django import forms
from .models import Review


# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your Name",
#                                  max_length=100,
#                                  error_messages={
#                                      "required":"Your name must be entered",
#                                      "max_length":"Please enter a shorter"
#                                  })
#     review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta: #nest class by django.. tells if which model the class should be related
        model = Review  # WE don't instantite this. WThis points to the review form to the review Model
        #possible where you have a model that you don't need them all rendered in a field
        fields = ['user_name', 'review_text', 'rating'] # list of fields to be included
        #if you want all fields use. this doesn't include ID
        #fields = '__all__' 
        #can exclude all used with __all__
        #exclude = ['owner_comment']
        #labels are used to maps the models to label values
        labels = {
            "user_name":" Your Name",
            "review_text": "Your feedback",
            "Rating": "Your Rating"
        }
        error_message = {
            "user_name":{
                "required":"Your Name must be added",
                "max_length": "can't be longer than 100",
                

            }
        }
