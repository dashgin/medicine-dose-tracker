from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from medicines.models import Medicine


def check_for_owner(view_func):
    def wrap(request, *args, **kwargs):
        medicine = get_object_or_404(Medicine, pk=kwargs['pk'])
        if request.user == medicine.user:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse("You are not owner of this", status=401)

    return wrap
