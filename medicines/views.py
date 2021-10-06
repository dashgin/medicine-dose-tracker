from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)

from medicines.forms import MedicineForm
from medicines.models import Medicine


class MedicineListView(ListView):
    model = Medicine
    template_name = 'index.html'
    context_object_name = 'medicines'


medicine_list = MedicineListView.as_view()


class MedicineCreateView(CreateView):
    model = Medicine
    form_class = MedicineForm
    template_name = 'index.html'


medicine_create = MedicineCreateView.as_view()


class MedicineDetailView(DetailView):
    model = Medicine
    context_object_name = 'medicine'
    template_name = 'index.html'


medicine_detail = MedicineDetailView.as_view()


class MedicineUpdateView(UpdateView):
    model = Medicine
    form_class = MedicineForm
    template_name = 'index.html'


medicine_update = MedicineUpdateView.as_view()


class MedicineDeleteView(DeleteView):
    model = Medicine
    template_name = 'index.html'
    success_message = 'medicine deleted'
    success_url = '/'


medicine_delete = MedicineDeleteView.as_view()
