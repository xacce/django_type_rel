from django.views.generic import ListView
from django.shortcuts import Http404, HttpResponse


class Items(ListView):
    template_name = None
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        from django.db import models
        from django.shortcuts import Http404, HttpResponse
        from django.utils.simplejson import dumps

        result = []
        data = self.request.POST.get('for', None)

        try:
            from_model, to_model, field_name, pk = data.split("-")
        except ValueError:
            raise Http404('Data is not valid')

        from_model = models.get_model(*from_model.split('.'))
        to_model = models.get_model(*to_model.split('.'))
        for x in to_model.objects.filter(**{"%s_id" % field_name: pk}).all():
            result.append({"pk": x.pk, "value": unicode(x)})

        return HttpResponse(dumps(result), content_type="application/json")
