#class crud(object):
#    """description of class"""


from crudbuilder.abstract import BaseCrudBuilder
from app.models import * 

class ModuleCrud(BaseCrudBuilder):
    model = Module
    search_fields = ['moduleName']
    tables2_fields = ('moduleName', 'ipAddress','SensorReading', 'GpsReading')
    tables2_css_class = "table table-bordered table-condensed"
    tables2_pagination = 20  # default is 10
    #modelform_excludes = ['SensorReading', 'GpsReading']
    login_required=False
    permission_required=False


    #@classmethod
    #def custom_queryset(cls, request, **kwargs):
    #    """Define your own custom queryset for list view"""
    #    qset = cls.model.objects.filter(moduleName)
    #    return qset

class SensorCrud(BaseCrudBuilder):
    model = SensorReading
    search_fields = ['SensorID']
    tables2_fields = ('humidity', 'temp','pressure','orient','orientRaw','compass','compassRaw','gyro','gyroRaw','accel','accelRaw')
    tables2_css_class = "table table-bordered table-condensed"
    tables2_pagination = 20  # default is 10
    login_required=False
    permission_required=False


class GpsCrud(BaseCrudBuilder):
    model = GpsReading
    search_fields = ['GpsID']
    tables2_fields = ('latitude', 'longitude','timeUtc','altitude','speed','climb')
    tables2_css_class = "table table-bordered table-condensed"
    tables2_pagination = 20  # default is 10
    modelform_excludes = ['SensorReading', 'GpsReading']
    login_required=False
    permission_required=False



    #@classmethod
    #def custom_context(cls, request, context, **kwargs):
    #    context['custom_data'] = "Some custom data"
    #    return context

    # permissions = {
    #     'list': 'example.person_list',
    #     'create': 'example.person_create'
    # }
    #createupdate_forms = {
    #    'create': ModuleCreateForm,
    #    'update': ModuleUpdateForm
    #}