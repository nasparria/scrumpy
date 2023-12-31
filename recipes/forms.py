from django import forms


from recipes.models import Recipe, Rating


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ["value"]
