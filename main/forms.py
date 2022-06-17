#from attr import field
from django import forms

from . import models


class CreateNewList(forms.Form):
    name=forms.CharField(label="Name",max_length=200)

"""class DeleteList(forms.Form):
    def __init__(self,maxValue:int, *args, **kwargs):
        super(DeleteList, self).__init__(*args, **kwargs)
        self.fields['id'] = forms.IntegerField(label="Enter id",min_value=1,max_value=maxValue)
    id = forms.IntegerField()    
"""
