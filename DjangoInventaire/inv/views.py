from django.shortcuts import render


# Create your views here.
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import LoginView
from inv.models import Item
from inv.forms import ItemCreateForm
from inv.forms import ItemUpdateForm
from inv.forms import ItemDeleteForm

class ItemListView(ListView):
    model = Item
    context_object_name = "items"
    template_name = "inv/items-list.html"
    paginate_by = None


class ItemRetrieveView(DetailView):
    model = Item
    context_object_name = 'item'
    template_name = "inv/item-detail.html"

class ItemCreateView(CreateView):
    model = Item
    form_class = ItemCreateForm
    template_name = "inv/item-create.html"

    def get_initial(self):
        return {'name': self.request.user.member,
                'description': self.request.user.member,
                'place_occupe': self.request.user.member}

class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemUpdateForm
    template_name = "inv/item-update.html"

    def get_initial(self):
        return {'name': self.request.user.member,
                'description': self.request.user.member,
                'place_occupe': self.request.user.member}

class ItemDeleteView(DeleteView):
   model = Item
    #form_class = ItemDeleteForm
   template_name = "inv/item-delete.html"
   success_url = "/"

class ItemLoginview(LoginView):
    model = Item
    template_name = "inv/item_login.html"