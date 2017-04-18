from inv.models import Item
from django.forms import ModelForm

class ItemCreateForm(ModelForm) :
    class Meta:
        model = Item
        fields = ['name','description','place_occupe']

class ItemUpdateForm(ModelForm) :
    class Meta:
        model = Item
        fields = ['name','description','place_occupe']

class ItemDeleteForm(ModelForm) :
    class Meta:
        model = Item
        fields = ['name']