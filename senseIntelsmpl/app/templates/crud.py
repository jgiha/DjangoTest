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

