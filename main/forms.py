#from attr import field
from django import forms

from . import models
#from bootstrap_datepicker_plus import DatePickerInput #old version.
#from bootstrap_datepicker_plus.widgets import DatePickerInput


from datetime import date  #trying to validate - to make it work with only future dates.

class CreateNewList(forms.Form):
    name=forms.CharField(label="Name",max_length=200)
    

choices = (
    ("category1", "category1"),
    ("category2", "category2"),
    ("category3", "category3"),
    ("category4", "category4"),
    ("category5", "category5"),
)

#tring to mkae this method work as a direct validator 
def present_or_future_date(value):
    if value < date.today():
        raise forms.ValidationError("The date cannot be in the past! ps:it's a due date!")
        #decided to handle validation error message via custom handles
        #this idea on hold.
        #raise forms.ValidationError("")
    return value

class CreateNewItem(forms.Form):
    title=forms.CharField(label="Title",max_length=100)
    description=forms.CharField(label="Description",max_length=250)
    category = forms.TypedChoiceField(choices=choices,coerce=str)
    due_date = forms.DateField(widget = forms.SelectDateWidget,validators=[present_or_future_date])
    image1 = forms.ImageField(label="Image1")
    image2 = forms.ImageField(label="Image2")
    image3 = forms.ImageField(label="Image3") 
    """
    #this method works , trying for something similar
    def clean_date(self):
        date = self.cleaned_data['date']
        if date < date.today():
            raise forms.ValidationError("The date cannot be in the past!")
        return date
    """
    
"""class DeleteList(forms.Form):
    def __init__(self,maxValue:int, *args, **kwargs):
        super(DeleteList, self).__init__(*args, **kwargs)
        self.fields['id'] = forms.IntegerField(label="Enter id",min_value=1,max_value=maxValue)
    id = forms.IntegerField()    
"""
