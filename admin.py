class DtrAdmin(object):
    type_rel_fields = {'record': 'type'}

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in self.type_rel_fields:
            return self.formfield_for_type_rel(db_field, **kwargs)

        return super(DtrAdmin, self).formfield_for_dbfield(db_field, **kwargs)

    def formfield_for_type_rel(self, db_field, **kwargs):
        from django_type_rel.widgets import TypeRelWidget

        kwargs.pop("request", None)
        rel_rel_name = self.type_rel_fields[db_field.name]
        kwargs['widget'] = TypeRelWidget(self.model, db_field.rel.to, rel_rel_name)
        return db_field.formfield(**kwargs)

