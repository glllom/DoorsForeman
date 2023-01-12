from django.contrib import admin
from .models import *

admin.site.register(DoorType)
admin.site.register(Lock)
admin.site.register(Hinge)
admin.site.register(Order)
admin.site.register(DoorInstance)
admin.site.register(DoorsGroupInstance)


