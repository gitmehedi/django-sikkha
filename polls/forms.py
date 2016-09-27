from django import forms


class QuestionForm(forms.Form):
    question_text = forms.CharField(label="Question Tile", max_length=120)
    pub_date = forms.DateField(label='Publish Date')




class ChoiceForm(forms.Form):
    question = forms.CharField(label="Title", max_length=120)
    votes = forms.IntegerField(label="Votes")


