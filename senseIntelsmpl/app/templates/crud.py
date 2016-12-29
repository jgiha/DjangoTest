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





Module.objects.create(
  moduleName='test',data={
    "accel": {
      "pitch": 0.05162583142908932,
      "roll": 358.9180023060999,
      "yaw": 88.41593137179046
    },
    "accelRaw": {
      "x": -0.0017278495943173766,
      "y": -0.018815619871020317,
      "z": 0.9628462195396423
    },
    "compass": 88.41024182421185,
    "compassRaw": {
      "x": 0.38670799136161804,
      "y": -14.604934692382812,
      "z": 5.905102252960205
    },
    "gyro": {
      "pitch": 0.08530018482155957,
      "roll": 358.92965845080533,
      "yaw": 88.41337005085171
    },
    "gyroRaw": {
      "x": -0.012549860402941704,
      "y": -0.03786290064454079,
      "z": 0.0020742900669574738
    },
    "humidity": 37.94554901123047,
    "orient": {
      "pitch": 0.1468588055109267,
      "roll": 358.95223457388977,
      "yaw": 88.40925827697137
    },
    "orientRaw": {
      "pitch": 0.00207962142303586,
      "roll": -0.018486613407731056,
      "yaw": 1.5430498123168945
    },
    "pressure": 1026.365234375,
    "temp": 16.053691864013672,
    "tempHumidity": 16.053691864013672,
    "tempPressure": 15.012500762939453
  }
)
Module().save()
