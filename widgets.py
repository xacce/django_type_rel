from django import forms
from django.forms import fields
from django.contrib.admin import widgets
from django.templatetags.static import static
from django.utils.html import mark_safe


class TypeRelWidget(widgets.AdminTextInputWidget):
    def __init__(self, model, to_model, rel_rel_name, admin, *args, **kwargs):
        self.from_model, self.admin, self.to_model, self.rel_rel_name = model, admin, to_model, rel_rel_name
        self.objects = admin.dtr_root_qs(to_model, rel_rel_name)
        super(TypeRelWidget, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None):
        from django.core.urlresolvers import reverse

        key = "%s.%s-%s.%s-%s" % (
            self.from_model._meta.app_label, self.from_model.__name__,
            self.to_model._meta.app_label, self.to_model.__name__,
            self.rel_rel_name
        )

        default_query = ''
        if value:
            to_object = self.to_model.objects.get(pk=value)
            default_query = ("%s-%s" % (key, getattr(to_object, "%s_id" % self.rel_rel_name)))

        options = ''u"".join([u"<option value='%s-%s'>%s</option>" % (key, x.pk, self.admin.dtr_root_label(x)) for x in self.objects])
        html = u"<select data-url='%s' data-default-query='%s' data-default='%s' data-target='%s' class='dtr_select'>%s</select>" \
               % (reverse('dtr_listing'), default_query, value, name, options)

        html_main_select = "<select name='%s' id='%s'></select>" % (name, name)
        html += html_main_select
        return mark_safe(html)
        # return super(SorcererWidget, self).render(name, value, final_attrs)
        #
        #
        #

    @property
    def media(self):
        js_list = [
            static("django_type_rel/dtr.js"),

        ]
        return forms.Media(
            js=js_list,
        )
