from inv.models import Item
from django.forms import ModelForm

class ItemCreateForm(ModelForm) :
    class Meta:
        model = Item
        fields = ['name','description','place_occupe','inventaire']

class ItemUpdateForm(ModelForm) :
    class Meta:
        model = Item
        fields = ['name','description','place_occupe','inventaire']

class ItemDeleteForm(ModelForm) :
    class Meta:
        model = Item
        fields = ['name']