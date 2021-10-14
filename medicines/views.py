from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView
)

from medicines.forms import MedicineForm
from medicines.models import Medicine
from .decorators import check_for_owner


@login_required
def medicine_create(request):
    form = MedicineForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        medicine_object = form.save()
        context['form'] = MedicineForm()
        context['object'] = medicine_object
        context['created'] = True
        return render(request, "medicines/create.html", context=context)
    return render(request, "medicines/create.html", context=context)


class MedicineDetailView(DetailView):
    model = Medicine
    context_object_name = 'medicine'
    template_name = 'medicines/detail.html'


medicine_detail = MedicineDetailView.as_view()


@login_required
@check_for_owner
def medicine_edit(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    form = MedicineForm(request.POST or None, instance=medicine)
    context = {"form": form}
    if form.is_valid():
        medicine_object = form.save()
        context['form'] = MedicineForm(instance=medicine)
        context['object'] = medicine_object
        context['edited'] = True
        return render(request, "medicines/edit.html", context=context)
    return render(request, "medicines/edit.html", context=context)


class MedicineDeleteView(DeleteView):
    model = Medicine
    template_name = 'medicines/delete.html'
    success_message = 'medicine deleted'
    context_object_name = 'object'

    def get_success_url(self):
        return reverse('medicines:list')


medicine_delete = MedicineDeleteView.as_view()


class MedicineListView(ListView):
    model = Medicine
    template_name = 'index.html'
    context_object_name = 'medicines'


medicine_list = MedicineListView.as_view()
