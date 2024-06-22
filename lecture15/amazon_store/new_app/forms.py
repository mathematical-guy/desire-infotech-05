from django import forms

from new_app.models import Phone


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = "__all__"

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise forms.ValidationError("Negative nahi hota be")
        return price
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name == 'iPhone':
            raise forms.ValidationError("Iphone naam ka phone mat daalo please")
        return name