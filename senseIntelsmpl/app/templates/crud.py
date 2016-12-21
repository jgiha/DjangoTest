from crudbuilder.abstract import BaseCrudBuilder
from app.models import Module

class crud(BaseCrudBuilder):
    model = Module
    search_fields = ['moduleName']
    tables2_fields = ('moduleName','ipAddress')
    tables2_css_class = "table table-bordered table-condensed"
    modelform_excludes = ['created_by', 'updated_by']
    login_required=False
    permission_required=False




    @classmethod
    def custom_queryset(cls, request, **kwargs):
        """Define your own custom queryset for list view"""
        qset = cls.model.objects.filter(Module.moduleName)
        return qset

    #@classmethod
    #def custom_context(cls, request, context **kwargs):
    #    context['custom_data'] = "Some custom data"
    #    return context
